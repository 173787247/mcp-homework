# mcp_12306.py
# 12306 行程规划 MCP Server 示例
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/plan', methods=['POST'])
def plan_trip():
    data = request.json
    from_city = data.get('from')
    to_city = data.get('to')
    # 示例返回，实际应对接 12306 API
    return jsonify({
        'from': from_city,
        'to': to_city,
        'trains': [
            {'train': 'G123', 'depart': '08:00', 'arrive': '12:00'},
            {'train': 'D456', 'depart': '10:00', 'arrive': '14:30'}
        ]
    })

if __name__ == '__main__':
    app.run(port=5001)
