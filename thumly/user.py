import MySQLdb
import credentials

class User(object):
    def __init__(self, email password):
        self.email = emal
		self.password = password

    def __str__(self):
        return "email: " + str(self.email) + "password: " + str(self.password)

    def save(self):
        """
        Saves this User to the database.
        """
        
        # Get new database instance
        db = credentials.getDatabase()

        cur = db.cursor()
        query = '''INSERT IGNORE INTO users
                VALUES(%s, %s);'''

        data = (self.email, self.password)
        cur.execute(query, data)

        # commit query
        db.commit()
        db.close()


def load(email):
		'''
		given a user email, returns that user
		'''
        # Get new database instance
        db = credentials.getDatabase()

        cur = db.cursor()
        query = '''SELECT * FROM users WHERE email = %s;'''
		cur.execute(query,email)
		
		user = ""
		for tup in cur:
			user = User(tup[0], tup[1])

        # commit query
        db.commit()
        db.close()
    return user

def loadAll():
		'''
		return a list of all users
		'''
		# Get new database instance
        db = credentials.getDatabase()

        cur = db.cursor()
        query = '''SELECT * FROM users;'''
		cur.execute(query,email)
		
		users = []
		for tup in cur:
			users.append(User(tup[0], tup[1]))

        # commit query
        db.commit()
        db.close()
    return users
	
def addUser(email, password):
		'''
		saves new user to db
		'''
		User(email,password).save()
	
def isUniqueEmail(email):
		'''
		returns true if email is not in db
		'''
		# Get new database instance
        db = credentials.getDatabase()

        cur = db.cursor()
		query = '''SELECT COUNT(*) FROM users WHERE email =%s;'''
		cur.execute(query, email)
	#return true if the email is unique
	return tup[0] == 0