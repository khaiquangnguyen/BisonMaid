# import required modules
import os
import requests
from dotenv import load_dotenv
from Utilities import right_padding, to_monospace

load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather_data_of_city_with_id(id: int) -> str:
    complete_url = base_url + "APPID=" + api_key + "&id=" + str(id) + "&units=metric"
    response = requests.get(complete_url)
    response_data = response.json()
    weather_data_sys = response_data.get('sys', {})
    city_name = response_data.get('name', 'N/A')
    country = weather_data_sys.get('country', 'N/A')
    temp_data = response_data.get('main', {})
    temp = temp_data.get('temp', 'no clue')
    weather_data = response_data.get('weather', [{}])[0]
    weather = weather_data.get('description', 'no clue')
    weather_icon_link = weather_data.get('icon', '')
    weather_icon = f'https://openweathermap.org/img/wn/{weather_icon_link}@2x.png'
    # print following values
    return f'{right_padding(to_monospace(city_name))}   ' \
           f'{right_padding(to_monospace("{:04.1f}".format(temp) + " °C"), 80)} {weather}'
