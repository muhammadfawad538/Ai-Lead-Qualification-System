#!/usr/bin/env python3
"""
n8n API Client - Direct API interaction with n8n instance
Bypasses MCP OAuth issues by using the Bearer token directly
"""

import requests
import json
import sys
from typing import Dict, List, Optional

class N8nClient:
    def __init__(self, base_url: str, api_token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }

    def list_workflows(self) -> List[Dict]:
        """List all workflows in the n8n instance"""
        response = requests.get(
            f'{self.base_url}/api/v1/workflows',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json().get('data', [])

    def get_workflow(self, workflow_id: str) -> Dict:
        """Get a specific workflow by ID"""
        response = requests.get(
            f'{self.base_url}/api/v1/workflows/{workflow_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_workflow(self, workflow_data: Dict) -> Dict:
        """Create a new workflow"""
        response = requests.post(
            f'{self.base_url}/api/v1/workflows',
            headers=self.headers,
            json=workflow_data
        )
        response.raise_for_status()
        return response.json()

    def update_workflow(self, workflow_id: str, workflow_data: Dict) -> Dict:
        """Update an existing workflow"""
        response = requests.put(
            f'{self.base_url}/api/v1/workflows/{workflow_id}',
            headers=self.headers,
            json=workflow_data
        )
        response.raise_for_status()
        return response.json()

    def delete_workflow(self, workflow_id: str) -> bool:
        """Delete a workflow"""
        response = requests.delete(
            f'{self.base_url}/api/v1/workflows/{workflow_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return True

    def activate_workflow(self, workflow_id: str) -> Dict:
        """Activate a workflow"""
        response = requests.patch(
            f'{self.base_url}/api/v1/workflows/{workflow_id}',
            headers=self.headers,
            json={'active': True}
        )
        response.raise_for_status()
        return response.json()

    def deactivate_workflow(self, workflow_id: str) -> Dict:
        """Deactivate a workflow"""
        response = requests.patch(
            f'{self.base_url}/api/v1/workflows/{workflow_id}',
            headers=self.headers,
            json={'active': False}
        )
        response.raise_for_status()
        return response.json()

if __name__ == '__main__':
    # Load config from .env
    import os
    from dotenv import load_dotenv

    load_dotenv()

    base_url = os.getenv('N8N_BASE_URL')
    # Extract token from .mcp.json
    with open('.mcp.json', 'r') as f:
        mcp_config = json.load(f)
        token = mcp_config['mcpServers']['n8n-mcp']['headers']['Authorization'].replace('Bearer ', '')

    client = N8nClient(base_url, token)

    # Example: List workflows
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        workflows = client.list_workflows()
        print(json.dumps(workflows, indent=2))
    else:
        print("Usage: python n8n_api_client.py [list]")
