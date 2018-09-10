from task import Task

def load_tasks(nTasks, nMachines):
    file = open('test.txt', 'r')
    firstLine = True
    tasks = []
    lines = [line.rstrip('\n') for line in file]
    for i in range(nTasks):
        newTask = Task(i)
        for j in range(nMachines):
            newTask.machineTimes.append(float(lines[(i*nMachines)+j]))
        tasks.append(newTask)    

    return tasks
