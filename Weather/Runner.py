import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
print("Weather Application - OpenWeatherMap\n")
city_name = input("Enter City Name: ")
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    temperature = y["temp"]
    temperature = ((temperature - 273.15) * 9 / 5 + 32)
    humidity = y["humidity"]
    z = x["weather"]
    description = z[0]["description"]
    celsiusTemp = (temperature - 32) * 5/9

    print("Temperature: (F) {:0.2f}ºF".format(temperature) + " (C) {:0.2f}ºC".format(celsiusTemp) + "\nDescription: " + str(description).upper())

else:
    print("Invalid City.")