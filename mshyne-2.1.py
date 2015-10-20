import os, sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

args = sys.argv[1:]

argdict = {}

for argument in args:
	key = argument.split('=',1)[0]
	value = argument.split('=',1)[1]
	argdict[key] = value

invalid_arguments = ''
if len(set(argdict.keys()).difference(valid_args)) > 0:
	s = '\n'
	print "The following input was invalid: \n" + s.join(set(argdict.keys()).difference(valid_args))

if len(required_args.difference(argdict)) > 0:
	s = '\n'
	if len(required_args.difference(argdict)) > 1:
		print "The following required arguments are missing: \n" + s.join(required_args.difference(argdict))
		exit()
	else:
		print "The following required argument is missing: \n" + s.join(required_args.difference(argdict))
		exit()
	
if len(required_args.intersection(argdict)) == 2:
	header_template = """From: """ + argdict['from'] + """
To: """ + argdict['to'] + """
Subject: {}
Body: {}"""
	if len(valid_args.intersection(argdict)) == 4:
	#print "keep going"
		header_template.format(argdict['subject'], argdict['body'])
		print header_template
	if len(valid_args.intersection(argdict)) == 3:
		if 'subject' in valid_args.intersection(argdict):
			header_template.format(argdict['subject'], '')
			print header_template
		else:
			header_template.format('', argdict['body'])
			print header_template
	else:
		header_template.format('', '')
		print header_template
