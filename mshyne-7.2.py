import subprocess, sys

#out = subprocess.check_output(['curl', sys.argv[1]])
#print open(out).read()

subprocess.call(['curl',sys.argv[1]], stdout=open('outfile.txt', 'w'), stderr=STDOUT)