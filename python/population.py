from individual import Individual
from random import randint
import heapq
import math

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

	def select_individual(self):
		indexIndividual = randint(0, len(self.individuals)-1)
		return self.individuals[indexIndividual]

	def insert_individual(self, newIndividual):
		if not self.is_duplicate(newIndividual):
			heapq.heappushpop(self.individuals, newIndividual)

	def is_duplicate(self, individualToInsert):
		for i in range(len(self.individuals)): # check if the element already exists in population (update generation if so)
			if individualToInsert.genotype == self.individuals[i].genotype:
				return True

		return False

	def average_fitness(self):
		sumTotal = 0.0
		for individual in self.individuals:
			sumTotal += individual.makespan
		average = sumTotal / len(self.individuals)
		return average

	def deviation(self, average):
		divisor = 0.0
		for individual in self.individuals:
			add = math.pow((individual.makespan - average), 2)
			divisor += add
		quotient = len(self.individuals) - 1
		deviation = math.sqrt(divisor / quotient)
		return deviation

	def best_individual(self):
		copiedIndividuals = self.individuals.copy()
		while len(copiedIndividuals) > 1:
			individual = heapq.heappop(copiedIndividuals)
		bestIndividual = heapq.heappop(copiedIndividuals)
		return bestIndividual

	def show(self):
		print("\n===== POPULATION")
		copiedIndividuals = self.individuals.copy()
		orderedList = []
		while len(copiedIndividuals) > 0:
			individual = heapq.heappop(copiedIndividuals)
			orderedList.append(individual)
		for i in range(len(orderedList)):
			orderedList[i].show()

	def show_simple(self):
		print("\n===== BEST INDIVIDUAL")
		bestIndividual = self.best_individual()
		print("ID: " + str(bestIndividual.identifier))
		print("Makespan: " + str(bestIndividual.makespan * -1))
		print("Generation: " + str(bestIndividual.generation))

