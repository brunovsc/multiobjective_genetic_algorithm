from random import randint
from task import Task
from individual import Individual
from population import Population
import file_manager
import matplotlib.pyplot as plt
import graph

class GA():
	def __init__(self, filename, nTasks, nMachines, mutationFactor, populationSize, maxIterations):
		self.filename = filename
		self.nTasks = nTasks
		self.nMachines = nMachines
		self.mutationFactor = mutationFactor
		self.populationSize = populationSize
		self.maxIterations = maxIterations
		self.logs = []
		self.logs_makespan = []
		self.logs_average = []
		self.logs_generations = []

	def execute_makespan(self):
		Individual.nMachines = self.nMachines
		Individual.nTasks = self.nTasks
		Individual.tasks = file_manager.load_tasks(self.filename, self.nTasks, self.nMachines)
		Individual.crossoverMask = Individual.generate_crossover_mask(self.nTasks)

		makespanPopulation = Population.generate(self.populationSize, Individual.tasks)
		print("\nINITIAL POPULATION")
		makespanPopulation.show_simple()

		for i in range(self.maxIterations):
			parent1, parent2 = makespanPopulation.select_parents()
			# child1, child2 = Individual.crossover_one_point(parent1, parent2, i+1)
			child1, child2 = Individual.crossover_two_point(parent1, parent2, i+1)
			# child1, child2 = Individual.crossover_uniform_unique(parent1, parent2, i+1)
			# child1, child2 = Individual.crossover_uniform_multiple(parent1, parent2, i+1)
			# child1.apply_mutation_simple(self.mutationFactor)
			# child2.apply_mutation_simple(self.mutationFactor)
			child1.apply_mutation_uniform(self.mutationFactor)
			child2.apply_mutation_uniform(self.mutationFactor)
			makespanPopulation.insert_individual(child1)
			makespanPopulation.insert_individual(child2)
			if(i % 100 == 0):
				self.save_log_information(i, makespanPopulation)

		print("\nFINAL POPULATION")
		makespanPopulation.show_simple()
		self.log_information()
		return makespanPopulation.best_individual(), makespanPopulation.average_fitness() * -1


	def log_information(self):
		logFileName = self.filename.replace('.txt', '_log.txt')
		file = open(logFileName, "w")
		for logLine in self.logs:
			file.write(logLine)
		file.close()
		graphName = self.filename.replace(".txt", "") + "_graph.png"
		graph.plot_graph(self.filename, self.logs_generations, self.logs_makespan, self.logs_average, graphName)


	def save_log_information(self, generation, population):
		average = population.average_fitness()
		deviation = population.deviation(average)
		best = population.best_individual()
		bestFitness = best.makespan
		bestGeneration = best.generation
		stringData = "average: {0:5.12f} \tdeviation: {1:.12f}\tbest: {2:.12f}\tgeneration: {3:d}\n".format(average * -1, deviation, bestFitness * -1, bestGeneration) 
		self.logs.append(stringData)
		self.logs_makespan.append(bestFitness * -1)
		self.logs_generations.append(generation)
		self.logs_average.append(average * -1)
	

