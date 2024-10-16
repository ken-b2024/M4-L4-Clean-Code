class WeatherDataFetcher:
    def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
    # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})
    
    def get_detailed_forecast(self,city):
    # Function to provide a detailed weather forecast for a city
        data = self.fetch_weather_data(city)
        return self.parse_weather_data(data)
    
class DataParser:
    def parse_weather_data(data):
    # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
class AppInterface:
    def __init__(self):
        self.parse_data = DataParser()
        self.fetch_data = WeatherDataFetcher()

    def get_detailed_forecast(self,city):
        # Function to provide a detailed weather forecast for a city
        data = self.fetch_data(city)
        return self.parse_data(data)
    
    def display_weather(self,city):
        # Function to display the basic weather forecast for a city
        data = self.fetch_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parse_data(data)
            print(weather_report)
    
    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

# if __name__ == "__main__":
AppInterface.main()