# Function to perform Insertion Sort on an array
def insertionSort(data):
    # Get the length of the array
    n = len(data)
    # If the array has 0 or 1 element, it is already sorted, so return
    if n<=1:
        return
    # Iterate through the array starting from the second element
    for i in range(1,n):
        # Store the current element to be inserted
        key=data[i]
        # Initialize the index 'j' to the position before the current element
        j=i-1
        # Move elements of data[0..i-1], that are greater than key,
        # to one position ahead of their current position
        # until an element less than or equal to key is found
        while j>=0 and key < data[j]:
            # Shift the elements to the right to make space for the key
            data[j+1]=data[j]
            # Move to the previous position to continue comparisons
            j-=1
        # Place the key at its correct position in the sorted array
        data[j+1]=key
