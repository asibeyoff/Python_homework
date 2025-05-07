import requests

def get_weather(city_name):
    API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city_name}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description'].capitalize()}")
    else:
        print("Error:", data.get("message", "Failed to fetch weather data."))

# Example usage
get_weather("Tashkent")
