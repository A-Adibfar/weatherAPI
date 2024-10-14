import urllib.request
import sys
import os 
import json
import redis



API_KEY = os.getenv('WEATHER_API_KEY')    

try: 
  ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/san%20diego?unitGroup=metric&key={API_KEY}&contentType=json")
  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)
  
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()


