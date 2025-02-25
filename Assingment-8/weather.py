from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import requests
import streamlit as st
load_dotenv()

weather_api_key  =os.getenv("WEATHER_API_KEY")
gemini_api_key =os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini/gemini-2.0-flash-exp",api_key=os.getenv("GEMINI_API_KEY"))


def fetch_weather(city: str) -> str:
    """
    Fetches the current weather for a given city.

    Parameters:
    - city (str): Name of the city to fetch weather for.

    Returns:
    - str: Weather details or error message.
    """
    api_key = weather_api_key  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        # Check if the API returned an error
        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'Unknown error occurred.')}"

        # Extract weather details
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]

        return (
            f"Weather in {city_name}:\n"
            f"- Description: {weather}\n"
            f"- Temperature: {temperature}°C\n"
            f"- Humidity: {humidity}%"
        )
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch weather data. Details: {e}"
    except KeyError:
        return "Error: Unable to parse weather data. Please check the city name."




prompt = """You are a helpful weather assistant that provides accurate, up-to-date weather forecasts and insights. You should:
- Provide current weather conditions based on the user's location or specified city.
- Include details such as temperature, humidity, wind speed, and the chance of precipitation.
- Offer a brief summary of the weather outlook for the day.
- Suggest appropriate attire or precautions based on the forecast (e.g., 'Carry an umbrella' or 'Wear sunscreen').
- Use a friendly, conversational tone, and adapt your responses to the user's needs (e.g., vacation planning, outdoor activities, or driving conditions).
- Be concise but informative, delivering the key weather information quickly.
- Use both Fahrenheit and Celsius if not specified, but default to the user’s preference if they mention it.
- If a user asks about topics that are not weather-related, respond with a message such as: 'I'm sorry, but I can only provide weather information. Please ask me about the weather.' Always maintain a friendly, concise, and informative tone in your responses.
"""


st.title("Weather Assistant")
st.markdown(("""
    - **Enter a City or Country name below to receive the current weather forecast!**  
    - Whether you’re planning your day or a weekend getaway, get up-to-date weather details instantly.  
    🌍🏙️
     """))
   

user_input = st.text_input("City/Country Name", placeholder="e.g., New York, USA or Paris, France 🌆")
if st.button("Get Weather Forecast"):
    if user_input:
        weather_data = fetch_weather(user_input)
        st.write(weather_data)
    else:
        st.warning("Please enter a valid city or country name.")
    
    
    
