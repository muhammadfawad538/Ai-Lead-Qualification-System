#!/usr/bin/env python3
"""
Validate n8n workflow SDK code before creation.

Usage:
    python validate_n8n_code.py <code_file>
"""

import sys
from pathlib import Path

def validate_code_structure(code):
    """Basic validation of workflow code structure."""
    errors = []
    warnings = []

    # Check for required imports
    if 'from n8n_sdk' not in code and 'import' not in code:
        warnings.append("No imports found - ensure n8n SDK is imported")

    # Check for workflow export
    if 'export' not in code and 'workflow' not in code.lower():
        errors.append("No workflow export found")

    # Check for basic structure
    if '.addNode' not in code and 'node' not in code.lower():
        warnings.append("No nodes found in workflow")

    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    code_file = Path(sys.argv[1])

    if not code_file.exists():
        print(f"Error: File not found: {code_file}")
        sys.exit(1)

    code = code_file.read_text(encoding='utf-8')

    errors, warnings = validate_code_structure(code)

    if errors:
        print("❌ Validation Errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    if warnings:
        print("⚠️  Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    print("✓ Basic validation passed")
    print("\nNote: Use n8n MCP 'validate_workflow' tool for full validation")

if __name__ == "__main__":
    main()
