# Deployment Checklist

Use this checklist to deploy your Lead Enrichment Pipeline project.

---

## ☐ Phase 1: Local Setup & Testing

### Frontend Setup
- [ ] Navigate to frontend directory: `cd E:\manage-n8n\frontend`
- [ ] Install dependencies: `npm install`
- [ ] Copy environment file: `cp .env.local.example .env.local`
- [ ] Update `.env.local` with your n8n webhook URL
- [ ] Start dev server: `npm run dev`
- [ ] Open http://localhost:3000 and verify it loads
- [ ] Test form submission (use test data from PROJECT_SUMMARY.md)

### n8n Workflow Setup
- [ ] Go to https://pakfawad.app.n8n.cloud/
- [ ] Import workflow: `workflows/lead_enrichment_pipeline_simplified.json`
- [ ] Configure Gemini API credential (both nodes)
- [ ] Configure Google Sheets OAuth
- [ ] Verify Google Sheet has correct column headers
- [ ] Activate the workflow
- [ ] Copy webhook URL from "Lead Form Submission" node
- [ ] Update `.env.local` with webhook URL
- [ ] Test workflow with sample lead (HubSpot example)
- [ ] Verify data appears in Google Sheet

---

## ☐ Phase 2: GitHub Repository

### Create Repository
- [ ] Go to https://github.com/new
- [ ] Repository name: `lead-enrichment-pipeline`
- [ ] Description: `AI-powered lead enrichment and qualification system with Next.js frontend and n8n automation`
- [ ] Visibility: Public (recommended for portfolio)
- [ ] **DO NOT** initialize with README, .gitignore, or license
- [ ] Click "Create repository"
- [ ] Copy the repository URL

### Push Code to GitHub
```bash
cd E:\manage-n8n\frontend
git remote add origin https://github.com/YOUR_USERNAME/lead-enrichment-pipeline.git
git branch -M main
git push -u origin main
```

- [ ] Run the commands above (replace YOUR_USERNAME)
- [ ] Verify files appear on GitHub
- [ ] Check README.md displays correctly

---

## ☐ Phase 3: Vercel Deployment

### Connect to Vercel
- [ ] Go to https://vercel.com/signup (create account if needed)
- [ ] Click "Add New..." → "Project"
- [ ] Click "Import Git Repository"
- [ ] Select your GitHub repository: `lead-enrichment-pipeline`
- [ ] Click "Import"

### Configure Project
- [ ] Framework Preset: **Next.js** (should auto-detect)
- [ ] Root Directory: `./` (leave default)
- [ ] Build Command: `npm run build` (leave default)
- [ ] Output Directory: `.next` (leave default)

### Add Environment Variables
Click "Environment Variables" and add:

```
NEXT_PUBLIC_N8N_WEBHOOK_URL
Value: [Your n8n webhook URL]

NEXT_PUBLIC_N8N_INSTANCE_URL
Value: https://pakfawad.app.n8n.cloud

GOOGLE_SHEET_ID
Value: 1NSTsnCxlUqeyj_l873BYOLAYOeVz1xjG-F6s5H5uE64
```

- [ ] Add all three environment variables
- [ ] Click "Deploy"
- [ ] Wait for deployment to complete (~2-3 minutes)

### Verify Deployment
- [ ] Click "Visit" to open your live site
- [ ] Test the form with sample data
- [ ] Verify workflow executes
- [ ] Check Google Sheet for results
- [ ] Test on mobile device (responsive design)

---

## ☐ Phase 4: Final Configuration

### Enable Auto-Deployment
- [ ] In Vercel, go to Settings → Git
- [ ] Verify "Production Branch" is set to `main`
- [ ] Verify "Automatic Deployments" is enabled
- [ ] Test: Make a small change, push to GitHub, verify auto-deploy

