import subprocess, sys

out = subprocess.check_output(['curl', sys.argv[1]])
print out

#subprocess.call(['curl',sys.argv[1]], stdout=open('times.html', 'w'), stderr=STDOUT)