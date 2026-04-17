# Vercel Deployment Guide - Copy & Paste Ready

## 🚀 Quick Deploy Instructions

Follow these exact steps to deploy your project to Vercel.

---

## Step 1: Open Vercel

**Click this link**: https://vercel.com/new

- If you don't have an account, click "Sign Up" (use GitHub to sign up)
- If you have an account, sign in

---

## Step 2: Import Repository

1. You'll see "Import Git Repository"
2. Click **"Add GitHub Account"** or **"Adjust GitHub App Permissions"**
3. In the popup, select your repositories or give access to all
4. Find: **`Ai-Lead-Qualification-System`**
5. Click **"Import"** next to it

---

## Step 3: Configure Project

You'll see a configuration screen. **Leave everything as default** except environment variables:

### ✅ Auto-Detected Settings (Don't Change):
- **Framework Preset**: Next.js
- **Root Directory**: ./
- **Build Command**: npm run build
- **Output Directory**: .next
- **Install Command**: npm install

---

## Step 4: Add Environment Variables

**This is the most important step!**

Click **"Environment Variables"** section to expand it.

### Add These 3 Variables (Copy-Paste):

#### Variable 1:
```
Name (left box):
NEXT_PUBLIC_N8N_WEBHOOK_URL

Value (right box):
https://pakfawad.app.n8n.cloud/webhook/ee6a5882-b7a0-4f8a-9f38-b86aec1ec9e3
```
Click **"Add"**

#### Variable 2:
```
Name (left box):
NEXT_PUBLIC_N8N_INSTANCE_URL

Value (right box):
https://pakfawad.app.n8n.cloud
```
Click **"Add"**

#### Variable 3:
```
Name (left box):
GOOGLE_SHEET_ID

Value (right box):
1NSTsnCxlUqeyj_l873BYOLAYOeVz1xjG-F6s5H5uE64
```
Click **"Add"**

### ✅ You should now see 3 environment variables listed

---

## Step 5: Deploy

1. Scroll down
2. Click the big blue **"Deploy"** button
3. Wait 2-3 minutes (you'll see a build log)
4. When done, you'll see: 🎉 "Congratulations!"

---

## Step 6: Visit Your Live Site

1. Click **"Visit"** or **"Go to Dashboard"**
2. Your live URL will be something like:
   - `https://ai-lead-qualification-system.vercel.app`
   - or `https://ai-lead-qualification-system-xxx.vercel.app`

---

## Step 7: Test Your Live Site

1. Open your live URL
2. Fill in the form with test data:
   ```
   Full Name: Sarah Johnson
   Email: sarah@hubspot.com
   Company Name: HubSpot
   Phone: +1-617-555-0100
   Message: Testing live deployment
   ```
3. Click "Submit Lead"
4. Wait for success message
5. Check your Google Sheet for the new row

---

## ✅ Success Checklist

After deployment, verify:
- [ ] Site loads at your Vercel URL
- [ ] Form is visible and looks good
- [ ] Form submission works
- [ ] Success message appears
- [ ] Data appears in Google Sheet
- [ ] No errors in browser console (F12)

---

## 🔄 Auto-Deployment is Now Active

From now on:
- Every time you push to GitHub `main` branch
- Vercel automatically rebuilds and deploys
- Takes ~2 minutes
- No manual action needed

---

## 📱 Test on Mobile

1. Open your Vercel URL on your phone
2. Test the form
3. Verify responsive design works

---

## 🎯 Your Project URLs

After deployment, save these:

- **Live Site**: `https://[your-project].vercel.app`
- **GitHub**: https://github.com/muhammadfawad538/Ai-Lead-Qualification-System
- **n8n**: https://pakfawad.app.n8n.cloud/
- **Google Sheet**: https://docs.google.com/spreadsheets/d/1NSTsnCxlUqeyj_l873BYOLAYOeVz1xjG-F6s5H5uE64/edit

---

## 🆘 Troubleshooting

### Build Failed?
- Check environment variables are correct (no extra spaces)
- Make sure all 3 variables are added
- Check build logs for specific error

### Form Not Working?
- Open browser console (F12)
- Check for errors
- Verify webhook URL is correct
- Make sure n8n workflow is activated

### 404 Error?
- Make sure you're at the root URL (not /form or /api)
- Clear browser cache
- Try incognito mode

---

## 🎉 You're Done!

Once deployed and tested, you have:
- ✅ Live production website
- ✅ Working lead enrichment system
- ✅ Auto-deployment from GitHub
- ✅ Portfolio-ready project

---

**Time to deploy**: ~5 minutes
**Difficulty**: Easy (just copy-paste)

**Start here**: https://vercel.com/new

---

**Let me know your live URL once it's deployed!** 🚀
