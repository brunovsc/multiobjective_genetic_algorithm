from file_manager import load_tasks
from random import randint
from task import Task
from individual import Individual
from population import Population


class GA():
	def __init__(self, filename, nTasks, nMachines, mutationFactor, populationSize, maxIterations):
		self.filename = filename
		self.nTasks = nTasks
		self.nMachines = nMachines
		self.mutationFactor = mutationFactor
		self.populationSize = populationSize
		self.maxIterations = maxIterations

	def execute_makespan(self):
		Individual.nMachines = self.nMachines
		Individual.nTasks = self.nTasks
		Individual.tasks = load_tasks(self.filename, self.nTasks, self.nMachines)

		makespanPopulation = Population.generate(self.populationSize, Individual.tasks)
		makespanPopulation.show_simple()

		for i in range(self.maxIterations):
			parent1, parent2 = makespanPopulation.select_parents()
			child1, child2 = Individual.crossover(parent1, parent2, i+1)
			makespanPopulation.insert_individual(child1)
			makespanPopulation.insert_individual(child2)

			mutationRand = randint(0, 100)
			if mutationRand <= self.mutationFactor:
				makespanPopulation.apply_mutation()

		makespanPopulation.show_simple()
		return makespanPopulation.best_individual()
