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

if len(required_args.intersection(argdict)) == 2:
	if len(valid_args.intersection(argdict)) == 4:
	#print "keep going"
		header_template = """From: {}
To: {}
Subject: {}
Body: {}""".format(argdict['from'], argdict['to'], argdict['subject'], argdict['body'])
		print header_template
	if len(valid_args.intersection(argdict)) == 3:
		if 'subject' in valid_args.intersection(argdict):
			header_template = """From: {}
To: {}
Subject: {}
Body:""".format(argdict['from'], argdict['to'], argdict['subject'])
			print header_template
		else:
			header_template = """From: {}
To: {}
Subject: 
Body: {}""".format(argdict['from'], argdict['to'], argdict['body'])
			print header_template
	else:
		header_template = """From: {}
To: {}
Subject:
Body:""".format(argdict['from'], argdict['to'])
		print header_template
else:
	if len(required_args.difference(argdict)) > 0:
		missing_arguments = ''
		for argument in required_args.difference(argdict):
			missing_arguments = missing_arguments + "\n" + argument
		if len(required_args.difference(argdict)) > 1:
			print "The following required arguments are missing:" + missing_arguments
		else:
			print "The following required argument is missing:" + missing_arguments
	
	invalid_arguments = ''
	for key in argdict.keys():
		if not key in valid_args:
			invalid_arguments = invalid_arguments + "\n" + key
	if not invalid_arguments == '':
		print "The following input was invalid:" + invalid_arguments