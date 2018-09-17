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
		self.makespan = -(max(busyTimes))

	def make_copy(self, newGeneration):
		newIndividual = Individual(newGeneration)
		for i in range(Individual.nTasks):
			newIndividual.genotype.append(self.genotype[i])
		return newIndividual

	@staticmethod
	def crossover(parent1, parent2, generation):
		child1 = parent1.make_copy(generation)
		child2 = parent2.make_copy(generation)
		crossoverPoint = randint(1, Individual.nTasks - 1)
		for i in range(crossoverPoint, Individual.nTasks):
			aux = child1.genotype[i]
			child1.genotype[i] = child2.genotype[i]
			child2.genotype[i] = aux
		child1.calculate_makespan()
		child2.calculate_makespan()
		return child1, child2

	def show(self):
		print("\nID: " + str(self.identifier))
		print("Generation: " + str(self.generation))
		print("Makespan: " + str(self.makespan * -1))
		print("Genotype: ", end = "")
		for machine in self.genotype:
			print(machine, end = " ")
		print("")