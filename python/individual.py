from random import randint

class Individual:
	nextIndividualIdentifier = 0
	nMachines = 0
	nTasks = 0
	tasks = []
	crossoverMask = []

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
	def crossover_one_point(parent1, parent2, generation):
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

	@staticmethod
	def crossover_two_point(parent1, parent2, generation):
		child1 = parent1.make_copy(generation)
		child2 = parent2.make_copy(generation)
		crossoverPointOne = randint(1, Individual.nTasks - 1)
		crossoverPointTwo = crossoverPointOne
		while crossoverPointTwo == crossoverPointOne :
			crossoverPointTwo = randint(1, Individual.nTasks - 1)
		left = min(crossoverPointOne, crossoverPointTwo)
		right = max(crossoverPointOne, crossoverPointTwo)
		for i in range(left, right):
			aux = child1.genotype[i]
			child1.genotype[i] = child2.genotype[i]
			child2.genotype[i] = aux
		child1.calculate_makespan()
		child2.calculate_makespan()
		return child1, child2

	@staticmethod
	def crossover_uniform_unique(parent1, parent2, generation):
		child1 = parent1.make_copy(generation)
		child2 = parent2.make_copy(generation)
		for i in range(0, Individual.nTasks):
			if Individual.crossoverMask[i] == 1:
				child1.genotype[i] = parent1.genotype[i]
				child2.genotype[i] = parent2.genotype[i]
			else:
				child2.genotype[i] = parent1.genotype[i]
				child1.genotype[i] = parent2.genotype[i]
		child1.calculate_makespan()
		child2.calculate_makespan()
		return child1, child2

	@staticmethod
	def crossover_uniform_multiple(parent1, parent2, generation):
		child1 = parent1.make_copy(generation)
		child2 = parent2.make_copy(generation)
		crossoverMask = Individual.generate_crossover_mask(Individual.nTasks)
		for i in range(0, Individual.nTasks):
			if crossoverMask[i] == 1:
				child1.genotype[i] = parent1.genotype[i]
				child2.genotype[i] = parent2.genotype[i]
			else:
				child2.genotype[i] = parent1.genotype[i]
				child1.genotype[i] = parent2.genotype[i]
		child1.calculate_makespan()
		child2.calculate_makespan()
		return child1, child2

	def apply_mutation_simple(self, mutationFactor):
		mutationRand = randint(0, 100)
		if mutationRand <= mutationFactor:
			indexMutation = randint(0, len(self.genotype)-1)
			newMachine = randint(0, Individual.nMachines)
			self.genotype[indexMutation] = newMachine
		self.calculate_makespan()

	def apply_mutation_uniform(self, mutationFactor):
		for i in range(0, len(self.genotype)-1):
			mutationRand = randint(0, 100)
			if mutationRand <= mutationFactor:
				newMachine = randint(0, Individual.nMachines)
				self.genotype[i] = newMachine
		self.calculate_makespan()

	@staticmethod
	def generate_crossover_mask(nTasks):
		crossoverMask = []
		for t in range(0, nTasks):
			assignedMachine = randint(1, 2)
			crossoverMask.append(assignedMachine)
		return crossoverMask

	def show(self):
		print("\nID: " + str(self.identifier))
		print("Generation: " + str(self.generation))
		print("Makespan: " + str(self.makespan * -1))
		print("Genotype: ", end = "")
		for machine in self.genotype:
			print(machine, end = " ")
		print("")