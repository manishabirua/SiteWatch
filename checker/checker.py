import requests
import time
from datetime import datetime
import redis

URLS=["https://www.google.com", "https://www.youtube.com", "https://httpbin.org", "https://httpstat.us/503"]
r = redis.Redis (host='localhost', port=6379, decode_responses=True)

def check_url(url):
 headers = {"User-Agents": "Mozilla/5.0"}
 try:
   response = requests.get(url, timeout=5)
   if response.status_code<500:
     return "UP"
   else:
     return "DOWN"
 except requests.exceptions.RequestException:
   return "DOWN"

while True:
 for url in URLS:
   status = check_url(url)
   timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
   r.hset ("sitewatch", url, f"{status} | {timestamp}")
   print (f"[{timestamp}]  {url} -> {status}")
 print ("         (Waiting for 5 minutes)")
 time.sleep(300)
