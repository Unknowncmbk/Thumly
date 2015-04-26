#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="45.55.130.201", # your host, usually localhost
                     user="root", # your username
                      passwd="411itsair", # your password
                      db="thumly") # name of the data base

cur = db.cursor() 
cur.execute("SELECT * FROM restaurants")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
    print row

def _parse_like(uuid, rid, delta):

	# if user has liked restaurant before
	has_voted = check_vote(uuid, rid)
	if has_voted:

		# update their value
		query = '''UPDATE transactions 
				SET vote=? 
				WHERE uuid=? AND rid=?;'''

		cursor.execute(query, [delta, uuid, rid])

	else:

		# insert new value
		query = '''INSERT INTO transactions 
				(uuid, rid, vote)
				VALUES (?, ?, ?);'''

		cursor.execute(query, [uuid, rid, delta])

	return

if __name__ == '__main__':
	# Execute from command line
	if len(sys.argv) > 1:
		path = sys.argv[1]