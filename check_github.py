import urllib.request
import json
try:
    url = "https://api.github.com/repos/YousefEl-Basuony/task_for_orange4"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("Fork:", data.get("fork"))
        if data.get("fork"):
            print("Parent:", data.get("parent", {}).get("full_name"))
except Exception as e:
    print(e)
