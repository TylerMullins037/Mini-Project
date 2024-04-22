import random
import time
from QuickSort import quickSort
from MergeSort import mergeSort
from InsertionSort import insertionSort

def randomList(length, min, max):
    return [random.randint(min,max) for _ in range(length)]

def times(min, max):
    list1 = randomList(max,min,max)
    size = len(list1)
    alg_times =[]
    
    list1_copy = list1.copy()
    start_time = time.perf_counter()
    quickSort(list1_copy, 0, size-1)
    end_time = time.perf_counter()
    t1 = 1000*end_time - 1000*start_time
    alg_times.append(t1)

    list1_copy = list1.copy()
    start_time = time.perf_counter()
    mergeSort(list1_copy)
    end_time = time.perf_counter()
    t2 = 1000*end_time - 1000*start_time
    alg_times.append(t2)
    

    list1_copy = list1.copy()
    start_time = time.perf_counter()
    insertionSort(list1_copy)
    end_time = time.perf_counter()
    t3 = 1000*end_time - 1000*start_time
    alg_times.append(t3)
    return alg_times


