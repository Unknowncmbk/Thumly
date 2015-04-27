#!/usr/bin/python2.7.3

import random
import string
from user import User

"""
Inputs:
	size: The length of the key to generate.
	chars: Character set to generate

Return:
	A generated key of length size.
"""
def generateEmail(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

# generate 100 users
for i in range(0, 100):
	email = generateEmail() + str('@bu.edu')
	password = 'test'
	User(email,password).save()