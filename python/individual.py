from random import randint

class Individual:
	nextIndividualIdentifier = 0
	nMachines = 0
	nTasks = 0
	tasks = []

	def __init__(self, generation):
		self.generation = generation
		self.genotype = []
		self.makespan = 0
		self.flowtime = 0
		self.identifier = Individual.nextIndividualIdentifier
		Individual.nextIndividualIdentifier += 1

	def __lt__(self, otherIndividual):
		return self.makespan < otherIndividual.makespan

	@staticmethod
	def generate(generation, tasks):
		newIndividual = Individual(generation)
		for t in tasks:
			assignedMachine = randint(1, Individual.nMachines) # machines from 1 to N
			newIndividual.genotype.append(assignedMachine)

		newIndividual.calculate_makespan()
		return newIndividual

	def calculate_makespan(self):
		busyTimes = []
		for i in range(Individual.nMachines):
			busyTimes.append(0.0)
		for i in range(Individual.nTasks):
			machine = self.genotype[i] - 1
			busyTimes[machine] = busyTimes[machine] + Individual.tasks[i].machineTimes[machine]
		self.makespan = max(busyTimes)

	def show(self):
		print("\nID: " + str(self.identifier))
		print("Generation: " + str(self.generation))
		print("Makespan: " + str(self.makespan))
		print("Genotype: ", end = "")
		for machine in self.genotype:
			print(machine, end = " ")
		print("")