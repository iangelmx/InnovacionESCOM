def calcula_distancia_in_km(latitude1, longitude1, latitude2, longitude2):
	from math import sin, cos, sqrt, atan2, radians

	# approximate radius of earth in km
	R = 6378.0

	lat1 = radians(latitude1)
	lon1 = radians(longitude1)
	lat2 = radians(latitude2)
	lon2 = radians(longitude2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	print("Result:", distance)
	return distance
	#print("Should be:", 278.546, "km")

def get_nearest_hospitals(latitud, longitud):
	from googleplaces import GooglePlaces, types, lang
	from operator import itemgetter 
	
	# This is the way to make api requests 
	# using python requests library 
	
	# send_url = 'http://freegeoip.net/json' 
	# r = requests.get(send_url) 
	# j = json.loads(r.text) 
	# print(j) 
	# lat = j['latitude'] 
	# lon = j['longitude'] 
	
	# Use your own API key for making api request calls 
	API_KEY = 'AIzaSyC_tO0YLLkYTNrxBz1vdFvFf58g4CPYcGM'
	
	# Initialising the GooglePlaces constructor 
	google_places = GooglePlaces(API_KEY) 

	latitude_user = latitud
	longitude_user = longitud
	
	# call the function nearby search with 
	# the parameters as longitude, latitude, 
	# radius and type of place which needs to be searched of  
	# type can be HOSPITAL, CAFE, BAR, CASINO, etc 
	query_result = google_places.nearby_search( 
			# lat_lng ={'lat': 46.1667, 'lng': -1.15}, 
			lat_lng ={'lat': latitude_user, 'lng': longitude_user}, 
			radius = 5000, 
			# types =[types.TYPE_HOSPITAL] or 
			# [types.TYPE_CAFE] or [type.TYPE_BAR] 
			# or [type.TYPE_CASINO]) 
			types =[types.TYPE_HOSPITAL]) 
	#google_places.text_search()
	
	# If any attributions related  
	# with search results print them 
	if query_result.has_attributions: 
		print (query_result.html_attributions) 
	
	lugares_distancia = []
	# Iterate over the search results 
	for place in query_result.places: 
		# place.get_details()
		lugar = {
			'nombre' : place.name,
			'id_lugar': place.place_id,
			'direccion' : place.vicinity,
			'latitud_lugar' : float(place.geo_location['lat']),
			'longitud_lugar' : float(place.geo_location['lng']),
			'distancia' : calcula_distancia_in_km( latitude_user, longitude_user, place.geo_location['lat'], place.geo_location['lng'] )
		}
		
		
		lugares_distancia.append(lugar)
	
	lugares_ordenados = sorted( lugares_distancia, key=itemgetter('distancia') ) 

	#for lugar in lugares_ordenados:
	#	print(lugar)
	
	if len(lugares_ordenados)>10:
		return lugares_ordenados[:10]
	else:
		return lugares_ordenados