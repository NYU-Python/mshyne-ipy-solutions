import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])


args = sys.argv[1:]

#print args

argdict = {}

for argument in args:
	key = argument.split('=',1)[0]
	value = argument.split('=',1)[1]
	argdict[key] = value

if len(required_args.intersection(argdict)) == 2 and len(valid_args.intersection(argdict)) == 4:
	print "keep going"
else:
	print "error"

#print argdict