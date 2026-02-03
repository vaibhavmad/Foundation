from ast import Pass
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)

if response.status_code == 200:
    print("Response ok")
    Pass
else:
    print("Response Error")
    exit(1)

data = response.json()
id = data["id"]
title = data["title"]
print(f"User with ID: {id}, has Title: {title}")