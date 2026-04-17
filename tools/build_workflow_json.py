#!/usr/bin/env python3
"""
Build n8n Workflow JSON
Creates valid n8n workflow JSON files that can be imported into n8n
"""

import json
import uuid
from typing import Dict, List, Optional

class N8nWorkflowBuilder:
    """Builder for creating n8n workflow JSON structures"""

    def __init__(self, name: str, description: str = ""):
        self.workflow = {
            "name": name,
            "nodes": [],
            "connections": {},
            "active": False,
            "settings": {
                "executionOrder": "v1"
            },
            "versionId": str(uuid.uuid4())
        }
        if description:
            self.workflow["meta"] = {"description": description}

    def add_webhook_trigger(self, path: str, method: str = "POST", position: tuple = (250, 300)) -> str:
        """Add a webhook trigger node"""
        node_name = "Webhook"
        node = {
            "parameters": {
                "path": path,
                "httpMethod": method,
                "responseMode": "onReceived",
                "options": {}
            },
            "id": str(uuid.uuid4()),
            "name": node_name,
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 2,
            "position": list(position),
            "webhookId": str(uuid.uuid4())
        }
        self.workflow["nodes"].append(node)
        return node_name

    def add_code_node(self, javascript_code: str, name: str = "Code", position: tuple = (450, 300)) -> str:
        """Add a Code (JavaScript) node"""
        node = {
            "parameters": {
                "jsCode": javascript_code
            },
            "id": str(uuid.uuid4()),
            "name": name,
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": list(position)
        }
        self.workflow["nodes"].append(node)
        return name

    def connect_nodes(self, from_node: str, to_node: str):
        """Connect two nodes together"""
        if from_node not in self.workflow["connections"]:
            self.workflow["connections"][from_node] = {"main": [[]]}

        self.workflow["connections"][from_node]["main"][0].append({
            "node": to_node,
            "type": "main",
            "index": 0
        })

    def save(self, filepath: str):
        """Save workflow to JSON file"""
        with open(filepath, 'w') as f:
            json.dumps(self.workflow, f, indent=2)
        return filepath


if __name__ == "__main__":
    builder = N8nWorkflowBuilder("Test Workflow", "A simple test")
    webhook = builder.add_webhook_trigger("/test")
    code = builder.add_code_node("return [{json: {message: 'Hello'}}];")
    builder.connect_nodes(webhook, code)
    builder.save(".tmp/test_workflow.json")
