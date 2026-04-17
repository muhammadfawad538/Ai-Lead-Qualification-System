# Create n8n Workflow

## Objective
Create a new workflow in n8n from validated SDK code.

## Required Inputs
- Workflow name
- Workflow description
- Valid n8n Workflow SDK code
- Optional: Project ID
- Optional: Folder ID

## Tools Used
- MCP n8n server tools (via Claude Code)
- `tools/validate_n8n_code.py` (for pre-validation)

## Steps

1. **Validate the workflow code**
   - Use `validate_workflow` MCP tool to check for errors
   - Fix any validation issues before proceeding

2. **Get node type definitions**
   - Use `search_nodes` to find required node types
   - Use `get_node_types` to get TypeScript definitions
   - Ensure all nodes are properly configured

3. **Create the workflow**
   - Use `create_workflow_from_code` MCP tool
   - Provide workflow name and description
   - Optionally specify project/folder

4. **Verify creation**
   - Check returned workflow ID
   - Optionally retrieve workflow details to confirm

## Expected Outputs
- New workflow created in n8n
- Workflow ID returned
- Console confirmation message

## Edge Cases
- **Validation failures**: Fix code and retry validation
- **Missing node types**: Search for correct node IDs
- **Project/folder not found**: Use `search_projects` and `search_folders` first
- **Duplicate names**: n8n allows duplicates, but consider checking first

## Learnings
- Always validate before creating
- Get SDK reference documentation first with `get_sdk_reference`
- Node type definitions are critical for correct parameter names
