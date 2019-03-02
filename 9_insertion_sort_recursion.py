def factorial(n):
    if n == 0:
        return 1
    else:
        return(n * factorial(n-1))

print factorial(3)
print factorial(5)
print factorial(7)

def multiply(m,n):
    if n == 1:
        return m
    else:
        return (m + multiply(m,n-1))

print multiply(3,5)
print multiply(13,2)

# Length of the list

def length(l):
    if l == []:
        return 0
    else:
        return(1 + length(l[1:]))

print length(range(997,1,-1))

# Recursion will fail for 998 we can increase the limit

import sys
sys.setrecursionlimit(10000)
print length(range(1000,1,-1))

# Sum of list of numbers

def sumlist(l):
    if l == []:
        return 0
    else:
        return (l[0] + sumlist(l[1:]))

print sumlist([32,3,5,2,42])

print "Recursive Insertion Sort"

def InsertionSort(seq):
    isort(seq,len(seq))

def isort(seq,k): # Sort slice seq [0:k]
    print seq, k
    if k > 1:
        isort(seq, k-1)
        print 'calling Insert'
        print seq, k-1
        insert(seq, k-1)

def insert(seq,k): # Insert seq[k] into sorted seq[0:k-1]
    pos = k
    while pos > 0 and seq[pos] < seq[pos-1]:
        (seq[pos],seq[pos- 1])=(seq[pos-1],seq[pos])
        pos = pos - 1

l = [23,2,6,4,42]
InsertionSort(l)
print l
