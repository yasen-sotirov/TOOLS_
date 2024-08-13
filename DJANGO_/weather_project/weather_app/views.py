import datetime
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    API_KEY = '50bdc27d48eceb79c3e752c5ff529831'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

    if request.method == "POST":
        city1 = request.POSTS['city1']
        city2 = request.get('city2', None)


    else:   # get
        return render(request, 'weather_app/index.html')    
    



def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key))
    lat, lon = response['coord']['lat'], response['coord']['lon']

    forecast_response = requests.get(forecast_url.format(lat, lon, api_key))

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    daily_forecasts = []
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
            'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
            'description': daily_data['weather'][0]['description'],
            'icon': daily_data['weather'][0]['icon'],
        })


# https://youtu.be/lyeK0aE_qRg?t=1384