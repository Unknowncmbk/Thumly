#!/usr/bin/python
import credentials
import parse_url
import restaurant

def construct(ll, query, fltr):
	fltr = fltr.lower()
	# get local credentials
	cr = credentials.getCredentials()

	# get list of rids that match this query around the location
	ids = parse_url.parse(cr.client_id, cr.client_secret, ll, query)

	if len(ids) == 0:
		return None

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

	if fltr == 'top':
		#top rid votes
		query = "SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE R.rid IN " + in_clause + " GROUP BY R.rid ORDER BY SUM(T.vote) DESC"
	elif fltr == 'hot':
		# Most votes in the last 7 days
		query = "SELECT R.rid, HOT.total_votes FROM restaurants R LEFT JOIN (SELECT T.rid as hid, SUM(T.vote) AS total_votes FROM transactions T WHERE T.creation > DATE_SUB(NOW(), INTERVAL 14 DAY) GROUP BY T.rid ORDER BY SUM(T.vote)) as HOT ON R.rid=HOT.hid WHERE R.rid IN " + in_clause + " GROUP BY R.rid ORDER BY HOT.total_votes DESC;"
		# query = '''SELECT R.rid, HOT.total_votes
		# 			FROM restaurants R
		# 			LEFT JOIN (
		# 				SELECT T.rid as hid, SUM(T.vote) AS total_votes 
		# 				FROM transactions T 
		# 				WHERE T.creation > DATE_SUB(NOW(), INTERVAL 14 DAY) 
		# 				GROUP BY T.rid 
		# 				ORDER BY SUM(T.vote)
		# 			) as HOT 
		# 			ON R.rid=HOT.hid 
		# 			WHERE R.rid IN ?
		# 			GROUP BY R.rid 
		# 			ORDER BY HOT.total_votes DESC;'''
	elif fltr == 'not':
		# Opposite of hot
		query = "SELECT R.rid, HOT.total_votes FROM restaurants R LEFT JOIN (SELECT T.rid as hid, SUM(T.vote) AS total_votes FROM transactions T WHERE T.creation > DATE_SUB(NOW(), INTERVAL 14 DAY) GROUP BY T.rid ORDER BY SUM(T.vote)) as HOT ON R.rid=HOT.hid WHERE R.rid IN " + in_clause + " GROUP BY R.rid ORDER BY HOT.total_votes ASC;"
	elif fltr == 'new':
		# The most recently voted on rids
		query = "SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE T.rid IN " + in_clause + " GROUP BY R.rid ORDER BY T.creation DESC;"
	elif fltr == 'old':
		# The most neglected rids
		query = "SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE T.rid IN " + in_clause + " GROUP BY R.rid ORDER BY T.creation ASC;"
	elif fltr == 'bot':
		# opposite of top
		query = "SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE R.rid IN " + in_clause + " GROUP BY R.rid ORDER BY SUM(T.vote) ASC"
	else:
		# return all restaurants we get from this call
		query = "SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE R.rid IN " + in_clause + " GROUP BY R.rid ORDER BY SUM(T.vote) DESC"
	
	cur.execute(query)

	restaurants = []
	for tup in cur:
		rid = tup[0]
		count = tup[1]
		if count == None:
			count = 0

		rest_dict = restaurant.load(rid).__json__()
		rest_dict["votes"] = str(count)
		# construct new restaurant
		restaurants.append(rest_dict)

	db.commit()
	db.close()

	print("Result size: ", len(restaurants))
	return restaurants
