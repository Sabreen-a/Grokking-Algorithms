def QuickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i <=pivot]
        greater=[i for i in arr[1:] if i>pivot]
    return QuickSort(less)+[pivot]+QuickSort(greater)

print(QuickSort([1,5,2,3]))