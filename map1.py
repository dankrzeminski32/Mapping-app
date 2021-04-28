import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_el(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

    

html = """
Volcano name: <br> 
<a href = "https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")
#map object from folium package

#Feature group
fg = folium.FeatureGroup(name = "My Map")

#for-loop to add multiple points on map from volcanoes.txt file 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (name, name, el), width = 200, height = 100)
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), fill = True, fill_color = color_el(el), fill_opacity = 0.8))







map.add_child(fg)


map.save("Map1.html")
