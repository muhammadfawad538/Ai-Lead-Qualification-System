import axios from 'axios'

const N8N_WEBHOOK_URL = process.env.NEXT_PUBLIC_N8N_WEBHOOK_URL || 'https://pakfawad.app.n8n.cloud/webhook/lead-enrichment-form'
const N8N_INSTANCE_URL = process.env.NEXT_PUBLIC_N8N_INSTANCE_URL || 'https://pakfawad.app.n8n.cloud'

export interface SubmitLeadParams {
  fullName: string
  email: string
  company: string
  phone?: string
  message?: string
}

export async function submitLead(data: SubmitLeadParams) {
  try {
    const response = await axios.post(N8N_WEBHOOK_URL, {
      'Full Name': data.fullName,
      'Email': data.email,
      'Company Name': data.company,
      'Phone': data.phone || '',
      'Message': data.message || '',
    }, {
      headers: {
        'Content-Type': 'application/json',
      },
      timeout: 60000, // 60 second timeout
    })

    return {
      success: true,
      data: response.data,
    }
  } catch (error) {
    console.error('Error submitting lead to n8n:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
    }
  }
}

export async function getWorkflowStatus(workflowId: string) {
  // This would require n8n API access
  // For now, return mock data
  return {
    status: 'active',
    lastRun: new Date().toISOString(),
  }
}
