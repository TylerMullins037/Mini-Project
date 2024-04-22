def split(data, low, high):
    pivot = data[high]
    i = low-1
    for j in range(low,high):
        if data[j] <= pivot:
            i+=1
            (data[i], data[j]) = (data[j], data[i])
    (data[i+1], data[high]) = (data[high], data[i+1])
    return i+1

def quickSort(data, low, high):
    if low < high:
        piv = split(data, low, high)
        quickSort(data, low, piv - 1)
        quickSort(data, piv + 1, high)
    

