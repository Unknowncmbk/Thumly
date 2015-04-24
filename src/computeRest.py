'''
- computeRest(longitude, latitude, radius)
 
- make a query to restaurant table
- grab all the latitudes/longitudes
 
- somehow figure out which ones are in the right radius
 
- return their restaurant id's
 
'''
 
 
import MySQLdb
import math
 
db = MySQLdb.connect(host="45.55.130.201", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="thumly") # name of the data base
 
cur = db.cursor()
cur.execute("SELECT rid, latitude, longitude FROM restaurants")
 
 
restaurants = {}
 
 
# now, all restaurant locations are stored in restaurants dictionary
# with key being rid + a list of [lat, long]
for row in cur.fetchall() :
    restaurants[row[0]] = [float(row[1]), float(row[2])]
 
 
 
# findRests takes the restaurant dictionary, your current location as a [lat, long] pair,
# and the radius you'd like to search in in km
def findRests(restaurants, location, radius):
 
        close_restaurants = []
 
        current_lat = location[0]
        current_long = location[1]
 
        for rid in restaurants:
 
                rest_lat = restaurants[rid][0]
                rest_long = restaurants[rid][1]
 
                distance = haversine(current_long, current_lat, rest_long, rest_lat)
 
                if distance <= radius:
                        close_restaurants.append(rid)
 
 
        return close_restaurants
 
 
 
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees).
 
    Source: http://gis.stackexchange.com/a/56589/15183
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c
    return km
 
 
# print(findRests(restaurants, [50, 40], 10))