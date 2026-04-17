# Tools

This directory contains Python scripts for deterministic execution.

## Tool Guidelines

Each tool should:
- Do one thing well
- Load credentials from `.env`
- Accept inputs via command-line arguments
- Return clear success/error messages
- Be testable independently

## Tool Template

```python
#!/usr/bin/env python3
"""
Brief description of what this tool does.
"""

import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Your tool logic here
    pass

if __name__ == "__main__":
    main()
```

## Common Patterns

- **API calls**: Use `requests` library, handle rate limits
- **File operations**: Work with `.tmp/` for intermediates
- **Cloud uploads**: Use appropriate SDK (Google, AWS, etc.)
- **Error handling**: Exit with clear error codes and messages

## Adding New Tools

1. Create a new `.py` file with a descriptive name
2. Add required dependencies to `requirements.txt`
3. Document usage in the tool's docstring
4. Reference the tool in relevant workflows
