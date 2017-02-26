import datetime
def Bucketsort(mylist):
    '''
    Time complexity: best case: o(n+k) ,k is max number
    worst case : n*m ,n is number of element and m is their occurance
    Space Complexity :o(n*m)
    :param mylist:
    :return:
    '''
    buckets=[[] for i in range(max(mylist)+1)]
    for ele in mylist:
        buckets[ele].append(ele)
    for bucket in buckets :
        for ele in bucket:
            print ele,
start = datetime.datetime.now()
Bucketsort([4,1,90,7,34,2,0,100,5,3,50,7,5,3,50,1,1,3,55,5,6,60,4,4])
end =datetime.datetime.now()
print "Time taken to execute : " +str(end-start)