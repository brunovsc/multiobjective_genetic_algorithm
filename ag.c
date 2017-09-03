#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct individual {
	int *genotype;
	int sizeGenotype;
	int generation;
	double makespan;
	double flowtime;
} Individual;

typedef struct population {
	Individual *individuals;
	int sizePopulation;
	double highestFitness;
	double lowestFitness;
} Population;

Individual generate_individual(int nTasks, int nMachines, int generation);
Population generate_population(int nTasks, int nMachines, int sizePopulation);

double evaluate_individual_makespan(Individual);
double evaluate_individual_flowtime(Individual);

void print_individual(Individual);
void print_population(Population);
void print_complete_individual(Individual);
void print_complete_population(Population);

int main (int argc, char *argv[]){
	printf("Multiobjective Genetic Algorithm\n");

	int nTasks; // number of tasks in the system
	int nMachines; // number of machines in the system
	int sizePopulation1; // number of individuals in the population for objective 1
	int sizePopulation2; // number of individuals in the population for objective 2
	int sizePopulationBoth; // number of individuals in the population for both objectives

	double mutationFactor; // probability of mutation occurences on each iteration
	double coefficient1; // coefficient for weigth of first objective
	double coefficient2; // coefficient for weigth of second objective

	int iterations;
	double makespanMaxValue;
	double flowtimeMaxValue;

	printf("\nNumber of tasks: ");
	scanf("%d", &nTasks);
	printf("Number of machines: ");
	scanf("%d", &nMachines);
	printf("Size of population 1: ");
	scanf("%d", &sizePopulation1);
	printf("Size of population 2: ");
	scanf("%d", &sizePopulation2);
	printf("Size of population both: ");
	scanf("%d", &sizePopulationBoth);
	printf("Mutation factor (percentage): ");
	scanf("%lf", &mutationFactor);
	mutationFactor /= 100;
	printf("Weight of first objective (percentage): ");
	scanf("%lf", &coefficient1);
	coefficient1 /= 100;
	printf("Weight of second objective (percentage): ");
	scanf("%lf", &coefficient2);
	coefficient2 /= 100;

	srand(time(NULL));
	Population population1 = generate_population(nTasks, nMachines, sizePopulation1);

	print_population(population1);

	printf("\n");
	exit(0);
}

Population generate_population(int nTasks, int nMachines, int sizePopulation){
	Population population;
	population.sizePopulation = sizePopulation;
	population.highestFitness = -1; 
	population.individuals = (Individual *) malloc(sizePopulation * sizeof(Individual));

	int i;
	for(i = 0; i < sizePopulation; i++){
		population.individuals[i] = generate_individual(nTasks, nMachines, 0); // initial generation = 0
	}

	return population;
}

Individual generate_individual(int nTasks, int nMachines, int generation){
	Individual individual;
	individual.sizeGenotype = nTasks;
	individual.generation = generation;
	individual.genotype = (int *) malloc(nTasks * sizeof(int));

	int i;
	for(i = 0; i < nTasks; i++){
		individual.genotype[i] = (rand() % nMachines) + 1; // machine ids from 1 to N
	}

	return individual;
}

double evaluate_individual_makespan(Individual individual){
	return 0.0;
}

double evaluate_individual_flowtime(Individual individual){
	return 0.0;
}

void print_individual(Individual individual){
	int i;
	int size = individual.sizeGenotype;
	for(i = 0; i < size; i++){
		printf("%d ", individual.genotype[i]);
	}
}

void print_complete_individual(Individual individual){
	int i;
	int size = individual.sizeGenotype;

	printf("\nSize: \n", size);
	printf("Generation: \n", individual.generation);
	printf("Makespan: \n", individual.makespan);
	printf("Flowtime: \n", individual.flowtime);
	printf("Genotype: ", individual.flowtime);

	for(i = 0; i < size; i++){
		printf("%d ", individual.genotype[i]);
	}
	
	printf("\n");
}

void print_population(Population population){
	printf("\nPRINTING POPULATION\n");
	int i;
	int size = population.sizePopulation;
	for(i = 0; i < size; i++){
		printf("\nIndividual %2d: ", i + 1);
		print_individual(population.individuals[i]);
		printf("\n");
	}
}

void print_complete_population(Population population){
	printf("\nPRINTING POPULATION\n");
	int i;
	int size = population.sizePopulation;

	printf("Size: %d\n", size);
	printf("Highest Fitness: %lf\n", population.highestFitness);
	printf("Lowest Fitness: %lf\n", population.lowestFitness);

	for(i = 0; i < size; i++){
		printf("\nIndividual %2d: ", i + 1);
		print_complete_individual(population.individuals[i]);
		printf("\n");
	}
}