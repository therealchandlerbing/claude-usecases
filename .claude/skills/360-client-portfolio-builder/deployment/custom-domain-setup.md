# Custom Domain Setup Guide

**Purpose:** Connect your portfolio to a custom domain (e.g., `ecogrid.com`)
**Cost:** $12-15/year for domain registration
**Time:** 1-48 hours (depending on DNS propagation)

---

## Overview

A custom domain makes your portfolio look professional:
- ❌ `random-site-123.netlify.app`
- ✅ `ecogrid.com`

---

## Step 1: Purchase a Domain

### Recommended Registrars

**Namecheap** (https://www.namecheap.com)
- ✅ Affordable ($10-13/year for .com)
- ✅ Free WHOIS privacy
- ✅ Easy DNS management
- ✅ Good support

**Google Domains** (https://domains.google)
- ✅ Clean interface
- ✅ Free WHOIS privacy
- ✅ Integrates with Google Workspace
- ⚠️ Slightly more expensive ($12-14/year)

**GoDaddy** (https://www.godaddy.com)
- ✅ Largest registrar
- ✅ 24/7 support
- ⚠️ Upsells and renewals can be pricey

**Cloudflare** (https://www.cloudflare.com/products/registrar/)
- ✅ At-cost pricing (no markup)
- ✅ Free DNS and CDN
- ⚠️ Requires existing Cloudflare account

### Choosing a Domain Name

**Best Practices:**
- Short and memorable
- Easy to spell and pronounce
- Avoid hyphens and numbers
- Use .com if available (most trusted)
- Alternative TLDs: .org, .io, .co

**Examples:**
- ✅ `ecogrid.com`
- ✅ `healthbridge.org`
- ✅ `learnlocal.io`
- ⚠️ `eco-grid-solutions.com` (too long, has hyphens)

### Purchase Process

1. Search for your desired domain
2. Add to cart
3. Select registration period (1 year minimum, multi-year for discount)
4. Enable WHOIS privacy (hides personal info)
5. Decline upsells (hosting, email, etc.—not needed)
6. Complete purchase

---

## Step 2: DNS Configuration

DNS (Domain Name System) connects your domain to your hosting.

### Understanding DNS Records

**A Record:** Points domain to IP address
**CNAME Record:** Points subdomain to another domain
**Nameservers:** Control where DNS is managed

### Option A: Netlify DNS (Recommended)

**Advantages:**
- Simplest setup
- Automatic configuration
- No manual DNS records

**Steps:**

1. **In Netlify:**
   - Go to **Site settings** → **Domain management**
   - Click **"Add custom domain"**
   - Enter your domain (e.g., `ecogrid.com`)
   - Click **"Verify"** → **"Yes, add domain"**
   - Netlify shows 4 nameservers (e.g., `dns1.p01.nsone.net`)

2. **In Your Registrar (Namecheap example):**
   - Log in to Namecheap
   - Go to **Domain List** → Select your domain
   - Click **"Manage"**
   - Find **"Nameservers"** section
   - Select **"Custom DNS"**
   - Enter all 4 Netlify nameservers
   - Save changes

3. **Wait for Propagation:**
   - DNS changes take 1-48 hours (usually 1-4 hours)
   - Check status: https://dnschecker.org

4. **Enable HTTPS in Netlify:**
   - Once DNS propagates, Netlify auto-provisions SSL
   - Go to **Site settings** → **HTTPS**
   - Enable **"Force HTTPS"**

### Option B: External DNS (Keep Current Provider)

**Use when:** You want to keep DNS at registrar (Namecheap, GoDaddy, etc.)

**Steps:**

1. **In Netlify:**
   - Add custom domain (see Option A, step 1)
   - Netlify provides an IP address (e.g., `75.2.60.5`)

2. **In Your DNS Provider:**

   **For Root Domain (ecogrid.com):**
   ```
   Type: A Record
   Host: @ (or blank)
   Value: 75.2.60.5 (Netlify IP)
   TTL: 3600 (or automatic)
   ```

   **For www Subdomain (www.ecogrid.com):**
   ```
   Type: CNAME Record
   Host: www
   Value: your-site.netlify.app
   TTL: 3600 (or automatic)
   ```

3. **Wait for Propagation:** 1-24 hours

4. **Enable HTTPS:** Netlify auto-provisions after DNS verification

### Option C: GitHub Pages DNS

**Steps:**

1. **In GitHub:**
   - Go to repo **Settings** → **Pages**
   - Under **"Custom domain"**, enter your domain
   - Click **"Save"**

2. **In Your DNS Provider:**

   **For Root Domain:**
   ```
   Type: A Record (create 4 records)
   Host: @
   Value: 185.199.108.153
   Value: 185.199.109.153
   Value: 185.199.110.153
   Value: 185.199.111.153
   ```

   **For www Subdomain:**
   ```
   Type: CNAME Record
   Host: www
   Value: your-username.github.io
   ```

3. **Wait for Propagation:** 1-48 hours

4. **Enable HTTPS:** Check "Enforce HTTPS" in GitHub Pages settings

---

## Step 3: Verify DNS Configuration

### Check DNS Propagation

**Tool:** https://dnschecker.org

1. Enter your domain
2. Select **A** or **CNAME** record type
3. Click **"Search"**
4. Green checkmarks = propagated globally
5. Red X = still propagating (wait longer)

**Typical Propagation Times:**
- Minimum: 15 minutes
- Typical: 1-4 hours
- Maximum: 48 hours

### Test Your Site

1. Open incognito/private browser window
2. Go to `http://yourdomain.com`
3. Should redirect to `https://yourdomain.com`
4. Should show your portfolio

**If not working:**
- Clear browser cache
- Wait longer for DNS propagation
- Check DNS configuration

---

## Step 4: SSL/HTTPS Setup

### Netlify (Automatic)

1. After DNS propagates, Netlify auto-provisions SSL (Let's Encrypt)
2. Go to **Site settings** → **Domain management** → **HTTPS**
3. Click **"Verify DNS configuration"**
4. Click **"Provision certificate"**
5. Wait 1-2 minutes
6. Enable **"Force HTTPS"** (redirects HTTP → HTTPS)

### GitHub Pages (Automatic)

1. After DNS propagates, wait 24 hours
2. Go to repo **Settings** → **Pages**
3. ✅ Check **"Enforce HTTPS"**
4. If grayed out, wait longer for certificate provisioning

---

## Common DNS Configurations

### Scenario 1: Root Domain Only

**Want:** `ecogrid.com` (no www)

**DNS Records:**
```
Type: A
Host: @
Value: [Netlify IP or GitHub IPs]

Type: CNAME (optional redirect)
Host: www
Value: ecogrid.com
```

### Scenario 2: www Subdomain Only

**Want:** `www.ecogrid.com`

**DNS Records:**
```
Type: CNAME
Host: www
Value: your-site.netlify.app (or username.github.io)

Type: A (redirect root to www)
Host: @
Value: [Netlify IP]
```

**In Netlify:** Set `www.ecogrid.com` as primary domain

### Scenario 3: Both Root and www

**Want:** Both work, redirect to one

**DNS Records:**
```
Type: A
Host: @
Value: [Netlify IP]

Type: CNAME
Host: www
Value: your-site.netlify.app
```

**In Netlify:** Select primary domain (redirects other to it)

---

## Troubleshooting

### Issue: "Domain Already Claimed"

**Cause:** Domain registered to another Netlify site

**Solution:**
1. Remove domain from old site first
2. Or contact Netlify support

### Issue: SSL Certificate Error

**Causes:**
1. DNS not fully propagated
2. Certificate not provisioned yet

**Solutions:**
1. Wait 24-48 hours
2. Try **"Renew certificate"** in Netlify
3. Check DNS configuration is correct

### Issue: Site Not Loading on Custom Domain

**Causes:**
1. DNS not propagated
2. DNS records incorrect
3. Browser cache

**Solutions:**
1. Check https://dnschecker.org
2. Verify DNS records match hosting provider's requirements
3. Clear browser cache / try incognito mode
4. Wait longer for propagation

### Issue: www Works But Root Doesn't (or Vice Versa)

**Cause:** Missing DNS record

**Solution:**
1. Check both A and CNAME records configured
2. Set primary domain in hosting provider
3. Enable redirects

---

## Best Practices

1. **Enable WHOIS privacy:** Protects personal information
2. **Auto-renew domain:** Don't risk losing it
3. **Use HTTPS:** Always enable Force HTTPS
4. **Set up redirects:** Ensure root and www both work
5. **Monitor expiration:** Set calendar reminder before renewal
6. **Keep contact info current:** Registrar needs to reach you
7. **Use strong password:** For registrar account

---

## Cost Breakdown

**Initial Costs:**
- Domain registration: $10-15/year
- Hosting: $0 (Netlify or GitHub Pages free tier)
- SSL certificate: $0 (automatic Let's Encrypt)

**Annual Costs:**
- Domain renewal: $10-20/year (price may increase)
- Hosting: $0 (for typical portfolio traffic)

**Total:** ~$15/year

---

## Quick Reference

### DNS Record Types

| Type | Purpose | Example |
|------|---------|---------|
| A | Points domain to IP | `@ → 75.2.60.5` |
| CNAME | Points subdomain to domain | `www → site.netlify.app` |
| NS | Nameserver (controls DNS) | `dns1.p01.nsone.net` |

### Common TTL Values

- **300** (5 min): Fast changes, testing
- **3600** (1 hour): Standard
- **86400** (24 hours): Stable, rarely changing

### Checking Tools

- **DNS Propagation:** https://dnschecker.org
- **WHOIS Lookup:** https://whois.domaintools.com
- **SSL Checker:** https://www.sslshopper.com/ssl-checker.html

---

## Next Steps

After custom domain is configured:

1. ✅ Test on multiple browsers and devices
2. ✅ Verify HTTPS works and is enforced
3. ✅ Update all references to old URL
4. ✅ Set up email forwarding (if needed)
5. ✅ Configure analytics (optional)
6. ✅ Set renewal reminder for 11 months

---

**Domain connected!** Your portfolio now has a professional custom URL.
