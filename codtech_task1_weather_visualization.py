# Internship Task 1 - API Integration and Data Visualization
# Company: CodTech
# Author: Akash N.S.
# Description:
#   This script fetches current weather data from OpenWeatherMap API for a specified city
#   and visualizes the temperature, humidity, and wind speed using Matplotlib.

import requests
import matplotlib.pyplot as plt

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Check the city name or API key.")
        return None

# Function to visualize the weather data
def visualize_weather_data(city, data):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [
        data['main']['temp'],
        data['main']['humidity'],
        data['wind']['speed']
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title(f"Weather Data for {city}")
    plt.ylabel("Values")
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + 0.5, round(yval, 2))
    plt.tight_layout()
    plt.savefig("weather_dashboard.png")
    plt.show()

# Main execution
if __name__ == "__main__":
    # Replace this with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    city = "Coimbatore"

    data = fetch_weather_data(city, api_key)
    if data:
        visualize_weather_data(city, data)
