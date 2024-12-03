import requests
import json
import pandas as pd

def weather(url, params):
    response = requests.get(url, params = params) # fetch data from the API
    if response.status_code == 200:
        print("Data fetched successfully!")
        data = response.json()  # convert the data to JSON response
        print(json.dumps(data, indent=4))  # Make JSON response clearer
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(response.text)  # error message
    # flatten the data so that it can be converted into a DataFrame
    flatten_data = {
        "Longitude": data["coord"]["lon"],
        "Latitude": data["coord"]["lat"],
        "Temperature": data["main"]["temp"],
        "Feels like": data["main"]["feels_like"],
        "Min temp": data["main"]["temp_min"],
        "Max temp": data["main"]["temp_max"],
        "Pressure": data["main"]["pressure"],
        "Humidity": data["main"]["humidity"],
        "Weather main": data["weather"][0]["main"],
        "Weather description": data["weather"][0]["description"],
        "City name": data["name"],
        "Status code": data["cod"]
    }
    # convert the flattened data into a DataFrame for readability
    df = pd.DataFrame([flatten_data])
    print(df)
# Example usage
weather("https://api.openweathermap.org/data/2.5/weather",
        {
    "lat": 41.878113,  # Example: Latitude for Chicago
    "lon": -87.629799, # Example: Longitude for Chicago
    "appid": "6df5fc8020bd1271a99069f27a4b6100",  
    "units": "metric" 
})
