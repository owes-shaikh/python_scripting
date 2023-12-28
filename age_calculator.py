# DOB using datetime

import datetime
def get_age(y, m, d):
  today = datetime.datetime.now().date()
  print(today)
  dob = datetime.date(y, m, d)
  print(dob)
  age = int((today-dob).days/365.25)
  return age

get_age(1998, 9, 3)

# --> Output is 2023-12-28
#               1998-09-03
#               25
