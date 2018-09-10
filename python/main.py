from file_manager import load_tasks
from task import Task
from individual import Individual
from population import Population


print("\nMultiobjective Genetic Algorithm\n")

print("Number of tasks: ", end = "")
nTasks = int(input())
print("Number of machines: ", end = "")
nMachines = int(input())

Individual.nMachines = nMachines
Individual.nTasks = nTasks
Individual.tasks = load_tasks(nTasks, nMachines)

print("===== TASKS")
for task in Individual.tasks:
	task.show()
print()

print("Size of MAKESPAN population: ", end = "")
sizeMakespanPopulation = int(input())

makespanPopulation = Population.generate(sizeMakespanPopulation, Individual.tasks)

makespanPopulation.show()