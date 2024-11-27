from fastapi import APIRouter,Query
from utils.weatherApi import WeatherApiWrapperForTommorowIo,WeatherApiWrapper
from model.pydantic_model import Location
from pydantic import BaseModel
import joblib
router = APIRouter(
    prefix="/weather",
    tags=["weather"],
    responses={404: {"description": "Not found"}},
)
weather = WeatherApiWrapperForTommorowIo()
weather1 = WeatherApiWrapper()
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

@router.get("/location1",)
async def get_weather(
    latitude: float = Query(..., description="Latitude of the location"),
    longitude: float = Query(..., description="Longitude of the location"),
):
    try: 
        weather_data = weather1.get_weather_location(latitude,longitude)
        return weather_data
    except Exception as e:
        return {"error": str(e)}
class WeatherDataRequest(BaseModel):
    X: float
    Y: float
    Slope: float
    Curvature: float
    Aspect: float
    TWI: float
    FA: float
    Drainage: float
    Rainfall: float

@router.post("/predict")
async def post_weather_data(data: WeatherDataRequest):
    try:
        import os

        # Load the model from the ml_model folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)
        model = joblib.load(os.path.join(f"{current_dir}/random_forest_model.pkl"))
        encoder = joblib.load(os.path.join(f"{current_dir}/ordinal_encoder.pkl"))
        # Prepare the data for prediction
        input_data = [[
            data.X, data.Y, data.Slope, data.Curvature, data.Aspect,
            data.TWI, data.FA, data.Drainage, data.Rainfall
        ]]
        
        print("hi")
        prediction = model.predict(input_data)
        print(prediction)
        
        label = encoder.inverse_transform([prediction])[0][0]
        return label
    except Exception as e:
        return {"error": str(e)}