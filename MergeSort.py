def MergeSort(mylist):
    '''
    Time complexity: best case: n*n ,if inner loop if condition is always wrong
    worst case : n*n
    Space Complexity :o(1)
    :param mylist:
    :return:
    '''
    if len(mylist) <= 1:
        return mylist
    mid = len(mylist)/2
    left=MergeSort(mylist[0:mid])
    right=MergeSort(mylist[mid:len(mylist)])

    merged= left+right
    for i in range(1,len(merged)):
        if merged[i-1] > merged[i]:
            for j in range(0,i):
                if merged[j] > merged[i]:
                    merged[i],merged[j] =merged[j],merged[i]
    return merged

print MergeSort([50,1,4,1,7,34,2,0,5,3,1])