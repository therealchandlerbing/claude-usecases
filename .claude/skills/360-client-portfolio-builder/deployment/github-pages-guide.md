# GitHub Pages Deployment Guide

**Platform:** GitHub Pages
**Cost:** Free
**Best For:** Developers familiar with Git, version-controlled portfolios
**Time to Deploy:** 10-15 minutes

---

## Why GitHub Pages?

**Advantages:**
- ✅ Completely free
- ✅ Automatic HTTPS
- ✅ Custom domain support
- ✅ Version control with Git
- ✅ Automatic deployment from repository
- ✅ No bandwidth limits

**Limitations:**
- ⚠️ Requires Git/GitHub knowledge
- ⚠️ Public repositories only (free tier)
- ⚠️ 1 GB repository size limit
- ⚠️ Less intuitive than Netlify for non-developers

---

## Prerequisites

- GitHub account (free at https://github.com)
- Git installed locally (or use GitHub web interface)
- Portfolio HTML file named `index.html`

---

## Method 1: Web Interface (No Git Required)

**Best for:** Non-developers, quick deployment

### Step 1: Create Repository

1. Log in to GitHub
2. Click **"+"** (top right) → **"New repository"**
3. Repository name: `portfolio` (or `your-client-name`)
4. Make it **Public**
5. ✅ Check **"Add a README file"**
6. Click **"Create repository"**

### Step 2: Upload Your File

1. In your new repository, click **"Add file"** → **"Upload files"**
2. Drag your `index.html` (and any images/assets)
3. Scroll down, add commit message: "Add portfolio page"
4. Click **"Commit changes"**

### Step 3: Enable GitHub Pages

1. Go to repository **Settings** tab
2. Scroll to **"Pages"** section (left sidebar)
3. Under **"Source"**, select **"Deploy from a branch"**
4. Under **"Branch"**, select **"main"** and **"/ (root)"**
5. Click **"Save"**
6. Wait 1-2 minutes

### Step 4: Access Your Site

Your site is now live at:
```
https://your-username.github.io/portfolio/
```

Replace:
- `your-username` with your GitHub username
- `portfolio` with your repository name

---

## Method 2: Git Command Line

**Best for:** Developers, faster updates

### Step 1: Create Repository

1. Create new repository on GitHub (see Method 1, Step 1)
2. Copy repository URL (e.g., `https://github.com/username/portfolio.git`)

### Step 2: Initialize Local Repository

```bash
# Navigate to folder with index.html
cd /path/to/your/portfolio

# Initialize Git
git init

# Add all files
git add index.html
# Or add everything: git add .

# Commit
git commit -m "Initial portfolio commit"

# Add remote
git remote add origin https://github.com/username/portfolio.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

Follow Method 1, Step 3

### Step 4: Update Your Site

```bash
# Make changes to index.html

# Stage changes
git add index.html

# Commit
git commit -m "Update portfolio content"

# Push
git push

# Site updates in 1-2 minutes
```

---

## Custom Domain Setup

### Prerequisites

- Own a domain (e.g., `ecogrid.com`)

### Step 1: Configure GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Under **"Custom domain"**, enter your domain
3. Click **"Save"**
4. GitHub creates a `CNAME` file in your repository

### Step 2: Configure DNS

**For Root Domain (e.g., ecogrid.com):**

1. Go to your DNS provider (Namecheap, GoDaddy, etc.)
2. Create **A records** pointing to GitHub's servers:

```
Type: A
Host: @
Value: 185.199.108.153

Type: A
Host: @
Value: 185.199.109.153

Type: A
Host: @
Value: 185.199.110.153

Type: A
Host: @
Value: 185.199.111.153
```

**For Subdomain (e.g., www.ecogrid.com):**

```
Type: CNAME
Host: www
Value: your-username.github.io
```

### Step 3: Enable HTTPS

1. Wait 24-48 hours for DNS propagation
2. Go to repository **Settings** → **Pages**
3. ✅ Check **"Enforce HTTPS"**
4. SSL certificate provisioned automatically (Let's Encrypt)

---

## User/Organization Page (username.github.io)

**Special repository:** Named exactly `username.github.io`

**Advantage:** Site lives at `https://username.github.io/` (no `/portfolio` path)

### Setup

1. Create repository named **exactly** `your-username.github.io`
2. Upload `index.html`
3. No need to enable Pages—it's automatic!
4. Site live at `https://your-username.github.io/`

**Example:**
- Username: `360studios`
- Repository: `360studios.github.io`
- URL: `https://360studios.github.io/`

---

## Troubleshooting

### Issue: 404 Page Not Found

**Causes:**
1. File not named `index.html`
2. GitHub Pages not enabled
3. Deployment not complete

**Solutions:**
1. Ensure file is named exactly `index.html` (case-sensitive)
2. Check **Settings** → **Pages** is configured
3. Wait 2-5 minutes after push

### Issue: Changes Not Showing

**Causes:**
1. Browser cache
2. Deployment in progress

**Solutions:**
1. Hard refresh (Ctrl+F5 / Cmd+Shift+R)
2. Check **Actions** tab for deployment status
3. Wait 1-2 minutes after git push

### Issue: Custom Domain Not Working

**Causes:**
1. DNS not propagated
2. CNAME file missing/incorrect

**Solutions:**
1. Check DNS propagation: https://dnschecker.org
2. Verify `CNAME` file in repository contains correct domain
3. Wait 24-48 hours for DNS propagation

---

## Limitations & Workarounds

### Public Repository Required (Free Tier)

**Limitation:** Free GitHub accounts require public repositories for Pages

**Workaround:**
- Use Netlify if privacy needed
- Upgrade to GitHub Pro ($4/month) for private repos + Pages

### No Server-Side Processing

**Limitation:** Static files only (HTML, CSS, JS)

**Workaround:**
- Use Netlify for forms/functions
- Use external services (FormSpree for forms, etc.)

### Build Time

**Limitation:** Takes 1-2 minutes to deploy after push

**Workaround:**
- Test locally before pushing
- Use Netlify for instant deployments

---

## Quick Reference

### Useful Commands

```bash
# Clone your repository
git clone https://github.com/username/portfolio.git

# Update content
git add index.html
git commit -m "Update portfolio"
git push

# Check status
git status

# View remote URL
git remote -v
```

### Useful URLs

- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **GitHub IP Addresses:** https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain
- **DNS Checker:** https://dnschecker.org

---

## Best Practices

1. **Use meaningful commit messages:** "Update traction metrics" not "changes"
2. **Test locally first:** Open `index.html` in browser before pushing
3. **Use .gitignore:** Exclude unnecessary files
4. **Branch for major changes:** Use branches for experimental updates
5. **Enable HTTPS:** Always enforce HTTPS for security
6. **Monitor Actions tab:** Check deployment status

---

## Comparison: GitHub Pages vs. Netlify

| Feature | GitHub Pages | Netlify |
|---------|-------------|---------|
| **Cost** | Free | Free (generous tier) |
| **Ease of Use** | Medium (Git knowledge) | Easy (drag-and-drop) |
| **Deployment Speed** | 1-2 minutes | 10-30 seconds |
| **Custom Domain** | Yes | Yes |
| **HTTPS** | Yes (automatic) | Yes (automatic) |
| **Forms** | No | Yes (free tier: 100/month) |
| **Redirects** | Limited | Full support |
| **Best For** | Developers | Non-developers |

---

## Next Steps

After deploying:

1. ✅ Test at live URL
2. ✅ Verify on mobile devices
3. ✅ Set up custom domain (if applicable)
4. ✅ Enable HTTPS enforcement
5. ✅ Share URL with client
6. ✅ Document update process for client

---

**Alternative:** See [Netlify Guide](netlify-guide.md) for easier deployment
