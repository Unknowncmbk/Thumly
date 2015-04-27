import datetime
from random import randrange

startDate = datetime.datetime(2015, 3, 1,13,00)
def random_date(start):
   current = start
   curr = current + datetime.timedelta(days=randrange(50),minutes=randrange(60))
   return curr