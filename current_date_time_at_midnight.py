# tested on python 3.8
# created by Boniface Irungu
# Mwendia.bonface4@gmail.com
# Import libs
from datetime import datetime,date
todays_date = datetime.today()
# Now combine
midnight = datetime.combine(todays_date, datetime.min.time())
print("Todays Time at Midnight is : {0}".format(midnight))
