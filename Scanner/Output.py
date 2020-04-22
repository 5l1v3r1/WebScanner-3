

class Output(object):

	def __init__(self, filename):
		if (filename):
			self.output = open(filename + ".txt", "w+")
		else:
			self.output = open("output.txt", "w+")


	def append(self, text):
		self.output.write(text + "\n")


	def openingMessage(self):
		self.append("Web Vulnerability Scanner")
		self.append("Designed and Built by Tyler Fuchs")
		self.append("For CprE 331X, Git Repository Can be Found: https://github.com/tfuchs98/WebScanner")
		self.append("")