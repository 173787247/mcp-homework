# weather.py
# 美国天气助手应用示例
import requests

def get_us_weather(city):
    """
    查询美国城市天气（示例，实际需替换为真实API）
    """
    # 这里用伪数据，实际可用 openweathermap 或 weatherapi
    demo_data = {
        'New York': '晴，25°C',
        'Los Angeles': '多云，28°C',
        'Chicago': '小雨，22°C',
    }
    return demo_data.get(city, '暂未收录该城市天气')

if __name__ == "__main__":
    city = input("请输入美国城市名: ")
    print(f"{city} 天气: {get_us_weather(city)}")
