from random import randint
from task import Task
from individual import Individual
from population import Population
import file_manager

class GA():
	def __init__(self, filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, maxIterations):
		self.filename = filename
		self.nTasks = nTasks
		self.nMachines = nMachines
		self.mutationFactor = mutationFactor
		self.crossoverFactor = crossoverFactor
		self.elitismFactor = elitismFactor
		self.populationSize = populationSize
		self.maxIterations = maxIterations
		self.crossoverOperator = crossoverOperator
		self.mutationOperator = mutationOperator
		Individual.nextIndividualIdentifier = 0
		# temporary log holders
		self.logs = []
		self.logs_makespan = []
		self.logs_average = []
		self.logs_flowtime = []
		self.logs_generations = []

	def execute(self):
		Individual.nMachines = self.nMachines
		Individual.nTasks = self.nTasks
		Individual.tasks = file_manager.load_tasks(self.filename, self.nTasks, self.nMachines)
		Individual.crossoverMask = Individual.generate_crossover_mask(self.nTasks)

		makespanPopulation = Population.generate(self.populationSize, Individual.tasks)

		for i in range(self.maxIterations):
			currentMakespan = makespanPopulation.makespan_sum()
			# SELECTION
			parents = makespanPopulation.select_parents(self.crossoverFactor)

			# CROSSOVER
			childs = []
			childs = Individual.crossover_one_point(parents, i+1, currentMakespan)
			
			# MUTATION
			for child in childs:
				child.apply_mutation_simple(self.mutationFactor, currentMakespan)
				makespanPopulation.insert_individual(child)


			# INSERTION
			newPopulationIndividuals = makespanPopulation.update_population(self.elitismFactor)

			# LOGGING
			if(i % 100 == 0):
				self.save_log_information(i, makespanPopulation)

		return makespanPopulation.best_individual(), self.logs_generations, self.logs_average, self.logs_makespan, self.logs_flowtime


	def log_information(self):
		logFileName = self.filename.replace('.txt', '_log.txt')
		file = open(logFileName, "w")
		for logLine in self.logs:
			file.write(logLine)
		file.close()

	def save_log_information(self, generation, population):
		average = population.average_fitness()
		deviation = population.deviation(average)
		best = population.bestIndividual
		bestMakespan = best.makespan
		bestFlowtime = best.flowtime
		bestGeneration = best.generation
		stringData = "average: {0:5.12f} \tdeviation: {1:.12f}\tbest makespan: {2:.12f}\tbest flowtime: {3:.12f}\tgeneration: {4:d}\n".format(average, deviation, bestMakespan, bestFlowtime, bestGeneration) 
		self.logs.append(stringData)
		self.logs_makespan.append(bestMakespan)
		self.logs_flowtime.append(bestFlowtime)
		self.logs_average.append(average)
		self.logs_generations.append(generation)
	

