#!/usr/bin/python
import MySQLdb
import credentials
import time
from user import User

class Vote(object):
	def __init__(self, email, rid, vote, creation=""):
		self.email = email
		self.rid = rid
		self.vote = vote
		self.creation = creation

	def __str__(self):
		return "email: " + str(self.email) + "rid: " + str(self.rid) + "vote: " + str(self.vote) + "creation: " + str(self.creation)

	def __json__(self):
		json_object = {}
		json_object["email"] = str(self.email)
		json_object["rid"] = str(self.rid)
		json_object["vote"] = str(self.vote)
		json_object["date"] = str(self.creation)
		return json_object

	def save(self):
		'''
		Returns:
			The Vote object.
		'''
		User(self.email, "test").save()
		if isUnique(self.email, self.rid):
			# Get new database instance
			db = credentials.getDatabase()

			cur = db.cursor()

			# # generate votes
			# query = '''INSERT INTO transactions (uid, rid, vote, creation)
			# 		VALUES(%s, %s, %s, %s);'''

			# data = (self.email, self.rid, self.vote, self.creation.strftime('%Y-%m-%d %H:%M:%S'))

			query = '''INSERT INTO transactions (uid, rid, vote)
					VALUES(%s, %s, %s);'''

			data = (self.email, self.rid, self.vote)

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

			data = (self.vote, self.email, self.rid)
			cur.execute(query, data)

			# commit query
			db.commit()
			db.close()

		return self.__json__()
		

def isUnique(email, rid):
	'''
	Args:
		email: the user id
		rid: the restaurant id

	Returns:
		True if a vote has not yet been submitted by the user for the restaurant.
	'''
	# Get new database instance
	db = credentials.getDatabase()

	cur = db.cursor()
	query = '''SELECT COUNT(*) FROM transactions WHERE uid =%s AND rid = %s;'''
	data = (email, rid)
	cur.execute(query, data)

	count = 0
	for tup in cur:
		count = tup[0]

	return count == 0
	
def load(email, rid):
	'''
	Args:
		email: The user id.
		rid: The restaurant id.
	Returns:
		A vote given the email and rid.
	'''
	# Get new database instance
	db = credentials.getDatabase()

	cur = db.cursor()
	query = '''SELECT * FROM transactions WHERE uid = %s AND rid = %s;'''
	data = (email, rid)
	cur.execute(query,data)

	vote = ""
	for tup in cur:
		vote = Vote(tup[0], tup[1], tup[2], tup[3])

	# commit query
	db.commit()
	db.close()
	return vote