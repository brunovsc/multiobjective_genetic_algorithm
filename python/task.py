class Task():
	def __init__(self, identifier, machineTimes = []):
		self.identifier = identifier 
		self.machineTimes = []


	def show(self):
		print("Task " + str(self.identifier) + ": ", end = "")
		size = len(self.machineTimes)
		for i in range(size):
			print(self.machineTimes[i], end = " ")
		print("")
