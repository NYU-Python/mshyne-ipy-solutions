import sys, os

class PersistDict(dict):
	def __init__(self, filename):
		dict.__init__(self)
		self.filename = os.path.abspath(filename)
		if filename in os.listdir(os.path.dirname(sys.argv[0])):
			read_dict = open(filename)
			for line in read_dict.readlines():
				key, value = line.split('\t',1)
				self[key] = value
		else:
			open(os.path.dirname(sys.argv[0]) + "/" +  filename, 'w')
	
	def __setitem__(self,key,value):
		dict.__setitem__(self,key,value)
		self.rewrite_dict(self.filename)
	
	def __getitem__(self,key):
		return dict.__getitem__(self,self.__keytransform__(key))
	
	def __keytransform__(self,key):
		return key
	
	def rewrite_dict(self, dictionary_file):
		temp_dict = open(dictionary_file, 'w')
		temp_dict.write('')
		temp_dict_2 = open(dictionary_file, 'a')
		for key in self:
			temp_dict_2.write(str(key) + "\t" + str(self[key]) + '\n')
		temp_dict_2.close()
			
if __name__ == "__main__":
	pass