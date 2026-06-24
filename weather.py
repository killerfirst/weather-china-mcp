from typing import Any 
import os  # Python内置操作系统文件/路径工具库
from dotenv import load_dotenv
load_dotenv()  # ← 这一行会去读取 .env 文件，把内容注入到环境变量中

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCO server 初始化mcp服务器
mcp = FastMCP("weather-china")

# =============================================
# 从环境变量读取API Key
# =============================================
WEATHER_API_KEY = os.getenv("QWEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise RuntimeError(
        "缺少QWEATHER_API_KEY 环境变量 \n"
        "请在项目根目录创建 .env文件,并添加:\n"
        "QWEATHER_API_KEY=你的和风天气API_KEY"
    )
QWEATHER_API_HOST = os.getenv("QWEATHER_API_HOST")
if not QWEATHER_API_HOST:
    raise RuntimeError(
        "缺少QWEATHER_API_HOST 环境变量 \n"
        "请在项目根目录创建 .env文件,并添加:\n"
        "QWEATHER_API_HOST=你的和风天气API域名"
    )
WEATHER_API_BASE = f"https://{QWEATHER_API_HOST}/v7"
GEO_API_BASE = f"https://{QWEATHER_API_HOST}/geo/v2"
USER_AGENT="weather-china-app/1.0"

async def make_request(url:str)->dict[str,Any]|None:
    """通用的异步请求函数,带错误处理 Make a request to the API with proper error handling."""
    async with httpx.AsyncClient() as client:
        try:
            response=await client.get(url,timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
@mcp.tool()
async def get_weather(city:str)->str:
    """获取中国城市的实时天气 Get weather for chinese city
    
    Args:
    city:城市名称,例如"北京","上海","广州" 
    """
    # 第一步：根据城市名查询城市 ID  First get the city ID
    geo_url=f"{GEO_API_BASE}/city/lookup?location={city}&key={WEATHER_API_KEY}"
    geo_data=await make_request(geo_url)

    if not geo_data or geo_data.get("code")!="200" or not geo_data.get("location"):
        return f"未找到城市:{city}"
    
    location_id=geo_data["location"][0]["id"]
    city_name=geo_data["location"][0]["name"]

    # 第二步，获取实时天气  second to get the weather of the city
    weather_url=f"{WEATHER_API_BASE}/weather/now?location={location_id}&key={WEATHER_API_KEY}"
    weather_data=await make_request(weather_url)

    if not weather_data or weather_data.get("code")!="200":
        return f"无法获取{city_name}的天气数据"
    
    now = weather_data["now"]
    return f"""
📍 {city_name} 实时天气

🌡 温度：{now["temp"]}°C
体感温度：{now["feelsLike"]}°C
☁ 天气：{now["text"]}
💧 湿度：{now["humidity"]}%
🌬 风向：{now["windDir"]}（{now["windScale"]}级）
💨 风速：{now["windSpeed"]} km/h
👁 能见度：{now["vis"]} km
🕐 更新时间：{now["obsTime"]}
"""

@mcp.tool()
async def get_forecast(city:str)->str:
    """获取中国城市未来3天的天气预报

    Args:
        city: 城市名称，例如"北京"、"上海"、"广州"
    """
    # 第一步：查城市 ID
    geo_url = f"{GEO_API_BASE}/city/lookup?location={city}&key={WEATHER_API_KEY}"
    geo_data = await make_request(geo_url)

    if not geo_data or geo_data.get("code") != "200" or not geo_data.get("location"):
        return f"未找到城市：{city}"

    location_id = geo_data["location"][0]["id"]
    city_name = geo_data["location"][0]["name"]

    # 第二步：获取未来3天预报
    forecast_url = f"{WEATHER_API_BASE}/weather/3d?location={location_id}&key={WEATHER_API_KEY}"
    forecast_data = await make_request(forecast_url)

    if not forecast_data or forecast_data.get("code") != "200":
        return f"无法获取 {city_name} 的预报数据"

    forecasts = []
    for day in forecast_data["daily"]:
        forecast = f"""
📅 {day["fxDate"]}
🌡 {day["tempMin"]}°C ~ {day["tempMax"]}°C
☁ 白天：{day["textDay"]} / 夜间：{day["textNight"]}
💧 湿度：{day["humidity"]}%
🌬 风向：{day["windDirDay"]}（{day["windScaleDay"]}级）
"""
        forecasts.append(forecast)

    return f"📍 {city_name} 未来3天预报\n" + "\n---\n".join(forecasts)

def main():
    mcp.run(transport="stdio")

if __name__=="__main__":
    main()
