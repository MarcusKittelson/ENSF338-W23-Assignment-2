import time
import matplotlib.pyplot as plt

numbers = list(range(36))

original_times = []
improved_times = []

def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

def improved_func(n):
    fib_values = {}
    def fib(n):
        if n == 0 or n == 1:
            return n
        if n in fib_values:
            return fib_values[n]
        else:
            fib_values[n] = fib(n-1) + fib(n-2)
            return fib_values[n]
    return fib(n)

for i in numbers:
    start = time.time()
    original_func(i)
    end = time.time()
    original_times.append(end - start)

    start = time.time()
    improved_func(i)
    end = time.time()
    improved_times.append(end - start)

plt.plot(numbers, original_times, label='Original')
plt.plot(numbers, improved_times, label='Improved')
plt.xlabel('Input Into Function')
plt.ylabel('Time (Seconds)')
plt.title('Original Vs Improved Fibonacci Sequence Functions')
plt.legend()
plt.show()
