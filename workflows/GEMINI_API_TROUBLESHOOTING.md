# Gemini API High Demand - Troubleshooting Guide

## Issue
```
Service unavailable - try again later or consider setting this node to retry automatically
(This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.)
```

---

## Quick Fix: Enable Auto-Retry in n8n

### For Both Gemini Nodes:

1. **"AI Website Analysis (Gemini)"** node
2. **"Generate Personalized Email"** node

### Steps to Enable Retry:

1. Click on the node
2. Click **"Settings"** tab (gear icon)
3. Scroll to **"Retry On Fail"** section
4. Enable **"Retry On Fail"**
5. Configure:
   - **Max Tries**: `3`
   - **Wait Between Tries (ms)**: `5000` (5 seconds)
6. Click **"Save"**

---

## Alternative: Use Gemini 1.5 Flash (More Stable)

If Gemini 2.5 Flash keeps failing, switch to Gemini 1.5 Flash:

### Update URL in Both Nodes:

**Current URL:**
```
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent
```

**Change to:**
```
https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent
```

### How to Change:

1. Click on **"AI Website Analysis (Gemini)"** node
2. Find the **URL** field
3. Change `gemini-2.5-flash` to `gemini-1.5-flash`
4. Save
5. Repeat for **"Generate Personalized Email"** node

---

## Alternative: Add Delay Between Requests

Add a **Wait** node before each Gemini call:

1. Click **"+"** between nodes
2. Add **"Wait"** node
3. Set **"Amount"**: `2` seconds
4. This reduces API rate limiting

---

## Test Again

After enabling retry or switching models:

1. **Save the workflow**
2. **Test with n8n form**: https://pakfawad.app.n8n.cloud/form/ee6a5882-b7a0-4f8a-9f38-b86aec1ec9e3
3. **Wait 30-40 seconds** for processing
4. **Check Google Sheet** for results

---

## Expected Behavior

With retry enabled:
- First attempt might fail
- n8n automatically retries after 5 seconds
- Usually succeeds on 2nd or 3rd attempt
- Total time: 40-60 seconds instead of 30-40 seconds

---

## If Still Failing

**Option 1: Wait 10-15 minutes**
- Gemini API demand is temporary
- Try again later

**Option 2: Use Gemini 1.5 Flash**
- More stable, slightly less capable
- Still excellent for this use case

**Option 3: Test without AI (temporary)**
- Disable the Gemini nodes temporarily
- Test the rest of the workflow
- Re-enable when API is available

---

## Current Status

- **Time**: 2026-04-17 06:40 UTC
- **Issue**: Gemini 2.5 Flash high demand
- **Recommendation**: Enable retry OR switch to Gemini 1.5 Flash

---

**Enable retry on both Gemini nodes and test again!** 🔄
