
import urllib, json, sys, credentials
import Restaurant class


#client_id, client_secret, ll, query
def ParseURL(client_id, client_secret, ll, query):
    url = "https://api.foursquare.com/v2/venues/search?client_id=" + str(client_id) + "&client_secret=" + str(client_secret) + "&v=20130815&ll=" + str(ll) + "&query=" + str(query)

    response = urllib.urlopen(url);
    data = json.loads(response.read())

    venues = data["response"]["venues"]
    for v in venues:
        location = v["location"]
        if "address" in location:
            name = v["name"]
            address = location["address"]
            city = location["city"]
            state = location["state"]
            if "postalCode" in location:
                zipCode = location["postalCode"]
            lat = location["lat"]
            lng = location["lng"]

            contact = v["contact"]
            if "formattedPhone" in contact:
                phone = contact["formattedPhone"]
            if "url" in contact:
                website = contact["url"]
            if "twitter" in contact:
                twitter = contact["twitter"] 

        #Create Restaurant object
            rest = Restaurant(name, address, city, state, zipCode, phone, website, twitter, lat, lng)
            rest.save()
            
if __name__ == "__main__":
    if len(sys.argv) == 3:
        #get client information (id, secret)
        cr = credentials.getCredentials()
        #run parseURL(id, secret, lat/lng, query)
        parseURL(cr.client_id, cr.client_secret, sys.argv[1], sys.argv[2])
    else:
        print("incorrect input (python parseURL.py <'lat,lng'><'query'>)")
