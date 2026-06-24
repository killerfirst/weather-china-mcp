# 🌤 Weather China MCP Server

<p align="center">
  <a href="README.zh.md">🇨🇳 中文</a> &nbsp;|&nbsp; <b>🇺🇸 English</b>
</p>

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that provides real-time weather and 3-day forecast for Chinese cities, powered by [QWeather (和风天气)](https://www.qweather.com) API.

> **Inspiration**: This project is a learning exercise by the author, inspired by the [MCP server weather tutorial](https://modelcontextprotocol.io) on modelcontextprotocol.io — which demonstrated building a US weather MCP server. This is the Chinese weather counterpart, adapted for the QWeather API.

---

## ✨ Features

- **Real-time weather** — temperature, feels-like, humidity, wind, visibility, and more
- **3-day forecast** — daily high/low, day/night weather, humidity, wind
- **MCP-native** — works with any MCP-compatible client (Claude Code, Codex, OpenClaw, etc.)
- **Secure** — API credentials stored in `.env`, never committed to Git

## 📋 Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Python** | ≥ 3.11 |
| **uv** | Python package manager ([install](https://docs.astral.sh/uv/getting-started/installation/)) |
| **QWeather Account** | Free tier: 1,000 calls/day. Register at [console.qweather.com](https://console.qweather.com) |

After registering on QWeather Console:

1. Create a project → get your **API Key**
2. Go to Settings → copy your **dedicated API Host** (format: `xxx.xxx.qweatherapi.com`)

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd weather-china

# 2. Set up environment variables
cp .env.example .env
# Edit .env and fill in your QWeather API Key & API Host

# 3. Install dependencies
uv sync

# 4. Run the server (for testing)
uv run weather.py
```

## 🔧 MCP Client Configuration

### Claude Code

Add to `.mcp.json` in your project root (or `~/.claude/mcp.json` for global):

```json
{
  "mcpServers": {
    "weather-china": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/weather-china",
        "run",
        "weather.py"
      ]
    }
  }
}
```

Restart Claude Code or run `/mcp reload` to pick up the change.

### Codex (OpenAI)

In Codex, open Settings → MCP Servers → Add:

```json
{
  "mcpServers": {
    "weather-china": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/weather-china",
        "run",
        "weather.py"
      ]
    }
  }
}
```

### OpenClaw

Add to your OpenClaw MCP configuration file:

```yaml
mcp_servers:
  weather-china:
    command: uv
    args:
      - --directory
      - /path/to/weather-china
      - run
      - weather.py
```

### Other MCP Clients (Generic stdio)

Any MCP client that supports stdio transport:

```json
{
  "mcpServers": {
    "weather-china": {
      "command": "uv",
      "args": ["--directory", "/path/to/weather-china", "run", "weather.py"],
      "env": {
        "QWEATHER_API_KEY": "<your-api-key>",
        "QWEATHER_API_HOST": "<your-api-host>"
      }
    }
  }
}
```

> **Note**: If your client doesn't inherit shell environment variables, pass `QWEATHER_API_KEY` and `QWEATHER_API_HOST` via the `env` field as shown above. When using `.env` file, the server loads them automatically.

## 🛠 Available Tools

### `get_weather`

Get real-time weather for a Chinese city.

```
Parameters:
  city: string — City name (e.g., "北京", "上海", "广州")
```

### `get_forecast`

Get 3-day weather forecast for a Chinese city.

```
Parameters:
  city: string — City name (e.g., "北京", "上海", "广州")
```

## 📁 Project Structure

```
weather-china/
├── weather.py          # MCP server — main entry point
├── main.py             # Placeholder entry
├── .env.example        # Environment variable template
├── .env                # Your credentials (gitignored)
├── .gitignore
├── .mcp.json           # Claude Code MCP config (example)
├── pyproject.toml      # Python project metadata & dependencies
├── uv.lock             # Dependency lock file
├── README.md           # English readme
└── README.zh.md        # Chinese readme
```

## 🔒 Security

- `.env` is listed in `.gitignore` — never commit your API credentials
- `.env.example` provides a template for others to set up their own credentials
- Both `QWEATHER_API_KEY` and `QWEATHER_API_HOST` are read from environment variables, not hardcoded

## 📄 License

MIT
