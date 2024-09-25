import os
from dotenv import load_dotenv
from loguru import logger
import requests
load_dotenv()

class WeatherApiWrapper:
    "weather api wrapper class"
    def __init__(self, api_key:str = None):
        if api_key is None:
            api_key = os.getenv("WEATHER_API_KEY")
            if api_key is None:
                raise ValueError("API key not provided")
        self.api_key = api_key
        self.base_url = "https://api.tomorrow.io/v4"
    
    def get_weather_location(self, lat:float, lon:float):
        "get weather data for a location"
        url = f"{self.base_url}/weather/realtime?apikey={self.api_key}&location={lat},{lon}"
        headers = {
            "Accept": "application/json"
        }
        result  = requests.get(url,headers=headers)
        
        if result.status_code != 200:
            return Exception("Error fetching weather data")
            logger.error(f"Error fetching weather data {result.text}")
        logger.info(f"weather data fetched real time")
        return result.json()
        