# Function to partition the array around a pivot element
def split(data, low, high):
    # Select the pivot element (the last element in the array)
    pivot = data[high]
    # Initialize the index 'i' to track elements smaller than the pivot
    i = low-1
    # Iterate through the elements from 'low' to 'high - 1'
    for j in range(low,high):
        # If the current element is less than or equal to the pivot
        if data[j] <= pivot:
            # Increment the index 'i'
            i+=1
             # Swap the current element with the element at index 'i'
            (data[i], data[j]) = (data[j], data[i])
    # Swap the pivot element with the element at index 'i + 1'
    (data[i+1], data[high]) = (data[high], data[i+1])
    # Return the index of the pivot element after partitioning
    return i+1

# Function to perform Quick Sort recursively
def quickSort(data, low, high):
    # If the lower bound is less than the upper bound
    if low < high:
        # Partition the array and get the index of the pivot element
        piv = split(data, low, high)
        # Recursively sort the subarrays before and after the pivot element
        quickSort(data, low, piv - 1)
        quickSort(data, piv + 1, high)

