import math

def mergeSort(list):
    return mergeSortHelper(0, len(list)-1, list)

def mergeSortHelper(start, end, list):
    if start == end: return [list[start]]

    mid = math.floor((start + end) / 2)
    sortedLeft = mergeSortHelper(start, mid, list)
    sortedRight = mergeSortHelper(mid + 1, end, list)
   

    sortedLeft.append(float('inf'))
    sortedRight.append(float('inf'))

    li = 0
    ri = 0
    combinedArray = []
    
    for i in range(0, len(sortedLeft) + len(sortedRight) - 2):
        if sortedLeft[li] <= sortedRight[ri]:
            combinedArray.append(sortedLeft[li])
            li += 1
        else:
            combinedArray.append(sortedRight[ri])
            ri += 1
    
    return combinedArray


arr = [34,4546,32,3,2,8,6,76,56,45,34,566,1]
print(arr)
print(mergeSort(arr))