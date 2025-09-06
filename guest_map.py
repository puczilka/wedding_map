# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 11:46:49 2025

@author: marta
"""

import plotly.graph_objects as go
import pandas as pd
from plotly.offline import plot

# Sample guest data
guest_locations = [
    ("Monika Szewczyk-Drosio", "Warsaw"),
    ("Marek Drosio", "Warsaw"),
    ("Agata Kwiatkowska", "Warsaw"),
    ("Katarzyna Drosio", "Warsaw"),
    ("Janek Drosio", "Warsaw"),
    ("Klaudia Drosio", "Warsaw"),
    ("Magdalena Lewandowska", "Warsaw"),
    ("Mikolaj Drosio", "Warsaw"),
    ("Paulina Drosio", "Warsaw"),
    ("Magda Szulecka", "Warsaw"),
    ("Matthew Wong", "Warsaw"),
    ("Kinga Badura", "Warsaw"),
    ("Mateusz Struk", "Warsaw"),
    ("Natalia Wisniewska", "Warsaw"),
    ("Alberto Carceles", "Warsaw"),
    ("Zuzia Szankin-Sordyl", "Warsaw"),
    ("Przemek Sordyl", "Warsaw"),
    ("Tosia Sordyl", "Warsaw"),
    ("Anna Skrzypczyk", "Warsaw"),
    ("Tomasz Pacalowski", "Warsaw"),
    ("Romka Szura", "Warsaw"),
    ("Pawel Baranczewski", "Stockholm"),
    ("Swietlana Baranczewska", "Stockholm"),
    ("Mark Baranczewski", "Stockholm"),
    ("Aga Szalasny", "Berlin"),
    ("Michael Lee", "Berlin"),
    ("Aubrey Aguilar", "Florida"),
    ("Alvaro Aguilar", "Florida"),
    ("Joanna Szydelko", "Wroclaw"),
    ("Daniel Phillip", "Wroclaw"),
    ("Claire Ducommun", "Toulouse"),
    ("Denis Ducommun", "Toulouse"),
    ("Anne-Laure Maurel", "Toulouse"),
    ("Alexandre Maurel", "Toulouse"),
    ("Loukianos Couvaras", "Toulouse"),
    ("Elodie Couvaras", "Toulouse"),
    ("Louise Couvaeas", "Toulouse"),
    ("Lea Jammes", "Albi"),
    ("Benoit Sicart", "Albi"),
    ("Laurence Sanchez", "Toulouse"),
    ("Bernard Vitipon", "Toulouse"),
    ("Martine Jammes", "Toulouse"),
    ("Thierry Jammes", "Toulouse"),
    ("Claudine Peyre", "Toulouse"),
    ("Peter Shipman", "Toulouse"),
    ("Lea Batier", "Bordeaux"),
    ("Baptiste Ducommun", "Bordeaux"),
    ("Jean-Pierre Margaix", "Calabria"),
    ("Helen Margaix", "Calabria"),
    ("Joel Ducommun", "Niort"),
    ("Annick Ducommun", "Niort"),
    ("Ericka Ducommun", "Niort"),
    ("Remi Ducommun", "Poitiers"),
    ("Noémie Ducommun", "Poitiers"),
    ("Axel Ducommun", "Poitiers"),
    ("Adrien Saint", "Strasbourg"),
    ("Adrien Zarantonello", "Clermont-Ferrand"),
    ("Marine Waag", "Clermont-Ferrand"),
    ("Christos Papoutsis", "Paderborn"),
    ("Dimitris Papoutsis", "London"),
    ("Robin Child", "London"),
    ("James Child", "London"),
    ("Nadeena Gattsche", "New Zealand"),
    ("Adhi Gattsche", "New Zealand"),
    ("Amanda Barabas", "Ohio"),
    ("Colin Morsfield", "Ohio"),
    ("Enle Choo", "California"),
    ("Adibah Adnan", "California"),
    ("Aleks Frelas", "Lublin"),
    ("Kasia Szymańska", "Lublin"),
    ("Valentin Ducommun", "Paris"),
    ("Laura Delafosse", "Paris"),
    ("Stephane Trochou", "Paris"),
    ("Florent Delafosse", "Paris"),
    ("Elina Delafosse", "Paris"),
    ("Jean Delafosse", "Paris"),
    ("Marc Ducommun", "Paris"),
    ("Thuy Ducommun", "Paris"),
    ("Alain Thébert", "Paris"),
    ("Michelle Thébert", "Paris"),
    ("Flora Jammes", "Amsterdam"),
    ("Martin Porret", "Amsterdam")
]

# City coordinates (lat, lon)
city_coords = {
    "Warsaw": (52.2297, 21.0122),
    "Stockholm": (59.3293, 18.0686),
    "Berlin": (52.5200, 13.4050),
    "Florida": (27.9944, -81.7603),
    "Wroclaw": (51.1079, 17.0385),
    "Toulouse": (43.6047, 1.4442),
    "Bordeaux": (44.8378, -0.5792),
    "Calabria": (39.3088, 16.3464),
    "Niort": (46.3234, -0.4647),
    "Poitiers": (46.5798, 0.3417),
    "Albi": (43.9249, 2.1487),
    "Paris": (48.8566, 2.3522),
    "Amsterdam": (52.3676, 4.9041),
    "Clermont-Ferrand": (45.7772, 3.0870),
    "Paderborn": (51.7189, 8.7575),
    "New Zealand": (-40.9006, 174.8860),
    "Strasbourg": (48.5734, 7.7521),
    "London": (51.5074, -0.1278),
    "Ohio": (40.4173, -82.9071),
    "California": (36.7783, -119.4179),
    "Lublin": (51.2465, 22.5684)
}

# Group guests by city
from collections import defaultdict
grouped_guests = defaultdict(list)
for name, city in guest_locations:
    grouped_guests[city].append(name)

# Prepare data for plotting
plot_data = []
for city, guests in grouped_guests.items():
    lat, lon = city_coords[city]
    plot_data.append({
        "city": city,
        "lat": lat,
        "lon": lon,
        "count": len(guests),
        "names": "<br>".join(guests)
    })

df = pd.DataFrame(plot_data)

# Create interactive map
fig = go.Figure(go.Scattergeo(
    lon = df["lon"],
    lat = df["lat"],
    hoverinfo='text' ,
    text = df.apply(lambda row: f"<b>{row['city']}</b><br>{row['count']} guest(s):<br>{row['names']}", axis=1),
    mode = 'markers',
    marker = dict(
        size = df["count"] * 2.5,
        color = '#FF2DD1',
        line = dict(width=0.5, color='black')
    )
))

# Layout settings
fig.update_geos(
    visible=True,
    resolution=50,
    showcountries=True,
    showland=True,
    landcolor="lightgreen",
    showocean=True,
    showrivers=False,
    lakecolor="lightblue",
    oceancolor="lightblue",
    projection_type="natural earth"
)

fig.update_layout(
    title='Guest Locations for Marta & Pierre-Yves\' Wedding',
    geo=dict(
        scope='world',
        showland=True,
    )
)


# Render the map in your default browser
plot(fig, filename="wedding_guest_map.html")