"""
Selection Sort  O(n2)

Scan the entire list and move the min value to start positonself.

Start postion will change on each iteration

"""


def SelectionSort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i] < l[minpos]:
                minpos = i
        # if l[minpos] != l[start]:
        (l[minpos],l[start]) = (l[start],l[minpos])

l = [23,2,6,4,42]
SelectionSort(l)
print l

l = range(500,0,-1)
print l
SelectionSort(l)
print l

l = range(5000,0,-1)
SelectionSort(l)


"""

python will run in 1s if the computation is upto 10**7

In above selection sort we are running 2 loops so 5000x5000 will cross 10 power 7

so it will take more time to execute

time python sorting.py to check the time taken for
"""
