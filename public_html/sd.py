from datetime import datetime
import requests 
import json 

def wishNewMonth()->bool:
    while not False:
        time = datetime.now()
        if time.hour==21:
            print('Happy New Month')
            return True
# wishNewMonth()


d = requests.get('https://dev-app-weu-opsback.azurewebsites.net/api/Bot/domain-logs')

df = d.json()['result']
# with open("persocn.json", "w") as fp:
#     json.dump(df, fp) 
n =0
for i in df:
    if i['messageCount'] == "100":
      n+=1
  
print(n)
