import sys, os

class PersistDict(dict):
	def __init__(self, filename):
		dict.__init__(self)
		self.filename = os.path.abspath(filename)
		self.persist_dict = {}
		if filename in os.listdir(os.path.dirname(sys.argv[0])):
			#self.persist_dict = {}
			read_dict = open(filename)
			for line in read_dict.readlines():
				key, value = line.split('\t',1)
				self[key] = value
			#return persist_dict
		else:
			open(os.path.dirname(sys.argv[0]) + "/" +  filename, 'w')
	
	def __setitem__(self,key,value):
		dict.__setitem__(self,key,value)
	
	def __getitem__(self,key):
		return dict.__getitem__(self,self.__keytransform__(key))
	
	def __keytransform__(self,key):
		return key
			
if __name__ == "__main__":
	pass