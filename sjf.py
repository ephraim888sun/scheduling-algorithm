import schedule

def sjf(tasks):
    current_time = 0
    completion_times = {}

    # Sort tasks by burst time
    sorted_tasks = sorted(tasks, key=lambda x: x[2])

    for task in sorted_tasks:
        task_name, priority, burst_time = task
        completion_time = current_time + burst_time
        completion_times[task_name] = completion_time
        current_time = completion_time

    return completion_times

def main():
    filename = "schedule.txt"
    tasks = schedule.read_schedule(filename)
    completion_times = sjf(tasks)

    print("Task Completion Times (SJF):")
    for task, completion_time in completion_times.items():
        print(f"{task}: {completion_time}")

if __name__ == "__main__":
    main()
