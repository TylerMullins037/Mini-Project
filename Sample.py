import random
import time
from QuickSort import quickSort
from MergeSort import mergeSort
from InsertionSort import insertionSort

# Function to generate a random list of integers within a specified range
def randomList(length, min, max):
    return [random.randint(min,max) for _ in range(length)]

# Function to measure the execution time of each sorting algorithm
def times(min, max):
    list1 = randomList(max,min,max)
    size = len(list1)
    alg_times =[]
    
    # Sort the list using Quick Sort and measure the execution time
    list1_copy = list1.copy()
    start_time = time.perf_counter()
    quickSort(list1_copy, 0, size-1)
    end_time = time.perf_counter()
    t1 = 1000*end_time - 1000*start_time # Convert time to milliseconds
    alg_times.append(t1)
   
    # Sort the list using Merge Sort and measure the execution time
    list1_copy = list1.copy()
    start_time = time.perf_counter()
    mergeSort(list1_copy)
    end_time = time.perf_counter()
    t2 = 1000*end_time - 1000*start_time # Convert time to milliseconds
    alg_times.append(t2)
    
    # Sort the list using Insertion Sort and measure the execution time
    list1_copy = list1.copy()
    start_time = time.perf_counter()
    insertionSort(list1_copy)
    end_time = time.perf_counter()
    t3 = 1000*end_time - 1000*start_time # Convert time to milliseconds
    alg_times.append(t3)

    # Return the list containing the execution times of each sorting algorithm
    return alg_times



