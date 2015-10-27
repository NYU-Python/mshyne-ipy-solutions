import os, sys, time

class Logger:
	def __init__(self, filename, priority='DEBUG', datetime=True, scriptname=True):
		priorities = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
		
		self.log_line_spacer = "\n\n"
		
		for list_item in priorities:
			if list_item == priority:
				self.priority = priorities.index(list_item)
				break
			else:
				self.priority = 5
		
		self.datetime = datetime
		self.scriptname = scriptname
		
		self.write_file = open(os.path.dirname(sys.argv[0]) + "/" + filename, "a")

	def debug(self, message):
		self.write_log(message, 1)
		
	def info(self, message):
		self.write_log(message, 2)
	
	def warning(self, message):
		self.write_log(message, 3)
		
	def error(self, message):
		self.write_log(message, 4)
	
	def critical(self, message):
		self.write_log(message, 5)
	
	def write_log(self, message, priority):
		prepend = self.compose_prepend()
		if priority > self.priority:
			self.write_file.write(prepend + message + self.log_line_spacer)
		
	def compose_prepend(self):
		if self.datetime:
			if self.scriptname:
				return time.ctime() + " " + os.path.basename(sys.argv[0]) + " "
			else:
				return time.ctime() + " "
		if self.scriptname:
			return os.path.basename(sys.argv[0]) + " "
		else:
			return ""
	
	
if __name__ == "__main__":
	pass