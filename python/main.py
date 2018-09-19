from genetic_algorithm import GA
from individual import Individual

iterations = 100000


print("\nMultiobjective Genetic Algorithm\n")

# print("\nNumber of executions: ", end = "")
# executions = int(input())

# print("Number of tasks: ", end = "")
# nTasks = int(input())
nTasks = 512
# print("Number of machines: ", end = "")
# nMachines = int(input())
nMachines = 16

# print("Mutation factor (percentage): ", end = "")
# mutationFactor = int(input())
mutationFactor = 20

# print("Size of MAKESPAN population: ", end = "")
# sizeMakespanPopulation = int(input())
sizeMakespanPopulation = 50

bestIndividual = GA("tests/c_LL.txt", nTasks, nMachines, mutationFactor, sizeMakespanPopulation, iterations).execute_makespan()

