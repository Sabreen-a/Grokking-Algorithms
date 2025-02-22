def findSmallest(arr):
    smalest = arr[0]  # Store the smallest element here
    smalest_index = 0  # Store the index of the smallest value here
    for i in range(1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_index = i
    return smalest_index  # Return the index of the smallest element


def SelectionSort(arr):
    newArr = []  # Create a new array for adding sorted elements
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Find the index of the smallest element
        newArr.append(arr.pop(smallest))  # Remove it from `arr` and add it to `newArr`
    return newArr


# Test the SelectionSort function
print(SelectionSort([5, 3, 6, 2, 10]))