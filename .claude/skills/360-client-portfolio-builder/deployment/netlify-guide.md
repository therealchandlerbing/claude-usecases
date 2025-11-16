# Netlify Deployment Guide

**Platform:** Netlify
**Cost:** Free tier available (generous limits)
**Best For:** Quick deployments, custom domains, automatic HTTPS
**Time to Deploy:** 5-10 minutes

---

## Why Netlify?

**Advantages:**
- ✅ Free tier with generous limits
- ✅ Automatic HTTPS/SSL
- ✅ Custom domain support
- ✅ Instant global CDN
- ✅ Easy updates (drag-and-drop)
- ✅ Form handling (contact forms)
- ✅ No credit card required for free tier

**Limitations:**
- ⚠️ 300 build minutes/month (free tier)
- ⚠️ 100 GB bandwidth/month (free tier)
- ⚠️ Random URL unless you configure custom domain

---

## Quick Deployment (No Account)

**Use for:** Testing, quick sharing, temporary deployment

### Step 1: Prepare Your File

1. Save your portfolio HTML as `index.html`
2. All CSS and JavaScript should be embedded (single-file deployment)
3. If using images, keep them in same folder or use external URLs

### Step 2: Deploy to Netlify Drop

1. Go to **https://app.netlify.com/drop**
2. Drag your `index.html` (and images folder if applicable) into the upload zone
3. Netlify generates a live URL instantly (e.g., `random-name-123.netlify.app`)

**Limitations:**
- Site expires after 24 hours if you don't claim it
- Random URL (e.g., `loving-kare-123abc.netlify.app`)
- Can't update easily

---

## Recommended: Netlify with Account

**Use for:** Production deployments, custom domains, ongoing updates

### Step 1: Create Netlify Account

1. Go to **https://www.netlify.com**
2. Click **Sign Up** (free)
3. Sign up with:
   - GitHub account (recommended)
   - GitLab account
   - Bitbucket account
   - Email address

**No credit card required for free tier**

### Step 2: Deploy Your Site

**Option A: Manual Deploy (Easiest)**

1. Log in to Netlify
2. Click **"Sites"** in the top navigation
3. Scroll down to **"Want to deploy a new site without connecting to Git?"**
4. Click **"Deploy manually"**
5. Drag your `index.html` (and any assets) into the deploy zone
6. Wait 10-30 seconds
7. Site goes live at `random-name.netlify.app`

**Option B: Git-Connected Deploy (Best for Updates)**

1. Push your portfolio to GitHub repository
2. In Netlify, click **"Add new site"** → **"Import an existing project"**
3. Select **GitHub** (or GitLab/Bitbucket)
4. Authorize Netlify to access your repositories
5. Select your portfolio repository
6. Configure build settings:
   - **Build command:** Leave empty (static site)
   - **Publish directory:** Leave empty or enter `/` if index.html is at root
7. Click **"Deploy site"**

**Advantage:** Any push to GitHub automatically redeploys site

### Step 3: Customize Site Name

Your site will have a random URL like `loving-kare-123abc.netlify.app`. Change it:

1. Go to **Site settings**
2. Click **"Change site name"** (under Site information)
3. Enter new name (e.g., `ecogrid-portfolio`)
4. New URL: `ecogrid-portfolio.netlify.app`

**Requirements:**
- Must be unique across all Netlify sites
- Lowercase letters, numbers, hyphens only
- No spaces or special characters

### Step 4: Update Your Site

**Manual Deploy:**
1. Go to your site dashboard
2. Click **"Deploys"** tab
3. Scroll to **"Drag and drop"** section
4. Drag updated `index.html` to deploy zone
5. New version goes live in 10-30 seconds

**Git-Connected Deploy:**
1. Push changes to GitHub
2. Netlify automatically detects and redeploys
3. Takes 1-2 minutes to build and publish

---

## Custom Domain Setup

**Prerequisites:**
- Own a domain (purchased from Namecheap, GoDaddy, Google Domains, etc.)
- Domain costs $12-15/year typically

### Step 1: Add Domain to Netlify

1. Go to **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Enter your domain (e.g., `ecogrid.com`)
4. Click **"Verify"**
5. Netlify asks if you own the domain → Click **"Yes, add domain"**

### Step 2: Configure DNS

**Option A: Use Netlify DNS (Recommended)**

1. Netlify shows nameservers (e.g., `dns1.p01.nsone.net`)
2. Go to your domain registrar (Namecheap, GoDaddy, etc.)
3. Find **DNS settings** or **Nameservers**
4. Change to **Custom nameservers**
5. Enter Netlify's nameservers (all 4 provided)
6. Save changes
7. Wait 24-48 hours for DNS propagation (usually faster, 1-4 hours)

**Option B: Use Existing DNS (A Records)**

If you want to keep your current DNS provider:

