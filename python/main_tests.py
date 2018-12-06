from individual import Individual
import sys
import graph
import genetic_algorithm11
import genetic_algorithm12
import genetic_algorithm21
import genetic_algorithm22
import genetic_algorithm41

def main():
	print("\nObjective Genetic Algorithm\n")

	if len(sys.argv) != 11 and len(sys.argv) != 2:
		print("Wrong number of parameters (expected 2 or 11) but got " + str(len(sys.argv)))
		exit()

	if len(sys.argv) == 2:
		print("Number of tasks: ", end = "")
		nTasks = int(input())
		print("Number of machines: ", end = "")
		nMachines = int(input())
		print("Size of MAKESPAN population: ", end = "")
		populationSize = int(input())
		print("Mutation factor (percentage): ", end = "")
		mutationFactor = int(input())
		print("Crossover factor (percentage): ", end = "")
		crossoverFactor = int(input())
		print("Elitism factor (percentage): ", end = "")
		elitismFactor = int(input())
		print("Crossover Operator (1..4): ", end = "")
		crossoverOperator = int(input())
		print("Mutation Operator (1..2): ", end = "")
		mutationOperator = int(input())
		print("\nNumber of executions: ", end = "")
		executions = int(input())
	else:
		nTasks = int(sys.argv[2])
		nMachines = int(sys.argv[3])
		populationSize = int(sys.argv[4])
		mutationFactor = int(sys.argv[5])
		crossoverFactor = int(sys.argv[6])
		elitismFactor = int(sys.argv[7])
		crossoverOperator = int(sys.argv[8])
		mutationOperator = int(sys.argv[9])
		nExecutions = int(sys.argv[10])

	filename = sys.argv[1]
	iterations = 50000

	summaryLogLines = []
	makespans = []
	flowtimes = []
	averages = []
	for i in range(nExecutions):
		arguments = ' '.join(sys.argv[1:])
		print("EXECUTION " + str(i+1) + " of " + arguments)
		if crossoverOperator == 1:
			if mutationOperator == 1:
				bestIndividual, executionGenerations, executionAverages, executionMakespans, executionFlowtimes = genetic_algorithm11.GA(filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute()
			else:
				bestIndividual, executionGenerations, executionAverages, executionMakespans, executionFlowtimes = genetic_algorithm12.GA(filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute()
		elif crossoverOperator == 2:
			if mutationOperator == 1:
				bestIndividual, executionGenerations, executionAverages, executionMakespans, executionFlowtimes = genetic_algorithm21.GA(filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute()
			else:
				bestIndividual, executionGenerations, executionAverages, executionMakespans, executionFlowtimes = genetic_algorithm22.GA(filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute()
		else:
			bestIndividual, executionGenerations, executionAverages, executionMakespans, executionFlowtimes = genetic_algorithm41.GA(filename, nTasks, nMachines, mutationFactor, crossoverFactor, elitismFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute()
		makespans.append(executionMakespans)
		flowtimes.append(executionFlowtimes)
		averages.append(executionAverages)

		graphName = '-'.join(sys.argv[1:]).replace(".txt", "") + "-" + str(i+1) + "-graph.png"
		print(graphName)
		graph.plot_graph(graphName, executionGenerations, executionMakespans, executionAverages, graphName)
		summaryLogLine = logLine(filename, bestIndividual, executionAverages, populationSize, crossoverOperator, crossoverFactor, mutationOperator, mutationFactor, elitismFactor)
		print(summaryLogLine)
		summaryLogLines.append(summaryLogLine)

	logFilename = filename.replace(".txt", "_log.txt")
	logAverages = []
	logMakespans = []
	for i in range(len(executionGenerations)):
		averageSum = 0.0
		makespansSum = 0.0
		for j in range(nExecutions):
			averageSum += (averages[j])[i]
			makespansSum += (makespans[j])[i]

		logAverage = averageSum / nExecutions
		logMakespan = makespansSum / nExecutions

		logAverages.append(logAverage)
		logMakespans.append(logMakespan)

	graphName = '-'.join(sys.argv[1:]).replace(".txt", "") + "-graph.png"
	graph.plot_graph(filename, executionGenerations, logMakespans, logAverages, graphName)
	logSummary(summaryLogLines)

def logLine(filename, bestIndividual, executionAverages, populationSize, crossoverOperator, crossoverFactor, mutationOperator, mutationFactor, elitismFactor):
	crossoverOperatorName = ""
	if crossoverOperator == 1:
		crossoverOperatorName = "crossover_one_point"
	elif crossoverOperator == 2:
		crossoverOperatorName = "crossover_two_point"
	elif crossoverOperator == 3:
		crossoverOperatorName = "crossover_uniform_simple"
	elif crossoverOperator == 4:
		crossoverOperatorName = "crossover_uniform_multiple"
	else:
		exit()

	mutationOperatorName = ""
	if mutationOperator == 1:
		mutationOperatorName = "mutation_simple"
	elif mutationOperator == 2:
		mutationOperatorName = "mutation_uniform"
	else:
		exit()

	file = filename.replace("tests/", "")
	bestFitness = bestIndividual.makespan
	bestGeneration = bestIndividual.generation
	average = executionAverages[-1]
	line = "{0:s} --- best: {1:.12f} --- average: {2:.12f} --- generation: {3:d} --- population: {4:d} --- {5:s} {6:d}% --- {7:s} {8:d}% --- elitism: {9:d}%\n".format(filename, bestFitness, average, bestGeneration, populationSize, crossoverOperatorName, crossoverFactor, mutationOperatorName, mutationFactor, elitismFactor)
	return line


def logSummary(logLines):
	summaryLogFilename = "_summary.txt"
	with open(summaryLogFilename, "a") as file:
		file.write("\n")
		for line in logLines:
			file.write(line)
		file.close()

main()
