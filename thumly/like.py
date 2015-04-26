import MySQLdb
import credentials

class Like(object):
	def __init__(uid, rid, vote, date=null):
		self.uid = uid
		self.rid = rid
		self.vote = vote
		self.date = date

	def __str__(self):
		return "uid: " + str(self.uuid) + "rid: " + str(self.rid) + "vote: " + str(self.vote) + "date: " + str(slef.date)

	def save(self):
		'''
		Saves this Vote to the database.
		'''
		if isUnique(uid, rid, vote):
			# Get new database instance
			db = credentials.getDatabase()

			cur = db.cursor()
			query = '''INSERT INTO transactions (uid, rid, vote)
					VALUES(%s, %s, %s);'''

			data = (self.uid, self.rid, self.vote)
			cur.execute(query, data)

			# commit query
			db.commit()
			db.close()
		else:
			#update
			# Get new database instance
			db = credentials.getDatabase()

			cur = db.cursor()
			query = '''UPDATE transactions
					SET vote = %s
					WHERE uid = %s AND rid = %s;'''

			data = (self.vote, self.uid, self.rid)
			cur.execute(query, data)

			# commit query
			db.commit()
			db.close()

def isUnique(uid, rid, vote):
	'''
	Args:
		uid: the user id
		rid: the restaurant id
		vote: the vote...

	Returns:
		True if a vote has not yet been submitted by the user for the restaurant.
	'''
	# Get new database instance
	db = credentials.getDatabase()

	cur = db.cursor()
	query = '''SELECT COUNT(*) FROM transactions WHERE uid =%s AND rid = %s;'''
	data = (self.uid, self.rid)
	cur.execute(query, data)

	count = 0
	for tup in cur:
		count = tup[0]

	return count == 0
	
def load(uid, rid):
	'''
	Args:
		uid: The user id.
		rid: The restaurant id.
	Returns:
		A like given the uid and rid.
	'''
	# Get new database instance
	db = credentials.getDatabase()

	cur = db.cursor()
	query = '''SELECT * FROM transactions WHERE uid = %s AND rid = %s;'''
	data = (self.uid, self.rid)
	cur.execute(query,data)

	like = ""
	for tup in cur:
		like = Like(tup[0], tup[1], tup[2], tup[3])

	# commit query
	db.commit()
	db.close()
	return like