### Custom Domain (Optional)
- [ ] In Vercel, go to Settings → Domains
- [ ] Add your custom domain
- [ ] Follow DNS configuration instructions
- [ ] Wait for SSL certificate (automatic)

### Performance Optimization
- [ ] In Vercel, check Analytics tab
- [ ] Review Core Web Vitals
- [ ] Optimize images if needed
- [ ] Enable caching if needed

---

## ☐ Phase 5: Testing & Validation

### End-to-End Testing
Test with all three scenarios:

**Hot Lead (Score 70+)**
- [ ] Name: Sarah Johnson
- [ ] Email: sarah@hubspot.com
- [ ] Company: HubSpot
- [ ] Verify: Score 70-85, email generated, saved to sheet

**Warm Lead (Score 40-69)**
- [ ] Name: Mike Chen
- [ ] Email: mike@stripe.com
- [ ] Company: Stripe
- [ ] Verify: Score 40-60, no email, saved to sheet

**Cold Lead (Score <40)**
- [ ] Name: John Smith
- [ ] Email: john@localcafe.com
- [ ] Company: Local Cafe
- [ ] Verify: Score 0-20, archive reason, saved to sheet

### Cross-Browser Testing
- [ ] Test in Chrome
- [ ] Test in Firefox
- [ ] Test in Safari
- [ ] Test in Edge

### Mobile Testing
- [ ] Test on iPhone/iOS
- [ ] Test on Android
- [ ] Verify responsive design
- [ ] Check form usability

---

## ☐ Phase 6: Documentation & Portfolio

### Update Documentation
- [ ] Add live URL to README.md
- [ ] Add screenshots to repository
- [ ] Update CLAUDE.md with deployment info
- [ ] Create demo video (optional)

### Portfolio Presentation
- [ ] Add project to portfolio website
- [ ] Write case study highlighting:
  - Problem solved
  - Technologies used
  - Results/impact
  - Technical challenges overcome
- [ ] Include live demo link
- [ ] Include GitHub repository link

### Share & Promote
- [ ] Share on LinkedIn
- [ ] Share on Twitter/X
- [ ] Add to resume
- [ ] Prepare for interviews (be ready to explain architecture)

---

## ☐ Phase 7: Monitoring & Maintenance

### Set Up Monitoring
- [ ] Monitor Vercel Analytics
- [ ] Check n8n execution history regularly
- [ ] Review Google Sheet data quality
- [ ] Set up error alerts (optional)

### Regular Maintenance
- [ ] Update dependencies monthly: `npm update`
- [ ] Review and optimize workflow
- [ ] Check API quotas (Gemini, Google Search)
- [ ] Backup Google Sheet data

---

## Troubleshooting

### Common Issues

**Form submission fails:**
- Check n8n workflow is activated
- Verify webhook URL is correct in .env.local
- Check browser console for errors

**Workflow doesn't process:**
- Check Gemini API key is valid
- Verify Google Sheets OAuth is connected
- Check n8n execution logs

**Vercel build fails:**
- Check all environment variables are set
- Review build logs in Vercel dashboard
- Verify package.json dependencies

**Styling looks broken:**
- Clear browser cache
- Check Tailwind CSS is configured
- Verify globals.css is imported

---

## Success Criteria

✅ **Project is complete when:**
- [ ] Frontend loads on Vercel
- [ ] Form submits successfully
- [ ] n8n workflow processes leads
- [ ] Data appears in Google Sheet
- [ ] Hot leads get personalized emails
- [ ] Auto-deployment works (push → deploy)
- [ ] Mobile responsive
- [ ] No console errors
- [ ] All test scenarios pass

---

## Support

If you encounter issues:
1. Check PROJECT_SUMMARY.md for overview
2. Review CLAUDE.md for detailed instructions
3. Check n8n execution logs
4. Review Vercel deployment logs
5. Ask Claude for help (I have full context!)

---

**Last Updated**: 2026-04-17
**Status**: Ready to deploy! 🚀
