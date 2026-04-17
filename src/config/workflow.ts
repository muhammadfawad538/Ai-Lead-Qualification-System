export const workflowConfig = {
  name: 'Lead Enrichment & Qualification Pipeline',
  description: 'Automatically enrich, score, and qualify leads using AI',
  version: '1.0.0',

  // ICP Criteria
  icp: {
    industries: ['SaaS', 'Tech'],
    companySize: {
      min: 50,
      max: 500,
    },
    revenue: {
      min: 5000000,
      max: 50000000,
    },
    techStack: ['Mailchimp', 'ActiveCampaign', 'Salesforce', 'HubSpot'],
  },

  // Scoring weights
  scoring: {
    techStackMatch: 30,
    companySize: 25,
    industry: 20,
    revenue: 15,
    buyingSignals: 10,
  },

  // Lead status thresholds
  thresholds: {
    hot: 70,
    warm: 40,
  },

  // Processing time estimate
  processingTime: {
    average: 35, // seconds
    min: 25,
    max: 45,
  },
}
