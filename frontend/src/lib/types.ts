export interface LeadFormData {
  fullName: string
  email: string
  company: string
  phone?: string
  message?: string
}

export interface LeadScore {
  score: number
  status: 'Hot Lead' | 'Warm Lead' | 'Cold Lead'
  breakdown: string[]
  archiveReason?: string
}

export interface EnrichedLead {
  name: string
  email: string
  company: string
  domain: string
  website: string
  industry: string
  estimatedEmployees: number
  detectedTech: string[]
  leadScore: number
  status: string
  generatedEmail?: string
  archiveReason?: string
  timestamp: string
}

export interface WorkflowStep {
  number: number
  title: string
  description: string
  icon: string
  status?: 'pending' | 'processing' | 'completed' | 'error'
}
