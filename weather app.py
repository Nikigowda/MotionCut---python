import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        main_data = weather_data["main"]
        weather = weather_data["weather"][0]
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather Condition: {weather['description']}")
    else:
        print("City not found or error fetching data. Please try again.")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
