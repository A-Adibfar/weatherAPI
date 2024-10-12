import redis 
import requests



r = redis.Redis(host='localhost', port=6379, decode_responses=True)

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/san%20diego?unitGroup=metric&key=YOUR_API_KEY&contentType=json'

req = requests.get(url)
