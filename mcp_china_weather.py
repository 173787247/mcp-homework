# mcp_china_weather.py
# 中国天气查询 MCP Server 示例
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.json
    city = data.get('city')
    # 示例返回，实际应对接中国天气API
    demo_data = {
        '北京': '晴，30°C',
        '上海': '多云，28°C',
        '广州': '小雨，27°C',
    }
    return jsonify({
        'city': city,
        'weather': demo_data.get(city, '暂未收录该城市天气')
    })

if __name__ == '__main__':
    app.run(port=5002)
