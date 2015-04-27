from flask import Flask
from flask import request
import filter_restaurants
from vote import Vote
import vote
from user import User
import user
app = Flask(__name__)

# http://45.55.130.201:5000/search/40.7,-74/sushi/<hot|top|not|bot|new|old>
@app.route('/search/<loc>/<query>/<fltr>')
def get_restaurants(loc, query, fltr="def"):
	"""
	Args:
		loc: location as lat,lng. Ex: '40.7, -74'
		query: what they are looking for
		fltr: what to sort the restaurants by

	Returns:
		A list of JSON objects which are sorted restaurants.
	"""
	restaurants = filter_restaurants.construct(loc, query, fltr)
	return str(restaurants)

# http://45.55.130.201:5000/vote/sbahr@bu.edu/4e5ebafeb0fb27e2bd3deb97/1
@app.route('/vote/<email>/<rid>/<vote>')
def parse_vote(email, rid, vote=1):
	"""
	Args:
		email: email of the user
		rid: restaurant id
		vote: 1 or -1
	Returns:
		True if the vote was added. False if it was modified.
	"""
	vote = Vote(email, rid, vote)
	result = vote.save()
	return str({"result": result})

# http://45.55.130.201:5000/user/add/sbahr@bu.edu/test
@app.route('/user/add/<email>/<passwd>')
def add_user(email, passwd):
	"""
	Args:
		email: email of the suer
		passwd: passof the user

	Returns:
		True if the user was added.
	"""
	user = User(email, passwd)
	result = user.save()
	return str({"result": result})

# http://45.55.130.201:5000/user/verify/sbahr@bu.edu/test
@app.route('/user/verify/<email>/<passwd>')
def verify_user(email, passwd):
	"""
	Args:
		email: email of the suer
		passwd: passof the user

	Returns:
		True if the user/pass combination is correct. False otherwise.
	"""
	user = User(email, passwd)
	result = user.verify()
	return str({"result": result})

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
