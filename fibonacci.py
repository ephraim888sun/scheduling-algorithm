import threading

def generate_fibonacci(n, result):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    result.extend(fib_sequence)

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))

    result = []
    thread = threading.Thread(target=generate_fibonacci, args=(n, result))
    thread.start()
    thread.join()  # Wait for the thread to finish execution

    print("Fibonacci sequence:")
    print(result)

if __name__ == "__main__":
    main()
