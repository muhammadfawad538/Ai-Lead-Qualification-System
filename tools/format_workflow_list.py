#!/usr/bin/env python3
"""
Format n8n workflow list data into readable output.

Usage:
    python format_workflow_list.py <input_json> [--output csv|table]
"""

import json
import sys
import csv
from datetime import datetime
from pathlib import Path

def format_as_table(workflows):
    """Format workflows as a text table."""
    if not workflows:
        return "No workflows found."

    # Calculate column widths
    id_width = max(len(str(w.get('id', ''))) for w in workflows)
    name_width = max(len(w.get('name', '')) for w in workflows)
    id_width = max(id_width, len('ID'))
    name_width = max(name_width, len('Name'))

    # Header
    header = f"{'ID':<{id_width}} | {'Name':<{name_width}} | {'Active':<8} | {'Updated'}"
    separator = '-' * len(header)

    lines = [separator, header, separator]

    # Rows
    for w in workflows:
        wf_id = str(w.get('id', 'N/A'))
        name = w.get('name', 'Unnamed')
        active = 'Yes' if w.get('active', False) else 'No'
        updated = w.get('updatedAt', 'Unknown')

        lines.append(f"{wf_id:<{id_width}} | {name:<{name_width}} | {active:<8} | {updated}")

    lines.append(separator)
    lines.append(f"\nTotal workflows: {len(workflows)}")

    return '\n'.join(lines)

def format_as_csv(workflows, output_path=None):
    """Format workflows as CSV."""
    if not output_path:
        output_path = Path('.tmp') / f'workflows_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        if not workflows:
            f.write("No workflows found\n")
            return str(output_path)

        fieldnames = ['id', 'name', 'active', 'updatedAt', 'createdAt']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

        writer.writeheader()
        writer.writerows(workflows)

    return str(output_path)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'table'

    # Read input JSON
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        sys.exit(1)

    # Extract workflows list
    workflows = data if isinstance(data, list) else data.get('workflows', [])

    # Format output
    if output_format == 'csv':
        output_path = format_as_csv(workflows)
        print(f"CSV saved to: {output_path}")
    else:
        print(format_as_table(workflows))

if __name__ == "__main__":
    main()
