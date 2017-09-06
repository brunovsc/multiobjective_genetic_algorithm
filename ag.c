#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_TASK_TIME 20

typedef struct task {
    int machine;
    double *times;
} Task;

typedef struct individual {
	int id;
	Task *genotype;
	int sizeGenotype;
	int nMachines;
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

Task* generate_tasks(int nTasks, int nMachines);

Individual generate_individual(Task *tasks, int nTasks, int nMachines, int generation);
Population generate_population(Task *tasks, int nTasks, int nMachines, int sizePopulation);

double evaluate_individual_makespan(Individual);
double evaluate_individual_flowtime(Individual);

void evaluate_population(Population *);

void print_individual(Individual);
void print_population(Population);
void print_complete_individual(Individual);
void print_complete_population(Population);

int individualID = 0;

int main (int argc, char *argv[]){
	printf("Multiobjective Genetic Algorithm\n");

	int nTasks; // number of tasks in the system
	int nMachines; // number of machines in the system
	int sizePopulation1; // number of individuals in the population for objective 1
	/*
	int sizePopulation2; // number of individuals in the population for objective 2
	int sizePopulationBoth; // number of individuals in the population for both objectives

	double mutationFactor; // probability of mutation occurences on each iteration
	double coefficient1; // coefficient for weigth of first objective
	double coefficient2; // coefficient for weigth of second objective

	int iterations;
	double makespanMaxValue;
	double flowtimeMaxValue;
*/
	printf("\nNumber of tasks: ");
	scanf("%d", &nTasks);
	printf("Number of machines: ");
	scanf("%d", &nMachines);
	printf("Size of population 1: ");
	scanf("%d", &sizePopulation1);
	/*
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
    */
	srand(time(NULL));

    Task* tasks = generate_tasks(nTasks, nMachines);

	Population population1 = generate_population(tasks, nTasks, nMachines, sizePopulation1);

    evaluate_population_makespan(&population1);

	print_complete_population(population1);


	printf("\n");
	exit(0);
}

double evaluate_individual_makespan(Individual individual){
    int i;
    double busy_time[individual.nMachines];
    // initialize busy times to zero
    for(i = 0; i < individual.nMachines; i++){
        busy_time[i] = 0.0;
    }
    // compute busy time
    for(i = 0; i < individual.sizeGenotype; i++){
        Task t = individual.genotype[i];
        busy_time[t.machine - 1] += t.times[t.machine - 1]; // machine id from 1 to N
    }
    double max = 0.0;
    for(i = 0; i < individual.nMachines; i++){
        if(busy_time[i] > max){
            max = busy_time[i];
        }
    }
	return max;
}

double evaluate_individual_flowtime(Individual individual){
	int i;
    double busy_time[individual.nMachines];
    // initialize busy times to zero
    for(i = 0; i < individual.nMachines; i++){
        busy_time[i] = 0.0;
    }
    // compute busy time
    for(i = 0; i < individual.sizeGenotype; i++){
        Task t = individual.genotype[i];
        busy_time[t.machine - 1] += t.times[t.machine - 1]; // machine id from 1 to N
    }
    double sum = 0.0;
    for(i = 0; i < individual.nMachines; i++){
        sum += busy_time[i];
    }
    return sum;
}

void evaluate_population(Population *population){
    int i;
    for(i = 0; i < population->sizePopulation; i++){
        population->individuals[i].makespan = evaluate_individual_makespan(population->individuals[i]);
        population->individuals[i].flowtime = evaluate_individual_flowtime(population->individuals[i]);
    }
}

void evaluate_population_makespan(Population *population){
    evaluate_population(population);
    // sort by makespan fitness
    int i, key, j;
    for (i = 1; i < population->sizePopulation; i++){
        key = population->individuals[i].makespan;
        j = i - 1;
        while (j >= 0 &&  population->individuals[j].makespan > key){
            population->individuals[j + 1].makespan =  population->individuals[j].makespan;
            j = j-1;
        }
        population->individuals[j+1].makespan = key;
    }
    population->lowestFitness = population->individuals[0].makespan;
    population->highestFitness = population->individuals[population->sizePopulation - 1].makespan;
}

void evaluate_population_flowtime(Population *population){
    evaluate_population(population);
    // sort by makespan fitness
    int i, key, j;
    for (i = 1; i < population->sizePopulation; i++){
        key = population->individuals[i].flowtime;
        j = i - 1;
        while (j >= 0 &&  population->individuals[j].flowtime > key){
            population->individuals[j + 1].flowtime =  population->individuals[j].flowtime;
            j = j-1;
        }
         population->individuals[j+1].flowtime = key;
    }
    population->lowestFitness = population->individuals[0].flowtime;
    population->highestFitness = population->individuals[population->sizePopulation - 1].flowtime;
}


Task* generate_tasks(int nTasks, int nMachines){
    Task *tasks = (Task *) malloc(nTasks * sizeof(Task));
    int i, j;
    for(i = 0; i < nTasks; i++){
        tasks[i].machine = -1;
        tasks[i].times = (double *) malloc(nMachines * sizeof(double));
        for(j = 0; j < nMachines; j++){
            tasks[i].times[j] = rand() % MAX_TASK_TIME;
        }
    }
    return tasks;
}

Population generate_population(Task *tasks, int nTasks, int nMachines, int sizePopulation){
	Population population;
	population.sizePopulation = sizePopulation;
	population.highestFitness = -1;
	population.individuals = (Individual *) malloc(sizePopulation * sizeof(Individual));

	int i;
	for(i = 0; i < sizePopulation; i++){
		population.individuals[i] = generate_individual(tasks, nTasks, nMachines, 0); // initial generation = 0
	}

	return population;
}

Individual generate_individual(Task *tasks, int nTasks, int nMachines, int generation){
	Individual individual;
	individual.id = individualID++;
	individual.sizeGenotype = nTasks;
	individual.nMachines = nMachines;
	individual.generation = generation;
	individual.genotype = (Task *) malloc(nTasks * sizeof(Task));

	int i;
	int machine;
	for(i = 0; i < nTasks; i++){
        machine = (rand() % nMachines) + 1; // machine ids from 1 to N
		tasks[i].machine = machine;
		individual.genotype[i] = tasks[i];
	}

	return individual;
}

void print_individual(Individual individual){
	int i;
	int size = individual.sizeGenotype;
	for(i = 0; i < size; i++){
		printf("%d ", individual.genotype[i].machine);
	}
}

void print_complete_individual(Individual individual){
	int i, j;
	int size = individual.sizeGenotype;

    printf("\nID: %d\n", individual.id);
	printf("Size: %d\n", size);
	printf("Generation: %d\n", individual.generation);
	printf("Makespan: %lf\n", individual.makespan);
	printf("Flowtime: %lf\n", individual.flowtime);
	printf("Genotype: ");

	for(i = 0; i < size; i++){
		printf("\n(%d ,", individual.genotype[i].machine);
		for(j = 0; j < individual.nMachines; j++){
            printf(" %2.0lf", individual.genotype[i].times[j]);
		}
		printf(")");
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
