# 🌤 Weather China MCP Server

<p align="center">
  <b>🇨🇳 中文</b> &nbsp;|&nbsp; <a href="README.md">🇺🇸 English</a>
</p>

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
├── README.md           # 英文说明文档
└── README.zh.md        # 中文说明文档
```

## 🔒 安全说明

- `.env` 已加入 `.gitignore`，切勿提交 API 凭据
- `.env.example` 提供模板，方便其他开发者配置自己的凭据
- API Key 和 API Host 均通过环境变量读取，不做硬编码

## 📄 License

MIT
