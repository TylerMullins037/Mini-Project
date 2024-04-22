# Function to perform Merge Sort on an array
def mergeSort(arr):
    # Check if the length of the array is greater than 1
    if len(arr) > 1:
        # Calculate the middle index of the array
        mid = len(arr) // 2
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        # Recursively call mergeSort on the left and right halves
        mergeSort(left_half)
        mergeSort(right_half)

        # Initialize indices for merging the left and right halves
        i = j = k = 0
        # Merge the left and right halves into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
 
