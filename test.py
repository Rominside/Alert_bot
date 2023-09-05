import requests

headers = {"Content-type": "json"}
requests.post(url="http://127.0.0.1:5002/topic/alerts",json={"message": "✅ ROMAN ✅ It's just a test"})
