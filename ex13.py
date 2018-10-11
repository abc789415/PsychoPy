from sys import argv

script, a, b, c = argv

print "The script is called:", script
print "Your first variable is:", a
print "Your second variable is:", b
print "Your third variable is:", c

print "What ?"
x = raw_input()
print "So, your anwser is %r" % x
