import sys
import json
import matplotlib.pyplot as plt
import time
from threading import stack_size
stack_size(33554432)

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json") as InFile:
    data = json.load(InFile)

times = list()

for arr in data:
    print(len(arr))
    start = time.time()
    print("*")
    func1(arr, 0, len(arr) - 1)
    print("*")
    end = time.time()
    print(end-start)
    times.append(end-start)

print(times)

plt.plot(times, label='Original')
plt.xlabel('Input Into Function')
plt.ylabel('Time (Seconds)')
plt.title('Original Vs Improved Fibonacci Sequence Functions')
plt.legend()
plt.show()
