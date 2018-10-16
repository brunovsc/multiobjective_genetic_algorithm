from task import Task

def load_tasks(filename, nTasks, nMachines):
    file = open(filename, 'r')
    firstLine = True
    tasks = []
    lines = [line.rstrip('\n') for line in file]
    for i in range(nTasks):
        newTask = Task(i)
        for j in range(nMachines):
            newTask.machineTimes.append(float(lines[(i*nMachines)+j]))
        tasks.append(newTask)    

    return tasks

def create_log_file(filename):
    logFileName = filename.replace('.txt', '_log.txt')
    file = open(logFileName, "w")
    file.close()

def append_string_to_file(filename, stringData):
    with open(filename, "a") as file:
        file.write(stringData)
    file.close()

