# Intelligence Dashboard - Deployment Troubleshooting Guide

This guide covers common deployment issues and their solutions for deploying the Intelligence Dashboard to Vercel.

## Table of Contents

1. [Environment Variable Errors](#environment-variable-errors)
2. [Build Failures](#build-failures)
3. [Supabase Connection Issues](#supabase-connection-issues)
4. [General Deployment Tips](#general-deployment-tips)

---

## Environment Variable Errors

### Error: "Environment Variable references Secret which does not exist"

**Full Error Message:**
```
Environment Variable "NEXT_PUBLIC_SUPABASE_URL" references Secret "supabase_url", which does not exist.
```

**Cause:**
- Vercel is trying to reference a Vercel Secret (using the `@` prefix) that doesn't exist in your account
- The `vercel.json` file previously contained secret references, which have now been removed

**Solution:**

1. **Delete existing environment variables** in the Vercel deployment screen:
   - Look for the X or trash icon next to each variable
   - Remove both `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`

2. **Add the variables again with actual values**:

   **Environment Variable #1:**
   - **Key:** `NEXT_PUBLIC_SUPABASE_URL`
   - **Value:** `https://nzvmihdgbvomjlkelcum.supabase.co`
   - ✅ Paste the actual URL directly

   **Environment Variable #2:**
   - **Key:** `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - **Value:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im56dm1paGRnYnZvbWpsa2VsY3VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM3OTg0MzYsImV4cCI6MjA3OTM3NDQzNn0.8Z88SBISSMMJPoIqz_i3nc5KoiYKeNCJbaoI82Ijl30`
   - ✅ Paste the full JWT token directly

3. **Click "Deploy"** to retry the deployment

**Important Notes:**
- ❌ **DO NOT** use `@supabase_url` or any `@` syntax - this tells Vercel to look for a secret
- ❌ **DO NOT** create Vercel Secrets first - just paste the values directly
- ✅ **DO** paste the actual values into the "Value" field
- ✅ **DO** ensure values appear as plain text (URL and JWT token)

**Why This Happens:**
- The `@` prefix in environment variables tells Vercel to look for a stored secret
- Since `NEXT_PUBLIC_*` variables are exposed to the browser anyway, there's no security benefit to using secrets
- The `vercel.json` file has been updated to remove secret references

**Screenshots:**

The Vercel environment variable screen should look like this:

```
┌─────────────────────────────────────────────────────────────┐
│ Environment Variables                                       │
├─────────────────────────────────────────────────────────────┤
│ Key: NEXT_PUBLIC_SUPABASE_URL                              │
│ Value: https://nzvmihdgbvomjlkelcum.supabase.co           │
│                                                             │
│ Key: NEXT_PUBLIC_SUPABASE_ANON_KEY                         │
│ Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...           │
└─────────────────────────────────────────────────────────────┘
```

**NOT like this:**
```
┌─────────────────────────────────────────────────────────────┐
│ Key: NEXT_PUBLIC_SUPABASE_URL                              │
│ Value: @supabase_url  ❌ WRONG                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Build Failures

### Error: "Build failed with exit code 1"

**Common Causes:**
1. TypeScript type errors
2. Missing dependencies
3. ESLint errors
4. Environment variables not set

**Solution:**

1. **Test the build locally first:**
   ```bash
   cd intelligence-dashboard
   npm ci  # Clean install
   npm run build  # Should complete without errors
   ```

2. **Check for TypeScript errors:**
   ```bash
   npm run type-check
   ```

3. **Fix any type errors** before deploying

4. **Review Vercel build logs** for specific error messages

### Error: "Module not found"

**Symptoms:**
```
Error: Cannot find module '@/lib/supabase'
```

**Solution:**

1. **Check path aliases** in `tsconfig.json`:
   ```json
   {
     "compilerOptions": {
       "paths": {
         "@/*": ["./src/*"]
       }
     }
   }
   ```

2. **Verify file exists** at the correct location:
   ```bash
   ls -la src/lib/supabase.ts
   ```

3. **Ensure dependencies are installed:**
   ```bash
   npm install @supabase/supabase-js
   ```

---

## Supabase Connection Issues

### Error: Dashboard loads but shows "No data available"

**Causes:**
1. Environment variables not set correctly
2. Supabase database is empty
3. Database functions not created
4. RLS policies blocking access

**Solution:**

1. **Verify environment variables in Vercel:**
   - Go to Project Settings → Environment Variables
   - Check that both variables are set with correct values
   - Redeploy if you made changes

2. **Check Supabase connection** from browser console:
   ```javascript
   // Open browser console on your deployed site
   console.log(process.env.NEXT_PUBLIC_SUPABASE_URL)
   // Should show: https://nzvmihdgbvomjlkelcum.supabase.co
   ```

3. **Verify database has data:**
   - Go to Supabase → Table Editor → extractions
   - Check if there are rows in the table
   - If empty, run a test insert

4. **Test database functions:**
   - Go to Supabase → SQL Editor
   - Run: `SELECT get_dashboard_metrics();`
   - Should return data without errors

5. **Check RLS policies:**
   - Go to Supabase → Authentication → Policies
   - Ensure policies allow read access for anonymous users

### Error: Real-time updates not working

**Solution:**

1. **Enable real-time replication:**
   - Go to Supabase → Database → Replication
   - Enable replication for `extractions`, `experiments`, `edits`, and `weekly_analyses` tables

2. **Check browser console** for subscription errors:
   ```javascript
   // Look for errors like:
   Error: Realtime not enabled for table 'extractions'
   ```

3. **Verify table has REPLICA IDENTITY:**
   ```sql
   -- Run in Supabase SQL Editor
   ALTER TABLE extractions REPLICA IDENTITY FULL;
   ALTER TABLE experiments REPLICA IDENTITY FULL;
   ALTER TABLE edits REPLICA IDENTITY FULL;
   ALTER TABLE weekly_analyses REPLICA IDENTITY FULL;
   ```

---

## General Deployment Tips

### Pre-Deployment Checklist

Before deploying, ensure:

- [ ] All tests pass locally: `npm test`
- [ ] Build completes successfully: `npm run build`
- [ ] TypeScript has no errors: `npm run type-check`
- [ ] Environment variables are documented in `.env.local.example`
- [ ] `vercel.json` is configured correctly (no secret references)
- [ ] Database schema is up to date (`supabase-schema.sql`)
- [ ] Supabase tables have data or are ready to receive data

### Deployment Flow

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin your-branch
   ```

2. **Vercel auto-deploys** (if GitHub integration is set up)

3. **Or deploy manually:**
   ```bash
   npm install -g vercel
   vercel --prod
   ```

### Post-Deployment Verification

After deployment:

1. **Visit the deployed URL** provided by Vercel
2. **Check browser console** for any errors
3. **Test dashboard features:**
   - Metrics cards load
   - Charts render
   - Recent extractions table populates
   - Real-time updates work (if data is being inserted)
4. **Test Supabase connection** by inserting a test row
5. **Verify analytics** (if using Vercel Analytics)

### Rolling Back a Deployment

If a deployment fails or has issues:

1. **Go to Vercel Dashboard** → Your Project → Deployments
2. **Find the last working deployment**
3. **Click the three dots (⋮)** next to it
4. **Select "Promote to Production"**

This instantly rolls back to the previous version.

### Environment-Specific Variables

For production vs. preview vs. development:

1. **Production:** Set in Vercel → Project Settings → Environment Variables → Production
2. **Preview:** Set in Vercel → Project Settings → Environment Variables → Preview
3. **Development:** Set in `.env.local` (not committed to Git)

**Note:** For this project, all environments use the same Supabase instance.

---

## Common Vercel Error Codes

| Error Code | Meaning | Solution |
|------------|---------|----------|
| `DEPLOYMENT_ERROR` | General deployment failure | Check build logs for specific error |
| `BUILD_FAILED` | Build command failed | Fix TypeScript/ESLint errors |
| `FUNCTION_INVOCATION_FAILED` | Serverless function error | Check API route code |
| `ENV_VAR_NOT_FOUND` | Environment variable missing | Add variable in Vercel settings |
| `SECRET_NOT_FOUND` | Referenced secret doesn't exist | Use actual values, not secret references |

---

## Getting Additional Help

If you're still experiencing issues:

1. **Check Vercel Documentation:**
   - [Environment Variables](https://vercel.com/docs/environment-variables)
   - [Build Configuration](https://vercel.com/docs/build-configuration)
   - [Troubleshooting](https://vercel.com/docs/troubleshooting)

2. **Check Supabase Documentation:**
   - [Database Connection](https://supabase.com/docs/guides/database)
   - [Realtime](https://supabase.com/docs/guides/realtime)
   - [Client Libraries](https://supabase.com/docs/reference/javascript/introduction)

3. **Review Logs:**
   - **Vercel Build Logs:** Vercel Dashboard → Your Project → Deployments → [Click deployment] → Build Logs
   - **Vercel Function Logs:** Vercel Dashboard → Your Project → Deployments → [Click deployment] → Function Logs
   - **Browser Console:** Right-click on deployed site → Inspect → Console

4. **Common Resources:**
   - [Next.js Documentation](https://nextjs.org/docs)
   - [Vercel Community](https://github.com/vercel/vercel/discussions)
   - [Supabase Discord](https://discord.supabase.com)

---

## Success Indicators

You know the deployment is successful when:

✅ Build completes without errors
✅ Vercel provides a deployment URL
✅ Dashboard loads at the URL
✅ Metrics cards show correct data (or "No data" if database is empty)
✅ Charts render properly
✅ No errors in browser console
✅ Real-time updates work (if data is being inserted)
✅ Custom domain works (if configured)

---

**Last Updated:** 2025-01-23
**Project:** Intelligence Dashboard
**Maintainer:** 360 Social Impact Studios
