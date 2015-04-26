#!/usr/bin/python
import credentials
import parse_url
import restaurant

def construct(ll, query, fltr):
	# get local credentials
	cr = credentials.getCredentials()

	# get list of rids that match this query around the location
	ids = parse_url.parse(cr.client_id, cr.client_secret, ll, query)

	in_clause = "("
	for i in ids:
		in_clause += "'";
		in_clause += str(i)
		in_clause += "'";
		in_clause += ", "
	in_clause = in_clause[:-2]
	in_clause += ")"

	db = credentials.getDatabase()
	cur = db.cursor()

	query = ""

	if fltr == 'hot':
		# Most votes in the last 7 days
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " AND T.creation > DATE_SUB(NOW(), INTERVAL 7 DAY) GROUP BY T.rid ORDER BY SUM(T.vote) DESC;";
	elif fltr == 'not':
		# Opposite of hot
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " AND T.creation > DATE_SUB(NOW(), INTERVAL 7 DAY) GROUP BY T.rid ORDER BY SUM(T.vote) ASC;";
	elif fltr == 'new':
		# The most recently voted on rids
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " GROUP BY T.rid ORDER BY T.creation DESC;";
	elif fltr == 'old':
		# The most neglected rids
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " GROUP BY T.rid ORDER BY T.creation ASC;";
	elif fltr == 'bot':
		# opposite of top
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " GROUP BY T.rid ORDER BY SUM(T.vote) ASC;";
	else:
		#top rid votes
		query = "SELECT T.rid, SUM(T.vote) FROM transactions T WHERE T.rid IN " + in_clause + " GROUP BY T.rid ORDER BY SUM(T.vote) DESC;";
	
	cur.execute(query)

	restaurants = []
	for tup in cur:
		rid = tup[0]
		count = tup[1]
		print(rid, count)

		# construct new restaurant
		restaurants.append(restaurant.load(rid))

	db.commit()
	db.close()

	return restaurants

#construct("40.7,-74", "sushi", "hot")

