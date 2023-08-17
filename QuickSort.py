#fun to find the partitionposition
def parrtition(array,low,high):
    #chise the rightmost elemnt as pivot
    pivot=array[high]
    #pointer for greater elemnts
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
 
def quickSort(array,low,high):
    if low<high:
        pi=parrtition(array,low,high)
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)
data=[8,7,2,1,0,9,6]
print("Before Sorting")
print(data)
size=len(data)
quickSort(data,0,size-1)
print("After Sorting:")
print(data)

  




   

