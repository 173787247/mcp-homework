# MCP 作业说明

本项目包含四个主要 Python 文件，分别实现了美国天气助手、12306 行程规划服务、中国天气查询服务和行程规划助手。

## 文件说明

### 1. weather.py
美国天气助手应用。输入美国城市名，返回示例天气信息。

### 2. mcp_12306.py
12306 行程规划 MCP Server。基于 Flask 框架，模拟查询两地间的高铁车次信息，提供 `/plan` 接口。

### 3. mcp_china_weather.py
中国天气查询 MCP Server。基于 Flask 框架，模拟查询中国城市天气，提供 `/weather` 接口。

### 4. trip_planner.py
行程规划助手应用。可调用 12306 行程规划服务和中国天气服务，综合展示行程和天气信息。

## 运行说明

1. 安装依赖（首次运行需安装 Flask 和 requests）：
   ```bash
   pip install flask requests
   ```

2. 启动 12306 行程规划服务：
   ```bash
   python mcp_12306.py
   ```

3. 启动中国天气查询服务：
   ```bash
   python mcp_china_weather.py
   ```

4. 运行行程规划助手：
   ```bash
   python trip_planner.py
   ```

5. 运行美国天气助手：
   ```bash
   python weather.py
   ```

## 注意事项
- 需先启动两个 MCP Server（mcp_12306.py 和 mcp_china_weather.py），再运行 trip_planner.py。
- 所有服务均为示例，未对接真实 API。

---
如有问题请联系作者。
