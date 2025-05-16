import requests
import json
from datetime import datetime

# Coordenades de Barcelona
latitude = 41.3874
longitude = 2.1686

# Obtenir la data d'avui
today = datetime.now().strftime("%Y-%m-%d")

# Crida a l'API d'Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=Europe%2FMadrid"
response = requests.get(url)
data = response.json()

# Extreure temperatures d'avui
hours = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

# Filtrar només les temperatures d'avui
temps_today = [temp for time, temp in zip(hours, temps) if time.startswith(today)]

# Càlculs
temp_max = max(temps_today)
temp_min = min(temps_today)
temp_avg = round(sum(temps_today) / len(temps_today), 2)

# Resultat
result = {
    "data": today,
    "maxima": temp_max,
    "minima": temp_min,
    "mitjana": temp_avg
}

# Guardar en un fitxer JSON
filename = f"temp_{today.replace('-', '')}.json"
with open(filename, "w") as f:
    json.dump(result, f, indent=4)

print(f"Dades guardades a {filename}")
