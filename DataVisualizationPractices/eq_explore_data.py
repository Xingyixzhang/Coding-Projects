import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

# filename = 'files/global_files_json_csv/eq_data_1_day_m1.json'
filename = 'files/global_files_json_csv/eq_data_30_day_m1.json'
with open(filename) as file:
	all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

for key in colors.PLOTLY_SCALES.keys():
	print(key)

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]

	title = eq_dict['properties']['title']

	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_text.append(title)

### data = [Scattergeo(lon=lons, lat=lats)] Equivalent to:
#
#   data = [{
#		'type': 'scattergeo',
#		'lon': lons,
#		'lat': lats,
#	}]
#

data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_text,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	},
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='web_pages/global_earthquakes.html')
offline.plot(fig, filename='web_pages/global_earthquakes_2.html')

print(f'First 10 magnitude: {mags[:10]}')
print(f'First 5 Longitudes: {lons[:5]}')
print(f'First 5 Latitudes: {lats[:5]}')

readable_file = 'files/global_files_json_csv/readable_eq_data.json'
with open(readable_file, 'w') as file:
	json.dump(all_eq_data, file, indent=4)