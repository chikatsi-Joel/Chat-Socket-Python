import requests

r = requests.get("http://127.0.0.1:5000")
data = r.json()


print(f"There are {data['name']} age : . {data['age']}")