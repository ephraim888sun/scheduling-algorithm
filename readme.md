# Programming Assignment #1 For CS7343 - Operating Systems

### Fibanacci.py


I have developed a multithreaded program aimed at generating the Fibonacci sequence. The program operates in the following manner: Upon initiation, the user is prompted to input the desired number of Fibonacci numbers to be generated via the command line. Subsequently, the program spawns a distinct thread responsible for generating the Fibonacci numbers. These numbers are stored in a shared data structure, preferably an array, accessible by the threads. Upon completion of execution, the child thread relinquishes control, allowing the parent thread to retrieve and output the generated Fibonacci sequence. Given the dependency on the child thread's completion for output, the parent thread is programmed to wait until the child thread concludes its task.


```
Enter the number of Fibonacci numbers to generate: 10
Fibonacci sequence:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Schedule.py

Contains the function to read in the txt file and returns an array. We assume that the tasks all arrive at the same time.


### fcfs.py

Implementaiton of First Come First Serve


Results

```
Task Completion Times (FCFS):
T1: 20
T2: 45
T3: 70
T4: 85
T5: 105
T6: 115
T7: 145
T8: 170
```

