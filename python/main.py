from genetic_algorithm import GA
from individual import Individual
import sys

if len(sys.argv) != 4:
	print("Wrong number of parameters (expected 4).")
	exit()

filename = sys.argv[1]
nTasks = int(sys.argv[2])
nMachines = int(sys.argv[3])

iterations = 1000

print("\nObjective Genetic Algorithm\n")

# print("\nNumber of executions: ", end = "")
# executions = int(input())

# print("Number of tasks: ", end = "")
# nTasks = int(input())

# print("Number of machines: ", end = "")
# nMachines = int(input())

# print("Mutation factor (percentage): ", end = "")
# mutationFactor = int(input())
mutationFactor = 10

# print("Size of MAKESPAN population: ", end = "")
# sizeMakespanPopulation = int(input())
sizeMakespanPopulation = 50

bestIndividuals = []
averages = []
for i in range(5):
	print("\n!!! EXECUTION " + str(i+1))
	bestIndividual, averageFitness = GA(filename, nTasks, nMachines, mutationFactor, sizeMakespanPopulation, iterations).execute_makespan()
	bestIndividuals.append(bestIndividual)
	averages.append(averageFitness)

logFilename = filename.replace(".txt", "_log.txt")
averageSum = 0.0
fitnessSum = 0.0
for i in range(5):
	averageSum += averages[i]
	averageFitness += bestIndividual.makespan * -1

averageSum /= 5.0
averageFitness /= 5.0
print(averageSum)
print(averageFitness)




