import MySQLdb
import credentials

class Restaurant(object):
    def __init__(self, rid, name, address, city, state, zip_code, phone, website, twitter, lat, lng):
        self.rid = rid
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.website = website
        self.twitter = twitter
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return "rid: " + str(self.rid) + "name: " + str(self.name) + "address: " + str(self.address) + "city: " + str(self.city) + "state: " + str(self.state) + "zip_code: " + str(self.zip_code) + "phone: " + str(self.phone) + "website: " + str(self.website) + "twitter: " + str(self.twitter) + "lat: " + str(self.lat) + "lng: " + str(self.lng)

    def save(self):
        """
        Saves this Restaurant to the database.
        """
        
        # Get new database instance
        db = credentials.getDatabase()

        cur = db.cursor()
        query = '''INSERT IGNORE INTO restaurants
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

        data = (self.rid, self.name, self.address, self.city, self.state, self.zip_code, self.phone, self.website, self.twitter, self.lat, self.lng)
        cur.execute(query, data)

        # commit query
        db.commit()
        db.close()

def load(rid):
    # Get new database instance
    db = credentials.getDatabase()

    cur = db.cursor()
    query = '''SELECT * FROM restaurants WHERE rid = %s;'''
    cur.execute(query, rid)

    rest = ""
    for tup in cur:
        rest = Restaurant(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7], tup[8], tup[9], tup[10])

    # commit query
    db.commit()
    db.close()

    return rest

def loadAll():
    # Get new database instance
    db = credentials.getDatabase()

    cur = db.cursor()
    query = '''SELECT * FROM restaurants;'''
    cur.execute(query)

    result = []
    for tup in cur:
        result.append(Restaurant(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7], tup[8], tup[9], tup[10]))

    # commit query
    db.commit()
    db.close()

    return result

def isUnique(rid):
    # Get new database instance
    db = credentials.getDatabase()

    cur = db.cursor()
    query = '''SELECT COUNT(*) FROM restaurants WHERE rid=%s;'''
    cur.execute(query, [rid])

    result = 0
    for tup in cur:
        result = tup[0]

    # commit query
    db.commit()
    db.close()

    return result == 0
