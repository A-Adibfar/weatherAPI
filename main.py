import redis 
import requests
import json 


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

try:
    data = response.json()
except ValueError:
    print("Response content is not valid JSON")