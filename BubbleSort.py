def BubbleSort(mylist):
    '''
    Time complexity: best case: n*n
    worst case : n*n
    Space Complexity :o(1)
    :param mylist:
    :return:
    '''
    for i in range(len(mylist)):
        for j in range(len(mylist)-1):
            if mylist[j+1] < mylist[j]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    print mylist

BubbleSort([4,1,7,34,2,0,5,3,7])