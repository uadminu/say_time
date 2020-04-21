from say_time import say_time
from datetime import datetime, timedelta


say_time()  # it says the now time

now = datetime.now()
new_obj = now + timedelta(hours=2, minutes=10)
say_time(new_obj)  # it says the time in 2 hours and 10 minutes later
