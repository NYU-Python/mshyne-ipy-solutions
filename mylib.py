import sys, os

class PersistDict(dict):
	def __init__(self, filename):
		dict.__init__(self)
		self.filename = os.path.abspath(filename)
		if filename in os.listdir(os.path.dirname(sys.argv[0])):
			open(os.path.dirname(sys.argv[0]) + "/" + filename, 'w')
			
		else:
			open(os.path.dirname(sys.argv[0]) + "/" +  filename, 'w')
	
	def __setitem__(self,key,value):
		dict.__setitem__(self,key,value)
			
if __name__ == "__main__":
	pass