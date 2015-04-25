import urllib
import json
import sys
from restaurant import Restaurant
import restaurant
import credentials

#client_id, client_secret, ll, query
def parseURL(client_id, client_secret, ll, query):
    url = "https://api.foursquare.com/v2/venues/search?client_id=" + str(client_id) + "&client_secret=" + str(client_secret) + "&v=20130815&ll=" + str(ll) + "&query=" + str(query)

    response = urllib.urlopen(url);
    data = json.loads(response.read())
	results = []
	
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
			result.append(rid)
	return result
if __name__ == "__main__":
    if len(sys.argv) == 3:
        #get client information (id, secret)
        cr = credentials.getCredentials()
        #run parseURL(id, secret, lat/lng, query)
        parseURL(cr.client_id, cr.client_secret, sys.argv[1], sys.argv[2])
    else:
        print("Error: Expected python parseURL.py \"lat,lng\" \"query\")")
