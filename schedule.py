def read_schedule(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            task_name, priority, burst_time = line.strip().split(',')
            tasks.append((task_name.strip(), int(priority.strip()), int(burst_time.strip())))
    return tasks