1. At Netlify, they'll show you an IP address (e.g., `75.2.60.5`)
2. Go to your DNS provider
3. Create an **A record**:
   - **Host:** `@` (or leave blank for root domain)
   - **Value:** `75.2.60.5` (Netlify's load balancer IP)
   - **TTL:** Automatic or 3600

4. For `www` subdomain, create **CNAME record**:
   - **Host:** `www`
   - **Value:** `your-site.netlify.app`
   - **TTL:** Automatic or 3600

5. Save and wait for propagation (1-24 hours)

### Step 3: Enable HTTPS

1. Once DNS is configured, return to Netlify
2. Go to **Site settings** → **Domain management** → **HTTPS**
3. Click **"Verify DNS configuration"**
4. Click **"Provision certificate"** (free Let's Encrypt SSL)
5. Wait 1-2 minutes
6. HTTPS is now active
7. Enable **"Force HTTPS"** to redirect all HTTP to HTTPS

---

## Advanced Features

### Form Handling (Contact Forms)

Add `netlify` attribute to forms for automatic handling:

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="contact" />
  <label>
    Name: <input type="text" name="name" required />
  </label>
  <label>
    Email: <input type="email" name="email" required />
  </label>
  <label>
    Message: <textarea name="message" required></textarea>
  </label>
  <button type="submit">Send</button>
</form>
```

**Submissions go to:** Netlify dashboard → Forms

### Redirects and Rewrites

Create `_redirects` file in your site root:

```
# Redirect old URL to new URL
/old-page    /new-page    301

# Redirect to external site
/blog        https://medium.com/@yourname    301
```

### Environment Variables

For sites with API keys (if using JavaScript):

1. **Site settings** → **Build & deploy** → **Environment**
2. Click **"Edit variables"**
3. Add key-value pairs
4. Use in build process or client-side code

---

## Troubleshooting

### Issue: Site Not Loading

**Check:**
1. Deployment succeeded? (Go to **Deploys** tab)
2. DNS configured correctly? (Use **https://dnschecker.org**)
3. Clear browser cache (Ctrl+F5 or Cmd+Shift+R)

**Solution:**
- Redeploy site
- Verify DNS settings
- Wait for DNS propagation (up to 48 hours)

### Issue: HTTPS Certificate Error

**Check:**
1. DNS fully propagated?
2. Certificate provisioned?

**Solution:**
1. **Site settings** → **Domain management** → **HTTPS**
2. Click **"Renew certificate"**
3. Wait 1-2 minutes

### Issue: Changes Not Showing

**Cause:** Browser cache

**Solution:**
1. Hard refresh (Ctrl+F5 / Cmd+Shift+R)
2. Clear browser cache
3. Try incognito/private window
4. Check actual deployment time in **Deploys** tab

### Issue: Custom Domain Not Working

**Check:**
1. DNS propagation complete? (Use https://dnschecker.org)
2. Nameservers correct?
3. A/CNAME records pointing to Netlify?

**Solution:**
- Wait 24-48 hours for DNS propagation
- Double-check nameserver configuration
- Use Netlify DNS for simpler setup

---

## Cost & Limits

### Free Tier Includes:

- ✅ 100 GB bandwidth/month
- ✅ 300 build minutes/month (irrelevant for static HTML)
- ✅ Unlimited sites
- ✅ Free SSL certificates
- ✅ Form handling (100 submissions/month)
- ✅ Custom domain support

### When You Need Paid:

**Pro Plan ($19/month):**
- 1 TB bandwidth/month
- Unlimited form submissions
- Role-based access control
- Password-protected sites

**Business Plan ($99/month):**
- 2 TB bandwidth/month
- Analytics
- Priority support

**Most portfolio sites stay free forever**

---

## Quick Reference

### Useful URLs

- **Netlify Dashboard:** https://app.netlify.com
- **Netlify Drop (No Account):** https://app.netlify.com/drop
- **DNS Checker:** https://dnschecker.org
- **Netlify Docs:** https://docs.netlify.com

### Common Commands

**Update Site:**
- Drag new `index.html` to deploy zone

**Check Deployment Status:**
- **Deploys** tab → View latest deploy

**View Live Site:**
- Click **"Open production deploy"** button

---

## Best Practices

1. **Use descriptive site names:** `client-name-portfolio` not `site-123`
2. **Enable Force HTTPS:** Always redirect HTTP to HTTPS
3. **Set up custom domain:** Looks more professional than `.netlify.app`
4. **Test before deploying:** Open `index.html` locally in browser
5. **Keep backups:** Save HTML file locally before updates
6. **Monitor bandwidth:** Check usage if high traffic expected
7. **Use Git integration:** Easier updates, version history

---

## Next Steps

After deploying:

1. ✅ Test on multiple devices (mobile, tablet, desktop)
2. ✅ Check loading speed (https://pagespeed.web.dev)
3. ✅ Verify all links work
4. ✅ Test forms (if applicable)
5. ✅ Share URL with client
6. ✅ Set up custom domain (if applicable)
7. ✅ Enable Force HTTPS

---

**Deployment complete!** 🚀

Your portfolio is now live and accessible worldwide.

For alternative hosting options, see:
- [GitHub Pages Guide](github-pages-guide.md)
- [Custom Domain Setup](custom-domain-setup.md)
