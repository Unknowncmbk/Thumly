import json, MySQLdb

class Credentials(object):
    def __init__(self, client_id, client_secret, host, username, password, database):
        self.client_id = client_id
        self.client_secret = client_secret
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def __str__(self):
        return "client-id: " + str(self.client_id) + "\nclient-secret: " + str(self.client_secret) + "\nhost: " + str(self.host) + "\nuser: " + str(self.username) + "\npass: " + str(self.password) + "\ndb: " + str(self.database) 


#read file for client-id/client-secret
json_data=open("../thumlycredentials.txt").read()
data = json.loads(json_data)

f_creds = data["foursquare-creds"]
d_creds = data["database-creds"]

creds = Credentials(f_creds["client-id"], f_creds["client-secret"], d_creds["host"], d_creds["user"], d_creds["password"], d_creds["database"])

def getCredentials():
    """
    Returns:
        The construct credentials object.
    """
    return creds

def getDatabase():
    return MySQLdb.connect(host=creds.host, user=creds.username, passwd=creds.password, db=creds.database)