# API Setup Guide - Lead Enrichment Pipeline

This guide will walk you through setting up all the free API keys needed for the Lead Enrichment & Qualification workflow.

**Total Setup Time**: ~15 minutes  
**Cost**: $0 (100% free tier)

---

## 1. Google Gemini API (Required)

**What it does**: AI analysis of websites, pain point extraction, personalized email generation  
**Free tier**: Unlimited requests (rate-limited)  
**Setup time**: 2 minutes

### Steps:
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Get API Key"**
4. Click **"Create API key in new project"** (or select existing project)
5. Copy the API key
6. Add to `.env` file:
   ```
   GEMINI_API_KEY=your_key_here
   ```

**Note**: No credit card required!

---

## 2. Google Custom Search API (Required)

**What it does**: Find company websites, search for funding news, discover LinkedIn profiles  
**Free tier**: 100 queries per day  
**Setup time**: 5 minutes

### Steps:

#### Part A: Get API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable the **Custom Search API**:
   - Search for "Custom Search API" in the search bar
   - Click **Enable**
4. Go to **Credentials** → **Create Credentials** → **API Key**
5. Copy the API key
6. Add to `.env`:
   ```
   GOOGLE_SEARCH_API_KEY=your_key_here
   ```

#### Part B: Create Search Engine
1. Go to [Programmable Search Engine](https://programmablesearchengine.google.com/)
2. Click **"Get Started"** or **"Add"**
3. Configure:
   - **Sites to search**: Leave empty or put `*` (search entire web)
   - **Name**: "Lead Enrichment Search"
   - Enable **"Search the entire web"**
4. Click **Create**
5. Copy the **Search Engine ID** (looks like: `a1b2c3d4e5f6g7h8i`)
6. Add to `.env`:
   ```
   GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
   ```

**Important**: The 100 queries/day limit is shared across all uses of this API key.

---

## 3. Wappalyzer API (Optional but Recommended)

**What it does**: Detects tech stack (Mailchimp, HubSpot, Salesforce, etc.)  
**Free tier**: 50 lookups per month  
**Setup time**: 2 minutes

### Steps:
1. Go to [Wappalyzer API](https://www.wappalyzer.com/api/)
2. Click **"Sign up"**
3. Verify your email
4. Go to **API** section in dashboard
5. Copy your API key
6. Add to `.env`:
   ```
   WAPPALYZER_API_KEY=your_key_here
   ```

**Fallback**: If you skip this, the workflow will use web scraping to detect tech stack (less accurate but free).

---

## 4. AbstractAPI Email Validation (Optional)

**What it does**: Validates email addresses  
**Free tier**: 100 validations per month  
**Setup time**: 2 minutes

### Steps:
1. Go to [AbstractAPI Email Validation](https://www.abstractapi.com/api/email-verification-validation-api)
2. Click **"Get Started Free"**
3. Sign up (no credit card required)
4. Copy your API key from dashboard
5. Add to `.env`:
   ```
   ABSTRACTAPI_KEY=your_key_here
   ```

**Fallback**: If you skip this, the workflow will use regex + DNS MX record validation (free but less thorough).

---

## 5. Google Sheets Setup (Required)

**What it does**: Stores all lead data  
**Setup time**: 3 minutes

### Steps:

#### Part A: Create Spreadsheet
1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it: **"Lead Enrichment Database"**
4. Add column headers (Row 1):
   ```
   Timestamp | Name | Email | Company | Domain | Website | Industry | Company Size | Tech Stack | Lead Score | Status | Generated Email | Archive Reason | Raw Data
   ```
5. Copy the Sheet ID from URL:
   - URL: `https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit`
6. Add to `.env`:
   ```
   GOOGLE_SHEET_ID=your_sheet_id_here
   ```

#### Part B: Configure n8n OAuth
1. In n8n, go to **Credentials** → **Add Credential**
2. Select **Google Sheets OAuth2 API**
3. Follow the OAuth flow to connect your Google account
4. Grant permissions to read/write sheets

**Note**: You'll do this step when importing the workflow into n8n.

---

## 6. Workflow Configuration

Edit these values in `.env` to customize the generated emails:

```bash
# Your product/service value proposition
VALUE_PROPOSITION="We help SaaS companies automate their sales process and increase conversion rates by 40%"

# Your company name
COMPANY_NAME="Your Company Name"

# Contact email
CONTACT_EMAIL="sales@yourcompany.com"
```

---

## Summary Checklist

- [ ] Google Gemini API key added to `.env`
- [ ] Google Custom Search API key added to `.env`
- [ ] Google Search Engine ID added to `.env`
- [ ] (Optional) Wappalyzer API key added to `.env`
- [ ] (Optional) AbstractAPI key added to `.env`
- [ ] Google Sheet created with proper columns
- [ ] Google Sheet ID added to `.env`
- [ ] Value proposition and company info updated in `.env`
- [ ] Google Sheets OAuth configured in n8n

---

## Rate Limits Summary

| Service | Free Tier Limit | What Happens When Exceeded |
|---------|----------------|---------------------------|
| Gemini API | Unlimited (rate-limited) | Temporary slowdown, no hard limit |
| Google Custom Search | 100/day | Workflow will fail, resume next day |
| Wappalyzer | 50/month | Falls back to web scraping |
| AbstractAPI | 100/month | Falls back to regex validation |

**Recommendation**: Process leads in batches to stay within limits. With these limits, you can process ~50 leads per day completely free.

---

## Troubleshooting

### "API key invalid" error
- Double-check you copied the entire key (no spaces)
- Make sure the API is enabled in Google Cloud Console
- Wait 1-2 minutes after creating the key

### "Quota exceeded" error
- Check your daily/monthly limits
- Wait until the quota resets (daily at midnight PT)
- Consider using fallback methods (web scraping instead of Wappalyzer)

### Google Sheets not updating
- Verify OAuth is properly configured in n8n
- Check that the Sheet ID is correct
- Make sure the sheet has the correct column headers

---

## Next Steps

Once you have all API keys configured:
1. Copy `.env.example` to `.env`
2. Fill in your actual API keys
3. Import the workflow JSON into n8n
4. Test with a sample lead

**Ready to build the workflow?** See `workflows/lead_enrichment_sop.md` for usage instructions.
