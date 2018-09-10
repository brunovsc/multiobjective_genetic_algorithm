from individual import Individual
import heapq

class Population():

	def __init__(self, size):
		self.size = size
		self.individuals = []
		self.generation = 0
		self.highestFitness = 0
		self.lowestFitness = 0


	@staticmethod
	def generate(size, tasks):
		newPopulation = Population(size)
		for i in range(size):
			newIndividual = Individual.generate(newPopulation.generation, tasks)
			heapq.heappush(newPopulation.individuals, newIndividual)

		return newPopulation


	def show(self):
		print("\n===== POPULATION")
		copiedIndividuals = self.individuals.copy()
		while len(copiedIndividuals) > 0:
			individual = heapq.heappop(copiedIndividuals)
			individual.show()

