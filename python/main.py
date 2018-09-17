from file_manager import load_tasks
from random import randint
from task import Task
from individual import Individual
from population import Population

iterations = 10000


print("\nMultiobjective Genetic Algorithm\n")

# print("Number of tasks: ", end = "")
# nTasks = int(input())
nTasks = 512
# print("Number of machines: ", end = "")
# nMachines = int(input())
nMachines = 16

# print("Mutation factor (percentage): ", end = "")
# mutationFactor = int(input())
mutationFactor = 20

Individual.nMachines = nMachines
Individual.nTasks = nTasks
Individual.tasks = load_tasks(nTasks, nMachines)

# print("===== TASKS")
# for task in Individual.tasks:
# 	task.show()
# print()


# print("Size of MAKESPAN population: ", end = "")
# sizeMakespanPopulation = int(input())
sizeMakespanPopulation = 50
makespanPopulation = Population.generate(sizeMakespanPopulation, Individual.tasks)
makespanPopulation.show_simple()

for i in range(iterations):
	parent1, parent2 = makespanPopulation.select_parents()
	child1, child2 = Individual.crossover(parent1, parent2, i+1)
	makespanPopulation.insert_individual(child1)
	makespanPopulation.insert_individual(child2)

	mutationRand = randint(0, 100)
	if mutationRand <= mutationFactor:
		makespanPopulation.apply_mutation()

makespanPopulation.show_simple()

print()