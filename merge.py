def mergeSort(aSort):
    if(len(aSort)<= 1):
        return aSort
  mIndex = len(aSort) / 2
    left = mergeSort(asort[:mIndex])
    right = mergeSort(aSort[mIndex:])
 result = []
    while((len(left)>0)and (len(right))>0):
        if(left[0]>right[0]):   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 if(len(left) >0):
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 return result
def main():
    l = [3,2,1,3]
    sortedList = mergeSort(l)
    print sortedList
 
