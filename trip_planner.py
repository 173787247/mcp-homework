# trip_planner.py
# 行程规划助手应用示例
import requests

def plan_trip(from_city, to_city):
    url = 'http://127.0.0.1:5001/plan'
    data = {'from': from_city, 'to': to_city}
    try:
        resp = requests.post(url, json=data, timeout=5)
        return resp.json()
    except Exception as e:
        return {'error': str(e)}

def get_china_weather(city):
    url = 'http://127.0.0.1:5002/weather'
    data = {'city': city}
    try:
        resp = requests.post(url, json=data, timeout=5)
        return resp.json()
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    from_city = input("请输入出发城市: ")
    to_city = input("请输入到达城市: ")
    trip = plan_trip(from_city, to_city)
    print("行程规划:", trip)
    city = input("请输入要查询天气的中国城市: ")
    weather = get_china_weather(city)
    print("天气信息:", weather)
