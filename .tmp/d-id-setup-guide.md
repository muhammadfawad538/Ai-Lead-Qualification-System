# Getting D-ID API Key - Step by Step

## What is D-ID?
D-ID is an AI video generation platform that creates talking head videos from text and images. They offer a **free tier with 20 credits per month** (each video costs ~1-5 credits depending on length).

## Step-by-Step Guide

### 1. Sign Up for D-ID
1. Go to: https://studio.d-id.com/
2. Click **"Sign Up"** or **"Get Started"**
3. Sign up with:
   - Email
   - Google account
   - Or GitHub

### 2. Verify Your Email
- Check your email inbox
- Click the verification link
- Complete your profile setup

### 3. Get Your API Key
1. After login, go to: https://studio.d-id.com/account-settings
2. Click on the **"API"** tab
3. You'll see your **API Key** displayed
4. Click **"Copy"** to copy it
5. **Save it securely** - you'll need it for n8n

### 4. Check Your Credits
- Free tier: **20 credits/month**
- Each 15-second video: ~2-3 credits
- Credits reset monthly

### 5. Test the API (Optional)
You can test in their playground:
1. Go to: https://studio.d-id.com/
2. Try creating a test video
3. This helps you understand how it works

## D-ID API Endpoints

**Create Video:**
```
POST https://api.d-id.com/talks
```

**Check Status:**
```
GET https://api.d-id.com/talks/{talk_id}
```

## What You'll Need for n8n

- **API Key**: From step 3 above
- **Authorization Header**: `Basic {your-api-key}`

## Pricing (if you need more)

- **Free**: 20 credits/month
- **Lite**: $5.90/month - 100 credits
- **Pro**: $29.90/month - 500 credits
- **Advanced**: $195/month - 5000 credits

## Next Steps

Once you have your D-ID API key:
1. Save it in a secure place
2. We'll add it to your n8n workflow
3. Configure the Google Form integration
4. Test the complete flow

---

**Note**: Keep your API key secret. Don't share it publicly or commit it to git repositories.
