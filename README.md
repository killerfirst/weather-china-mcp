# 🌤 Weather China MCP Server

<p align="center">
  <samp>点击切换语言 · <b>Click a language to switch</b></samp>
</p>

<details open>
<summary>🇺🇸 <b>English</b></summary>

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
└── README.md
```

## 🔒 Security

- `.env` is listed in `.gitignore` — never commit your API credentials
- `.env.example` provides a template for others to set up their own credentials
- Both `QWEATHER_API_KEY` and `QWEATHER_API_HOST` are read from environment variables, not hardcoded

## 📄 License

MIT

</details>

<details>
<summary>🇨🇳 <b>中文</b></summary>

基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 的中国城市天气服务器，提供实时天气和未来 3 天预报，数据来源为[和风天气](https://www.qweather.com) API。

> **项目由来**：本项目是作者学习 MCP 协议的练手之作，灵感来源于 [modelcontextprotocol.io](https://modelcontextprotocol.io) 上的 MCP Server 美国天气教程。那个教程演示了如何构建一个查询美国天气的 MCP 服务器，本项目则是中国天气版本，适配了和风天气 API。

---

## ✨ 功能

- **实时天气** — 温度、体感温度、湿度、风向风速、能见度等
- **3 天预报** — 每日最高/最低温、白天/夜间天气、湿度、风力
- **MCP 原生** — 兼容所有 MCP 客户端（Claude Code、Codex、OpenClaw 等）
- **安全** — API 凭据存放在 `.env` 文件中，不会提交到 Git

## 📋 前置条件

| 条件 | 说明 |
|------|------|
| **Python** | ≥ 3.11 |
| **uv** | Python 包管理器（[安装指南](https://docs.astral.sh/uv/getting-started/installation/)） |
| **和风天气账号** | 免费版 1,000 次/天。在 [console.qweather.com](https://console.qweather.com) 注册 |

注册后：

1. 创建项目 → 获取 **API Key**
2. 进入设置 → 复制你的**专属 API Host**（格式：`xxx.xxx.qweatherapi.com`）

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone <你的仓库地址>
cd weather-china

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的和风天气 API Key 和 API Host

# 3. 安装依赖
uv sync

# 4. 运行服务器（测试用）
uv run weather.py
```

## 🔧 MCP 客户端配置

### Claude Code

在项目根目录的 `.mcp.json` 中添加（或全局配置 `~/.claude/mcp.json`）：

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

重启 Claude Code 或执行 `/mcp reload` 使配置生效。

### Codex (OpenAI)

在 Codex 中打开 Settings → MCP Servers → Add：

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

在 OpenClaw MCP 配置文件中添加：

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

### 其他 MCP 客户端（通用 stdio 方式）

所有支持 stdio 传输的 MCP 客户端：

```json
{
  "mcpServers": {
    "weather-china": {
      "command": "uv",
      "args": ["--directory", "/path/to/weather-china", "run", "weather.py"],
      "env": {
        "QWEATHER_API_KEY": "<你的API-Key>",
        "QWEATHER_API_HOST": "<你的API-Host>"
      }
    }
  }
}
```

> **注意**：如果你的客户端不会继承 Shell 环境变量，请通过 `env` 字段传入 `QWEATHER_API_KEY` 和 `QWEATHER_API_HOST`。使用 `.env` 文件时，服务器会自动加载。

## 🛠 可用工具

### `get_weather` — 实时天气

```
参数：
  city: string — 城市名称，如"北京"、"上海"、"广州"
```

### `get_forecast` — 3天预报

```
参数：
  city: string — 城市名称，如"北京"、"上海"、"广州"
```

## 📁 项目结构

```
weather-china/
├── weather.py          # MCP 服务器主入口
├── main.py             # 占位入口
├── .env.example        # 环境变量模板
├── .env                # 你的凭据（gitignore 已忽略）
├── .gitignore
├── .mcp.json           # Claude Code MCP 配置示例
├── pyproject.toml      # Python 项目元数据与依赖
├── uv.lock             # 依赖锁定文件
└── README.md
```

## 🔒 安全说明

- `.env` 已加入 `.gitignore`，切勿提交 API 凭据
- `.env.example` 提供模板，方便其他开发者配置自己的凭据
- API Key 和 API Host 均通过环境变量读取，不做硬编码

## 📄 License

MIT

</details>
