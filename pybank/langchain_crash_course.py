from dotenv import load_dotenv
import os
load_dotenv()
import requests
from langchain.agents import create_agent 
from langchian.tools import tool 


@tool("get_current_weather",description="Get the current weather in a given location",return_direct=False)
def get_current_weather(location):
    # Make a request to the OpenWeatherMap API
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}")
    data = response.json()
    # Extract the temperature and weather description from the response
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    # Return the temperature and weather description as a string
    return f"The current weather in {location} is {temperature} degrees with {weather_description}"



