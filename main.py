import requests
import datetime

NUTRITION_API_KEY = "nix_live_p0oh5YPqqpOCpoMAUgWfUUEsRwGSeLZU"
NUTRITION_APP_ID = "app_38c8f5abe18d410b9b5d8595"

SHEETDB_API_KEY = "ecq7qyclkidof"
SHEETDB_ENDPOINT = "https://sheetdb.io/api/v1/ecq7qyclkidof"

##______________________NUTRITION LLM____________________________##

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

user_input = input("What exercise did you do?")

header = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}
parameter = {
    "query" : user_input
}

response = requests.post(url=url, json=parameter, headers=header)
print(response.json())

date = datetime.date.today()
today_formatted = date.strftime("%d/%m/%Y")
print(today_formatted)

now = datetime.datetime.now()
time_formatted = now.strftime("%H:%M:%S")
print(time_formatted)

exercise = response.json()["exercises"][0]["name"]
print(exercise)

duration = response.json()["exercises"][0]["duration_min"]
print(duration)

calories = response.json()["exercises"][0]["nf_calories"]
print(calories)

##_____________________POST TO GOOOGLE SHEET USING DBSHEET_______________##
data_parameter = {
    "data" : {
        "Date" : today_formatted,
        "Time" : time_formatted,
        "Exercise" : exercise,
        "Duration" : duration,
        "Calories" : calories,
    }
}

data_header = {
    "Content-Type": "application/json"
}
new_data = requests.post(url=SHEETDB_ENDPOINT, json=data_parameter, headers=data_header)
print(new_data.text)


