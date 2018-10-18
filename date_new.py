from datetime import datetime

print "ymd ?"
date = raw_input()

a = datetime.strptime("19700101", "%Y%m%d") # 1970-01-01 is thursday
b = datetime.strptime(date, "%Y%m%d")

# total seconds form 1970-01-01 to input date
c = (datetime.strptime(date, "%Y%m%d") - datetime.strptime("19700101", "%Y%m%d")).total_seconds()

# passed day - 4
d = c / 86400 - 4
# remainder
e = d % 7

print a
print b
print c
print e
