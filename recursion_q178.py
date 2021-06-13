def intersectionOfArraysRepeats(intList1,intList2):
    #ここから書きましょう
    outList = []
    for x in intList1:
        if x in intList2:
            # if the element in intList1 is included in intList2, it is made into the outList
            outList.append(x)
            # to avoid considering the element in intList2, the element should be removed
            intList2.pop(intList2.index(x))
    # sort the elements of outList in ascending order
    outList.sort()
    return outList

print(intersectionOfArraysRepeats([3,2,2,2,1,10,10],[3,2,10,10,10]))