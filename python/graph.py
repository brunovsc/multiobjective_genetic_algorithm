import matplotlib.pyplot as plt

def plot_graph(title, generations, makespan, average, fileName):
	plt.plot(generations, makespan, linestyle=':', color='r')
	plt.plot(generations, average, linestyle='--', color='b')
	plt.xlabel('Número Gerações')
	plt.ylabel('Aptidão')
	plt.title(title.replace("tests/", "", 1))
	plt.legend(('Melhor Indivíduo', 'Média'), loc='upper right')
	plt.savefig(fileName)
	plt.close()

def plot_comparison(title, generations, makespan, otherMetric, fileName):
	plt.plot(generations, makespan, linestyle=':', color='r')
	plt.plot(generations, otherMetric, linestyle='--', color='b')
	plt.xlabel('Número Gerações')
	plt.ylabel('Aptidão')
	plt.title(title.replace("tests/", "", 1))
	plt.legend(('Makespan', 'Flowtime'), loc='upper right')
	plt.savefig(fileName)
	plt.close()