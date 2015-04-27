#!/usr/bin/python2.7.3

import random
import string
import user
import filter_restaurants
import generate_timestamp
import datetime
from random import randint
from vote import Vote

ll = "42.3601,-71.0589"
queries = ['sushi', 'burritos', 'pizza', 'ramen', 'burger', 'italian', 'bagels', 'chinese', 'japanese', 'thai']

# startDate = datetime.datetime(2015, 3, 1,13,00)
# for query in queries:
# 	restaurants = filter_restaurants.construct(ll, query, 'hott')
# 	if restaurants != None:
# 		restaurants = restaurants[0]
# 		rid = restaurants['rid']
# 		#valid query
# 		lstUsers = user.loadAll()
# 		for u in lstUsers:
# 			u_email = u.email
# 			# should vote
# 			if randint(0,3) == 0:
# 				# generate random vote
# 				vote = 1
# 				if randint(0,4) == 0:
# 					vote = -1
# 				date = generate_timestamp.random_date(startDate)
# 				v = Vote(u_email, rid, vote, date)
# 				v.save()
# 				print("Adding", str(u_email), "voting for", str(rid), "value", str(vote), "date", str(date))

startDate = datetime.datetime(2015, 3, 1,13,00)
lstUsers = user.loadAll()
# for each theme
for query in queries:
	restaurants = filter_restaurants.construct(ll, query, 'hott')
	if restaurants != None:
		restaurants = restaurants

		# for each user
		for u in lstUsers:
			u_email = u.email

			# calculate the chance to vote for it
			for r in restaurants:
				rid = r["rid"]
				r_name = r["name"]
				# should vote
				if randint(0,3) == 0:
					# generate random vote
					vote = 1
					if randint(0,4) == 0:
						vote = -1
					date = generate_timestamp.random_date(startDate)
					v = Vote(u_email, rid, vote, date)
					v.save()
					print("Adding", str(u_email), "voting for", str(r_name), "value", str(vote), "date", str(date))


