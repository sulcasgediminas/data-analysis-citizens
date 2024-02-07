import googlemaps
from typing import List, Tuple
from dotenv import load_dotenv
import os

# Your Google API key
load_dotenv()
api_key = os.getenv('API_KEY')

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

# List of locations (your provided array)
locations = ['Vilniaus m. sav.', 'Šiaulių m. sav.', 'Jonavos r. sav.',
       'Šiaulių r. sav.', 'Kauno m. sav.', 'Klaipėdos m. sav.',
       'Alytaus m. sav.', 'Varėnos r. sav.', 'Pasvalio r. sav.',
       'Tauragės r. sav.', 'Širvintų r. sav.', 'Kupiškio r. sav.',
       'Panevėžio r. sav.', 'Kauno r. sav.', 'Pakruojo r. sav.',
       'Rokiškio r. sav.', 'Joniškio r. sav.', 'Telšių r. sav.',
       'Klaipėdos r. sav.', 'Ukmergės r. sav.', 'Marijampolės sav.',
       'Vilkaviškio r. sav.', 'Utenos r. sav.', 'Molėtų r. sav.',
       'Prienų r. sav.', 'Kalvarijos sav.', 'Šalčininkų r. sav.',
       'Raseinių r. sav.', 'Visagino sav.', 'Trakų r. sav.',
       'Panevėžio m. sav.', 'Šilutės r. sav.', 'Druskininkų sav.',
       'Kėdainių r. sav.', 'Plungės r. sav.', 'Vilniaus r. sav.',
       'Elektrėnų sav.', 'Jurbarko r. sav.', 'Kretingos r. sav.',
       'Kazlų Rūdos sav.', 'Kaišiadorių r. sav.', 'Neringos sav.',
       'Biržų r. sav.', 'Palangos m. sav.', 'Radviliškio r. sav.',
       'Akmenės r. sav.', 'Šakių r. sav.', 'Mažeikių r. sav.',
       'Anykščių r. sav.', 'Alytaus r. sav.', 'Zarasų r. sav.',
       'Lazdijų r. sav.', 'Šilalės r. sav.', 'Švenčionių r. sav.',
       'Pagėgių sav.', 'Skuodo r. sav.', 'Birštono sav.',
       'Kelmės r. sav.', 'Rietavo sav.', 'Ignalinos r. sav.', None]

def get_lat_long(locations: List[str]) -> List[Tuple[float, float]]:
    lat_long_list = []
    for location in locations:
        if location:
            geocode_result = gmaps.geocode(location)
            if geocode_result:
                lat = geocode_result[0]['geometry']['location']['lat']
                lng = geocode_result[0]['geometry']['location']['lng']
                lat_long_list.append((lat, lng))
            else:
                lat_long_list.append((None, None))
        else:
            lat_long_list.append((None, None))
    return lat_long_list

# Get latitude and longitude for each location
lat_long_results = get_lat_long(locations)

# Separate latitudes and longitudes into two lists
latitudes = [result[0] for result in lat_long_results]
longitudes = [result[1] for result in lat_long_results]

print(latitudes)
print(longitudes)
