from genetic_algorithm import GA
from individual import Individual
import sys
import graph

def main():
	print("\nObjective Genetic Algorithm\n")

	if len(sys.argv) != 9 and len(sys.argv) != 2:
		print("Wrong number of parameters (expected 2 or 9) but got " + str(len(sys.argv)))
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
		crossoverOperator = int(sys.argv[6])
		mutationOperator = int(sys.argv[7])
		nExecutions = int(sys.argv[8])

	filename = sys.argv[1]
	iterations = 50000

	summaryLogLines = []
	highests = []
	averages = []
	for i in range(nExecutions):
		arguments = ' '.join(sys.argv[1:])
		print("EXECUTION " + str(i+1) + " of " + arguments)
		bestIndividual, executionGenerations, executionAverages, executionHighests = GA(filename, nTasks, nMachines, mutationFactor, populationSize, crossoverOperator, mutationOperator, iterations).execute_makespan()
		highests.append(executionHighests)
		averages.append(executionAverages)

		graphName = filename.replace(".txt", "_graph_") + str(i+1) + ".png" 
		graph.plot_graph(filename, executionGenerations, executionHighests, executionAverages, graphName)
		summaryLogLine = logLine(filename, bestIndividual, executionAverages, populationSize, crossoverOperator, mutationOperator, mutationFactor)
		summaryLogLines.append(summaryLogLine)

	logFilename = filename.replace(".txt", "_log.txt")
	logAverages = []
	logHighests = []
	for i in range(len(executionGenerations)):
		averageSum = 0.0
		highestSum = 0.0
		for j in range(nExecutions):
			averageSum += (averages[j])[i]
			highestSum += (highests[j])[i]

		logAverage = averageSum / nExecutions
		logHighest = highestSum / nExecutions

		logAverages.append(logAverage)
		logHighests.append(logHighest)

	graphName = filename.replace(".txt", "_graph.png")
	graph.plot_graph(filename, executionGenerations, logHighests, logAverages, graphName)
	logSummary(summaryLogLines)

def logLine(filename, bestIndividual, executionAverages, populationSize, crossoverOperator, mutationOperator, mutationFactor):
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
	bestFitness = bestIndividual.makespan * -1
	bestGeneration = bestIndividual.generation
	average = executionAverages[-1]
	line = "{0:s} --- best: {1:.12f} --- average: {2:.12f} --- generation: {3:d} --- population: {4:d} --- {5:s} --- {6:s} {7:d}%\n".format(filename, bestFitness, average, bestGeneration, populationSize, crossoverOperatorName, mutationOperatorName, mutationFactor)
	return line


def logSummary(logLines):
	summaryLogFilename = "_summary.txt"
	with open(summaryLogFilename, "a") as file:
		file.write("\n")
		for line in logLines:
			file.write(line)
		file.close()

main()
