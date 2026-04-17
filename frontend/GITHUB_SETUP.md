# GitHub Repository Setup Instructions

## Repository Name (Professional)
**Recommended**: `lead-enrichment-pipeline`

Alternative names:
- `ai-lead-qualification-system`
- `n8n-lead-enrichment-frontend`
- `smart-lead-scoring-app`

---

## Create Repository on GitHub

### Option 1: Via GitHub Website

1. Go to: https://github.com/new
2. **Repository name**: `lead-enrichment-pipeline`
3. **Description**: `AI-powered lead enrichment and qualification system with Next.js frontend and n8n automation`
4. **Visibility**: Public (for portfolio) or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### Option 2: Via GitHub MCP (if available)

Ask Claude to create the repository using the GitHub MCP server.

---

## Connect Local Repository to GitHub

After creating the repository on GitHub, run these commands:

```bash
cd E:\manage-n8n\frontend

# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/lead-enrichment-pipeline.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Verify Setup

After pushing, verify:
1. Visit your repository URL
2. Check all files are uploaded
3. README.md displays correctly
4. .gitignore is working (no node_modules, .env files)

---

## Next Steps: Deploy to Vercel

1. Go to: https://vercel.com/new
2. Click **"Import Git Repository"**
3. Select your GitHub repository: `lead-enrichment-pipeline`
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `./` (or leave default)
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
5. Add **Environment Variables**:
   ```
   NEXT_PUBLIC_N8N_WEBHOOK_URL=https://pakfawad.app.n8n.cloud/webhook/lead-enrichment-form
   NEXT_PUBLIC_N8N_INSTANCE_URL=https://pakfawad.app.n8n.cloud
   GOOGLE_SHEET_ID=1NSTsnCxlUqeyj_l873BYOLAYOeVz1xjG-F6s5H5uE64
   ```
6. Click **"Deploy"**

---

## Auto-Deployment Setup

Once connected to Vercel:
- Every push to `main` branch → Auto-deploys to production
- Pull requests → Create preview deployments
- Rollback available via Vercel dashboard

---

## Your GitHub Username

What's your GitHub username? I'll provide the exact commands with your username filled in.
