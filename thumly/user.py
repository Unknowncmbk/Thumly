import MySQLdb
import credentials

class User(object):
    def __init__(self, email, password):
        self.email = email
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
        query = '''INSERT IGNORE INTO users (email, password)
                VALUES(%s, %s);'''

        data = (self.email, self.password)
        cur.execute(query, data)

        # commit query
        db.commit()
        db.close()

        return True

    def verify(self):
        """
        Returns:
            True if the user's credentials match the database. False otherwise.
        """

        if isUniqueEmail(self.email) == False:
            # Get new database instance
            db = credentials.getDatabase()

            cur = db.cursor()
            query = '''SELECT email, password FROM users WHERE email = %s;'''

            cur.execute(query, self.email)
            em = ""
            ps = ""
            value = False
            for tup in cur:
                em = tup[0]
                ps = tup[1]

            if em == self.email and ps == self.password:
                value = True

            # commit query
            db.commit()
            db.close()

            return value
        return False


def load(email):
    '''
    Args:
        email: The email to query.
    Returns:
        A user given the email.
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
    Returns:
        A list of all users.
    '''
    # Get new database instance
    db = credentials.getDatabase()

    cur = db.cursor()
    query = '''SELECT email, password FROM users;'''
    cur.execute(query)

    users = []
    for tup in cur:
        users.append(User(tup[0], tup[1]))

    # commit query
    db.commit()
    db.close()
    return users

def addUser(email, password):
    '''
    Saves a new user to the database.
    '''
    User(email,password).save()

def isUniqueEmail(email):
    '''
    Args:
        email: the email to query

    Returns:
        True if the email does not yet exist in the database.
    '''
    # Get new database instance
    db = credentials.getDatabase()

    cur = db.cursor()
    query = '''SELECT COUNT(*) FROM users WHERE email =%s;'''
    cur.execute(query, email)

    count = 0
    for tup in cur:
        count = tup[0]

    return count == 0