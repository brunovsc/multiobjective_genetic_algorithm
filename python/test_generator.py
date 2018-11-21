from random import randint

populationSizes = ["050", "100", "150", "200"]
mutationFactor = ["1", "5", "10"]
crossoverFactor = ["5", "10", "25", "50"]
elitismFactor = ["10", "25"]
crossoverOperator = ["1", "2", "3", "4"]
mutationOperator = ["1", "2"]
numberOfRuns = "5"

for a in range(len(populationSizes)):
	for b in range(len(mutationFactor)):
		for c in range(len(crossoverFactor)):
			for d in range(len(elitismFactor)):
				for e in range(len(crossoverOperator)):
					for f in range(len(mutationOperator)):
						print("python3 main.py \"tests/c_LL.txt\" 512 16 " + 
							populationSizes[a] + " " + 
							mutationFactor[b] + " " + 
							crossoverFactor[c] + " " + 
							elitismFactor[d] + " " + 
							crossoverOperator[e] + " " + 
							mutationOperator[f] + " " + 
							numberOfRuns)