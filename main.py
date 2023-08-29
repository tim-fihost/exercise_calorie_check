import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


APP_ID = "YOUR APP_ID"
NUTRITION_API_KEY = "YOUR KEY"
link = "https://trackapi.nutritionix.com/v2/natural/exercise"

USER = "YOUR USER ID FOR GOOGLE SHEET"
GOOGLE_SHEETY_PASSWORD = "YOUR PASSWORD"
GOOGLE_SHEET_LINK = "LINK TO YOUR PORJECT"

header = {
    "x-app-id" : APP_ID,
    "x-app-key": NUTRITION_API_KEY
}
text = input("Tell me which exercises you did: ")
params = {
     "query":text,
     "gender":"male",
     "weight_kg":float(65),
     "height_cm":float(176),
     "age":21
}
response = requests.post(url=link,json=params,headers=header)
response.raise_for_status()
data = response.json().values()
data = (list(data)[0])[0]

#Day 
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = datetime.now().strftime('%X')

body = {
    "workout" : {
        "date" : today_date,
        "time":today_time,
        "exercise" : data["name"].title(),
        "duration" : data["duration_min"],
        "calories" : data["nf_calories"],
        "id" : data["tag_id"]
    }
        }
basic = HTTPBasicAuth(USER, GOOGLE_SHEETY_PASSWORD)

response = requests.post(url=GOOGLE_SHEET_LINK,
                         json=body,auth=basic)
response.raise_for_status()
print(response.json)
