from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API_KEY = "b6cd087ea945c372ac4a72789b9a8b41"  # OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"
#http://api.openweathermap.org/data/2.5/weather?q=London&appid=b6cd087ea945c372ac4a72789b9a8b41
def deg_to_compass(num):
    val = int((num / 22.5) + 0.5)
    directions = ["N","NNE","NE","ENE","E","ESE","SE","SSE",
                  "S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return directions[(val % 16)]

def aqi_description(aqi):
    return {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}.get(aqi, "Unknown")

def get_current_weather(city=None, lat=None, lon=None):
    if city:
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    elif lat and lon:
        url = f"{BASE_URL}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    else:
        return None

    response = requests.get(url).json()
    print(response)  # Debugging line to check the API response
    if response.get("cod") != 200:
        return None

    timezone_offset = response["timezone"]
    local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)
    sunrise = datetime.utcfromtimestamp(response["sys"]["sunrise"] + timezone_offset)
    sunset = datetime.utcfromtimestamp(response["sys"]["sunset"] + timezone_offset)

    lat = response["coord"]["lat"]
    lon = response["coord"]["lon"]
    wind_deg = response["wind"].get("deg", 0)
    weather_desc = response["weather"][0]["main"].lower()

    data = {
        "city": response["name"],
        "country": response["sys"]["country"],
        "temperature": response["main"]["temp"],
        "feels_like": response["main"]["feels_like"],
        "temp_min": response["main"]["temp_min"],
        "temp_max": response["main"]["temp_max"],
        "humidity": response["main"]["humidity"],
        "pressure": response["main"]["pressure"],
        "visibility": round(response.get("visibility", 0)/1000, 2),  # km
        "wind_speed": response["wind"]["speed"],
        "wind_dir": deg_to_compass(wind_deg),
        "description": response["weather"][0]["description"].title(),
        "icon": response["weather"][0]["icon"],
        "local_time": local_time.strftime("%Y-%m-%d %H:%M:%S"),
        "sunrise": sunrise.strftime("%H:%M"),
        "sunset": sunset.strftime("%H:%M"),
        "sunrise_countdown": str(sunrise - local_time).split('.')[0],
        "sunset_countdown": str(sunset - local_time).split('.')[0],
        "lat": lat,
        "lon": lon,
        "weather_main": weather_desc
    }

    # Air Pollution / AQI
    air_url = f"{BASE_URL}air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    air_res = requests.get(air_url).json()
    if "list" in air_res and len(air_res["list"]) > 0:
        air = air_res["list"][0]
        data["aqi"] = air["main"]["aqi"]
        data["aqi_desc"] = aqi_description(air["main"]["aqi"])
        data["pm2_5"] = air["components"]["pm2_5"]
        data["pm10"] = air["components"]["pm10"]
        data["o3"] = air["components"]["o3"]
    else:
        data["aqi"] = data["aqi_desc"] = data["pm2_5"] = data["pm10"] = data["o3"] = None

    # One Call API for UV index and dew point
    onecall_url = f"{BASE_URL}onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}&units=metric"
    onecall_res = requests.get(onecall_url).json()
    data["dew_point"] = onecall_res.get("current", {}).get("dew_point")

    return data

def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != "200":
        return None

    forecast_data = []
    for item in response["list"]:
        forecast_data.append({
            "time": datetime.utcfromtimestamp(item["dt"]).strftime('%d %b %H:%M'),
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "description": item["weather"][0]["description"].title(),
            "icon": item["weather"][0]["icon"]
        })
    return forecast_data

@app.route("/", methods=["GET", "POST"])
def index():
    weather, forecast = None, None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        lat = request.form.get("lat")
        lon = request.form.get("lon")

        weather = get_current_weather(city=city, lat=lat, lon=lon)
        if weather:
            if city:  # only fetch forecast if city search
                forecast = get_forecast(city)
        else:
            error = f"City not found or invalid coordinates!"

    return render_template("dashboard.html", weather=weather, forecast=forecast, error=error)

if __name__ == "__main__":
    app.run(debug=True)
