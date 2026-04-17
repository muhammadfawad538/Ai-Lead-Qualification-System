# List n8n Workflows

## Objective
Retrieve and display all workflows from the connected n8n instance.

## Required Inputs
- n8n instance URL (configured in .mcp.json)
- API authentication token (configured in .mcp.json)

## Tools Used
- MCP n8n server tools (via Claude Code)
- `tools/format_workflow_list.py` (for formatting output)

## Steps

1. Use the n8n MCP server to search for workflows
2. Retrieve workflow details including:
   - Workflow ID
   - Workflow name
   - Active/inactive status
   - Last updated date
3. Format the results for easy reading
4. Optionally export to Google Sheets or CSV

## Expected Outputs
- Console output with workflow list
- Optional: CSV file in `.tmp/` directory
- Optional: Google Sheet with workflow inventory

## Edge Cases
- **Rate limiting**: n8n API may have rate limits, handle gracefully
- **Large workflow counts**: Paginate if more than 100 workflows
- **Authentication errors**: Check token validity in .mcp.json
- **Network timeouts**: Retry with exponential backoff

## Learnings
- Document any rate limits discovered
- Note optimal batch sizes for workflow operations
