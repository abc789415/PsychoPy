from datetime import datetime

print "ymd ?"
date = raw_input()


week = datetime.strptime(date, "%Y%m%d").weekday()


print week
