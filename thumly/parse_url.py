import urllib
import json
import sys
from restaurant import Restaurant
import restaurant

#client_id, client_secret, ll, query
def parse(client_id, client_secret, ll, query):
	"""
	Parameters:
		client_id: foursquare api client id
		client_secret: foursquare api client client_secret
		ll: lat/long coordinates as a string separated by comma
		query: what the user wants, ex: sushi

	Returns:
		A list of restaurant ids that satisfy this query. If 
			the restaurant id does not exist in our database,
			we add it.
	"""
	url = "https://api.foursquare.com/v2/venues/search?client_id=" + str(client_id) + "&client_secret=" + str(client_secret) + "&v=20130815&ll=" + str(ll) + "&query=" + str(query)

	response = urllib.urlopen(url);
	data = json.loads(response.read())
	result = []
	
	# actual read of data
	venues = data["response"]["venues"]
	for v in venues:

		location = v["location"]
		rid = v["id"].encode("utf-8")

		if "address" in location:

			if restaurant.isUnique(rid):
				
				name = v["name"].encode("utf-8")
				address = location["address"].encode("utf-8")
				city = location["city"].encode("utf-8")
				state = location["state"].encode("utf-8")
				zipCode = ""
				if "postalCode" in location:
					zipCode = location["postalCode"].encode("utf-8")
				lat = round(float(location["lat"]), 6)
				lng = round(float(location["lng"]), 6)

				phone = ""
				website = ""
				twitter = ""
				contact = v["contact"]
				if "formattedPhone" in contact:
					phone = contact["formattedPhone"].encode("utf-8")
				if "url" in contact:
					website = contact["url"].encode("utf-8")
				if "twitter" in contact:
					twitter = contact["twitter"].encode("utf-8")

				#Create Restaurant object
				rest = Restaurant(rid, name, address, city, state, zipCode, phone, website, twitter, lat, lng)
				rest.save()

			#append to result
			result.append(rid)
	return result
