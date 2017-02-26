def SelectionSort(mylist):
    '''
    Time complexity: best case: n*n ,if inner loop if condition is always wrong
    worst case : n*n
    Space Complexity :o(1)
    :param mylist:
    :return:
    '''
    for i in range(len(mylist)):
        minindex=i
        for j in range(i+1,len(mylist)):
            if mylist[j] < mylist[minindex]:
                minindex = j
        mylist[i],mylist[minindex] = mylist[minindex],mylist[i]
        print mylist

SelectionSort([4,1,7,34,2,0,5,3,7])