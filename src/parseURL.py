import urllib, json, MySQLdb
 
url = "https://api.foursquare.com/v2/venues/search?client_id=NT1Q3ARZLWDLBGCRGCHS525MSYC0FATCOADM0ASO4GUARSXN&client_secret=GJKH4AANMRTB2LQ45CH22WVBQHV2ZXZ4FJ1NQZTQEBE44OQC&v=20130815&ll=40.7,-74&query=sushi"

def parseFoursquareReq(client_id, client_secret, location, query):
    """
    Given the location and query, get the JSON response from FourSquare.
    Ex: Location = 40.7,-74 and query = sushi.

    """

    url = "https://api.foursquare.com/v2/venues/search?client_id=" + str(client_id) + "&client_secret=" + str(client_secret) + "&v=20130815&ll=" + str(location) + "&query=" + str(query)

    return


response = urllib.urlopen(url);
data = json.loads(response.read())
 
db = MySQLdb.connect(host="45.55.130.201", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="thumly") # name of the data base
 
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
 
 
    #Insert into Restaurants
        query = '''INSERT INTO restaurants
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
 
        cursor.execute(query, [name, address, city, state, zipCode, phone, website, twitter, lat, lng])