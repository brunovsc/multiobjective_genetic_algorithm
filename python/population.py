from individual import Individual
from random import randint
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
		while len(newPopulation.individuals) < size:
			newIndividual = Individual.generate(newPopulation.generation, tasks)
			if not newPopulation.is_duplicate(newIndividual):
				heapq.heappush(newPopulation.individuals, newIndividual)

		return newPopulation

	def select_parents(self):
		indexParent1 = randint(0, len(self.individuals)-1)
		while True:
			indexParent2 = randint(0, len(self.individuals)-1)
			if indexParent2 != indexParent1:
				break
		parent1 = self.individuals[indexParent1]
		parent2 = self.individuals[indexParent2]
		return parent1, parent2

	def insert_individual(self, newIndividual):
		if not self.is_duplicate(newIndividual):
			heapq.heappushpop(self.individuals, newIndividual)

	def is_duplicate(self, individualToInsert):
		for i in range(len(self.individuals)): # check if the element already exists in population (update generation if so)
			if individualToInsert.genotype == self.individuals[i].genotype:
				return True

		return False

	def show(self):
		print("\n===== POPULATION")
		copiedIndividuals = self.individuals.copy()
		orderedList = []
		while len(copiedIndividuals) > 0:
			individual = heapq.heappop(copiedIndividuals)
			orderedList.append(individual)
		for i in range(len(orderedList)):
			orderedList[i].show()

