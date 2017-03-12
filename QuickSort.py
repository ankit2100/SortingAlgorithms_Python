__author__ = 'ankit.b.patel'
# Worst Case time complexity :n log n (log n for divide and n for merge)
# Best case time complexity :n log n
# Space complexity :n
def QuickSort(mylist):
    less = []
    equal = []
    greater = []
    if len(mylist) > 1:
        pivot = mylist[0]
        for x in mylist:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return QuickSort(less)+equal+QuickSort(greater)  # Just use the + operator to join lists
    else:
        return mylist
print QuickSort([12,4,5,6,7,3,1,15])
