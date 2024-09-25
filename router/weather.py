from fastapi import APIRouter,Query
from utils.weatherApi import WeatherApiWrapper
from model.pydantic_model import Location
router = APIRouter(
    prefix="/weather",
    tags=["weather"],
    responses={404: {"description": "Not found"}},
)
weather = WeatherApiWrapper()
@router.get("/location",)
async def get_weather(
    latitude: float = Query(..., description="Latitude of the location"),
    longitude: float = Query(..., description="Longitude of the location"),
):
    try: 
        weather_data = weather.get_weather_location(latitude,longitude)
        return weather_data
    except Exception as e:
        return {"error": str(e)}