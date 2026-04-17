'use client'

import { useState } from 'react'
import axios from 'axios'

interface FormData {
  fullName: string
  email: string
  company: string
  phone: string
  message: string
}

interface LeadResult {
  status: 'success' | 'error' | 'processing'
  score?: number
  leadStatus?: string
  generatedEmail?: string
  archiveReason?: string
}

export default function LeadForm() {
  const [formData, setFormData] = useState<FormData>({
    fullName: '',
    email: '',
    company: '',
    phone: '',
    message: '',
  })
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [result, setResult] = useState<LeadResult | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    setResult({ status: 'processing' })

    try {
      // Submit to n8n webhook
      const webhookUrl = process.env.NEXT_PUBLIC_N8N_WEBHOOK_URL || 'https://pakfawad.app.n8n.cloud/webhook/lead-enrichment-form'

      const response = await axios.post(webhookUrl, {
        'Full Name': formData.fullName,
        'Email': formData.email,
        'Company Name': formData.company,
        'Phone': formData.phone,
        'Message': formData.message,
      })

      // Simulate processing time (n8n workflow takes ~30-40 seconds)
      setTimeout(() => {
        setResult({
          status: 'success',
          score: 75,
          leadStatus: 'Hot Lead',
          generatedEmail: 'Email generated successfully! Check your Google Sheet for details.',
        })
        setIsSubmitting(false)
      }, 3000)

    } catch (error) {
      console.error('Error submitting form:', error)
      setResult({
        status: 'error',
      })
      setIsSubmitting(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-8">
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="fullName" className="block text-sm font-medium text-gray-700">
            Full Name *
          </label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            required
            value={formData.fullName}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-2 border"
            placeholder="John Smith"
          />
        </div>

        <div>
          <label htmlFor="email" className="block text-sm font-medium text-gray-700">
            Business Email *
          </label>
          <input
            type="email"
            id="email"
            name="email"
            required
            value={formData.email}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-2 border"
            placeholder="john@company.com"
          />
        </div>

        <div>
          <label htmlFor="company" className="block text-sm font-medium text-gray-700">
            Company Name *
          </label>
          <input
            type="text"
            id="company"
            name="company"
            required
            value={formData.company}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-2 border"
            placeholder="Acme Corp"
          />
        </div>

        <div>
          <label htmlFor="phone" className="block text-sm font-medium text-gray-700">
            Phone
          </label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-2 border"
            placeholder="+1-555-0100"
          />
        </div>

        <div>
          <label htmlFor="message" className="block text-sm font-medium text-gray-700">
            Message
          </label>
          <textarea
            id="message"
            name="message"
            rows={4}
            value={formData.message}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-2 border"
            placeholder="Tell us about your needs..."
          />
        </div>

        <button
          type="submit"
          disabled={isSubmitting}
          className="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {isSubmitting ? 'Processing...' : 'Submit Lead'}
        </button>
      </form>

      {result && (
        <div className="mt-8">
          {result.status === 'processing' && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-center">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
              <p className="text-blue-800 font-medium">Processing your lead...</p>
              <p className="text-blue-600 text-sm mt-2">This usually takes 30-40 seconds</p>
            </div>
          )}

          {result.status === 'success' && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-green-900 mb-4">Lead Processed Successfully!</h3>
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-gray-700">Lead Score:</span>
                  <span className="text-2xl font-bold text-green-600">{result.score}/100</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-700">Status:</span>
                  <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium">
                    {result.leadStatus}
                  </span>
                </div>
                {result.generatedEmail && (
                  <div className="mt-4 p-4 bg-white rounded border border-green-200">
                    <p className="text-sm text-gray-600">{result.generatedEmail}</p>
                  </div>
                )}
              </div>
            </div>
          )}

          {result.status === 'error' && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold text-red-900 mb-2">Error Processing Lead</h3>
              <p className="text-red-700">Please try again or contact support.</p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
