# Python MCP Server – hello-mcp

NAME: T.G SRAVAN TEJA
ROLL NO: 261FB04042

This is a beginner-friendly implementation of a local **Model Context Protocol (MCP) server** using Python, VS Code and GitHub Copilot Agent mode.

This project demonstrates how to create a Python MCP server, expose Python functions as MCP tools, connect the server to VS Code and invoke the tools through GitHub Copilot.

## 1. Project Overview

The project implements a local MCP server using standard input/output (stdio) transport.

The server exposes two tools:

| Tool | Description | Example |
|---|---|---|
| `get_greeting` | Returns a personalized greeting | `Hello, Students!` |
| `add_numbers` | Adds two integers | `10 + 20 = 30` |

## 2. Architecture

```text
GitHub Copilot (Agent Mode)
           |
           | MCP / stdio
           |
           v
    VS Code MCP Client
           |
           v
    Python MCP Server
        (server.py)
           |
      +----+----+
      |         |
      v         v
 get_greeting  add_numbers
      |         |
      v         v
  Greeting    Sum Result
```

## 3. Technologies Used

- **Programming Language:** Python
- **MCP SDK:** Python MCP SDK
- **Editor:** Visual Studio Code
- **AI Client:** GitHub Copilot Agent mode
- **Communication:** MCP over stdio
- **Environment:** Python Virtual Environment (`.venv`)

## 4. Prerequisites

Ensure the following are installed:

- Windows 10/11 (64-bit)
- Python 3.12 or above (subject to MCP SDK compatibility)
- Visual Studio Code
- GitHub Copilot with Agent mode access
- Internet connection for installing dependencies

Check Python:

```cmd
py --version
py -0p
```

## 5. Project Structure

```text
hello-mcp/
│
├── .vscode/
│   └── mcp.json
│
├── .venv/
│
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

**File descriptions:**

- `server.py` – Contains the MCP server and tool definitions.
- `requirements.txt` – Records Python dependencies.
- `.vscode/mcp.json` – Configures the MCP server in VS Code.
- `.gitignore` – Excludes virtual environments and unnecessary files.
- `.venv/` – Isolated Python environment (not committed to GitHub).

## 6. Installation and Setup

### Step 1: Clone the repository

```cmd
git clone https://github.com/USERNAME/hello-mcp.git
cd hello-mcp
```

### Step 2: Create a virtual environment

```cmd
py -3.12 -m venv .venv
```

Replace `3.12` with an installed and compatible Python version if necessary.

### Step 3: Install dependencies

```cmd
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 4: Verify installation

```cmd
.venv\Scripts\python.exe -m pip show mcp
```

## 7. MCP Server Implementation

The `server.py` file contains the following implementation:

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Hello MCP")


@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run()
```

**Note:** MCP SDK APIs may vary between versions. This implementation uses the API shown in the original project guide. If the import fails, check the installed SDK version and its corresponding API documentation.

## 8. VS Code MCP Configuration

Create `.vscode/mcp.json`:

```json
{
    "servers": {
        "helloMcp": {
            "type": "stdio",
            "command": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
            "args": ["server.py"]
        }
    }
}
```

This configuration tells VS Code how to launch the local Python MCP server using the project's virtual environment.

## 9. Starting the MCP Server

1. Open the project folder in VS Code.
2. Save all project files.
3. Open the Command Palette using `Ctrl + Shift + P`.
4. Search for `MCP: List Servers`.
5. Select `helloMcp`.
6. Start or restart the server.
7. Verify that the server is running and both tools are discovered.

## 10. Testing Through GitHub Copilot

Open Copilot Chat and select Agent mode.

### Test 1: Greeting Tool

Prompt:

```text
Use the get_greeting MCP tool from helloMcp
with the name Students. Show me the result.
```

Expected output:

```text
Hello, Students! Your first MCP tool works.
```

### Test 2: Addition Tool

Prompt:

```text
Use the add_numbers MCP tool from helloMcp
with a = 10 and b = 20. Show me the result.
```

Expected output:

```text
30
```

Ensure Copilot actually invokes the MCP tools rather than simply generating an ordinary chat response.

## 11. Troubleshooting

| Issue | Suggested Check |
|---|---|
| MCP import error | Verify installed SDK version and API compatibility. |
| Python executable not found | Check `.venv\Scripts\python.exe`. |
| Dependency installation failure | Check internet connection and retry pip installation. |
| MCP server not starting | Check Python syntax, JSON configuration and VS Code MCP logs. |
| Copilot not invoking tools | Verify Agent mode, server status and tool permissions. |

## 12. Future Enhancements

This project provides a starting point for exploring MCP server development.

Possible future enhancements:

- Create additional custom MCP tools.
- Integrate tools with databases.
- Connect MCP tools to REST APIs.
- Implement file and project management tools.
- Explore practical automation through GitHub Copilot.
- Build reusable MCP tools for development workflows.

## 13. Learning Outcome

After completing this project, you will understand:

- What an MCP server is.
- How Python functions are exposed as MCP tools.
- How MCP communicates using stdio.
- How VS Code discovers and launches an MCP server.
- How GitHub Copilot Agent mode invokes custom MCP tools.
- How to configure and manage a local MCP development environment.

---

**Project:** hello-mcp  
**Language:** Python  
**Client:** VS Code + GitHub Copilot Agent mode  
**Protocol:** Model Context Protocol (MCP)
