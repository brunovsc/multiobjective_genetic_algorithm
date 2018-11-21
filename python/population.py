from individual import Individual
from random import randint
from math import inf
import heapq
import math

class Population():

	def __init__(self, size):
		self.size = size
		self.individuals = []
		self.generation = 0
		self.bestIndividual = None


	@staticmethod
	def generate(size, tasks):
		newPopulation = Population(size)
		while len(newPopulation.individuals) < size:
			makespan = inf
			if (len(newPopulation.individuals) >= 1):
				makespan = newPopulation.best_individual().makespan
			newIndividual = Individual.generate(newPopulation.generation, tasks, makespan)
			if not newPopulation.is_duplicate(newIndividual):
				heapq.heappush(newPopulation.individuals, newIndividual)
		newPopulation.bestIndividual = newPopulation.individuals[0]
		return newPopulation


	def select_pair(self):
		indexParent1 = randint(0, len(self.individuals)-1)
		while True:
			indexParent2 = randint(0, len(self.individuals)-1)
			if indexParent2 != indexParent1:
				break
		parent1 = self.individuals[indexParent1]
		parent2 = self.individuals[indexParent2]
		return parent1, parent2


	def select_parents(self, crossoverFactor):
		parents = []
		numberOfParents = (int) (self.size * (crossoverFactor / 100))
		if numberOfParents % 2 == 0:
			numberOfParents -= 1
		numberOfPairs = (int) (numberOfParents / 2)
		for i in range(numberOfPairs):
			parent1, parent2 = self.select_pair()
			parents.append(parent1)
			parents.append(parent2)
		return parents


	def select_individual(self):
		indexIndividual = randint(0, len(self.individuals)-1)
		return self.individuals[indexIndividual]


	def insert_individual(self, newIndividual):
		# if not self.is_duplicate(newIndividual):
		heapq.heappush(self.individuals, newIndividual)
		best = self.individuals[0]
		self.bestIndividual = best


	def is_duplicate(self, individualToInsert):
		for i in range(len(self.individuals)): # check if the element already exists in population (update generation if so)
			if individualToInsert.genotype == self.individuals[i].genotype:
				return True
		return False


	def update_population(self, elitismFactor):
		newPopulation = []
		# ELITISM
		nElitism = (int) (self.size * (elitismFactor / 100))
		for i in range(nElitism):
			heapq.heappush(newPopulation, heapq.heappop(self.individuals))
		for i in range(self.size - nElitism):
			selectedIndividual = self.select_individual()
			heapq.heappush(newPopulation, selectedIndividual)
		self.individuals = newPopulation


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


	def variance(self, average):
		dev = self.deviation(average)
		var = pow(dev, 2)
		return var


	def makespan_sum(self):
		totalSum = 0.0
		for individual in self.individuals:
			totalSum = totalSum + individual.makespan
		return totalSum	


	def best_individual(self):
		return self.individuals[0]


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
		print("Makespan: " + str(bestIndividual.makespan))
		print("Generation: " + str(bestIndividual.generation))

