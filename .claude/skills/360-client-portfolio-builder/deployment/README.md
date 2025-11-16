# Deployment Guides

**Purpose:** Step-by-step instructions for deploying portfolio pages to various hosting platforms

**Status:** Planned - Guides will be created based on common deployment needs

---

## Planned Deployment Guides

### 1. Netlify Deployment (Primary Recommendation)
- **File:** `netlify-guide.md`
- **Why:** Free, instant deployment, custom domains, SSL automatic
- **Best For:** Most portfolios, non-technical clients
- **Status:** 📝 Planned

### 2. GitHub Pages Deployment
- **File:** `github-pages-guide.md`
- **Why:** Free, version controlled, GitHub ecosystem integration
- **Best For:** Technical clients, open-source projects
- **Status:** 📝 Planned

### 3. Custom Domain Setup
- **File:** `custom-domain-setup.md`
- **Why:** Professional branding (venture.com vs venture.netlify.app)
- **Best For:** Client-facing portfolios, investor materials
- **Status:** 📝 Planned

---

## Quick Reference

### Recommended Hosting by Use Case

**Investor Preparation:**
- **Platform:** Netlify with custom domain
- **Why:** Professional URL, fast, reliable
- **Cost:** Free hosting + $12-15/year domain

**Partnership Development:**
- **Platform:** Netlify (custom or .netlify.app)
- **Why:** Easy to update, shareable link
- **Cost:** Free

**Ecosystem Visibility:**
- **Platform:** GitHub Pages
- **Why:** Open source signal, developer credibility
- **Cost:** Free

**360 Portfolio Showcase:**
- **Platform:** Netlify with 360 subdomain
- **Why:** Unified 360.org/portfolio/[client] structure
- **Cost:** Free (360-managed domain)

---

## What Each Guide Will Include

**1. Prerequisites**
- What you need before starting
- Account setup requirements
- File preparation checklist

**2. Step-by-Step Deployment**
- Detailed instructions with screenshots
- Troubleshooting common issues
- Verification steps

**3. Custom Domain Configuration**
- DNS setup walkthrough
- SSL/HTTPS configuration
- Email forwarding (if applicable)

**4. Updating Deployed Site**
- How to make changes
- Deployment workflow
- Version control best practices

**5. Client Handoff**
- How to transfer ownership
- Update instructions for non-technical clients
- Maintenance considerations

---

## Deployment Decision Tree

```
Do you need custom domain (venture.com)?
├─ YES → Use Netlify + Custom Domain Guide
└─ NO
   ├─ Do you need version control/Git workflow?
   │  ├─ YES → Use GitHub Pages
   │  └─ NO → Use Netlify (*.netlify.app subdomain)
   └─ Is this part of 360's portfolio?
      └─ YES → Use Netlify with 360 subdomain
```

---

## Common Deployment Scenarios

### Scenario 1: First Portfolio, Testing with Client
**Recommended:** Netlify Drop (no account needed)
- Drag HTML to drop.netlify.com
- Get instant live URL
- Share with client for feedback
- Claim site later if approved

### Scenario 2: Production Portfolio for Investor Use
**Recommended:** Netlify + Custom Domain
- Create Netlify account
- Deploy HTML
- Purchase domain (Namecheap, Google Domains)
- Configure DNS
- Client has professional URL

### Scenario 3: Multiple Portfolios for 360 Website
**Recommended:** Netlify with 360 subdomain structure
- Deploy to 360-managed Netlify account
- Use 360.org/portfolio/[client-name] structure
- Maintain consistent 360 branding
- Centralized management

### Scenario 4: Technical Client Who Uses GitHub
**Recommended:** GitHub Pages
- Create repository for portfolio
- Enable GitHub Pages
- Deploy via Git push
- Client can update via pull requests

---

## Platform Comparison

| Feature | Netlify | GitHub Pages | Custom Server |
|---------|---------|--------------|---------------|
| **Cost** | Free | Free | $5-20/month |
| **Setup Time** | 5 min | 10 min | 30-60 min |
| **Custom Domain** | Yes (easy) | Yes (moderate) | Yes (complex) |
| **SSL/HTTPS** | Automatic | Automatic | Manual |
| **Deployment** | Drag & drop | Git push | FTP/SSH |
| **Updates** | Instant | 1-2 min | Immediate |
| **Technical Skill** | None | Basic Git | Advanced |
| **Best For** | Most portfolios | Developer clients | Special needs |

---

## Quick Deployment Checklist

Before deploying, ensure:

- [ ] HTML file named `index.html`
- [ ] All images included and paths correct
- [ ] External resources (fonts, CDN) use HTTPS
- [ ] Tested locally in browser
- [ ] No console errors
- [ ] Mobile responsive verified
- [ ] Client has approved content

---

## Support & Troubleshooting

**Common deployment issues:**

**Images don't load after deployment**
→ Check file paths are relative, not absolute
→ Ensure images are in same directory as HTML

**Fonts don't display correctly**
→ Verify Google Fonts links use HTTPS
→ Check font names match CSS exactly

**Custom domain not working**
→ DNS propagation takes 24-48 hours
→ Verify DNS records match hosting provider requirements

**Site loads but styling is broken**
→ Check CSS is embedded in HTML (not external file)
→ Verify all CSS selectors are correct

---

## Contributing Deployment Guides

**Want to add a deployment guide?**

1. Choose a platform (Netlify, GitHub Pages, Vercel, etc.)
2. Document complete deployment process with screenshots
3. Include troubleshooting section
4. Test with someone unfamiliar with platform
5. Submit guide following the structure above

---

**Last Updated:** 2025-11-16
**Status:** Awaiting deployment guide creation based on first production deployments
