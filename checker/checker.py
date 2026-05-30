import requests
import time
from datetime import datetime

URLS=["https://www.google.com", "https://www.youtube.com", "https://httpbin.org", "https://httpstat.us/503"]

def check_url(url):
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
   print (f"[{timestamp}]  {url} -> {status}")
 print ("         (Waiting for 5 minutes)")
 time.sleep(300)
