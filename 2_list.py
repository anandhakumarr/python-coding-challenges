l = [23,23,6,7.2,6,'gr',4,'aand','43534']

l.append(1)
print 'l.append(1)', l

l.extend(['34',45,4])   # Will be in same memory
print "l.extend(['34',45,4])", l

l.insert(0,'234')
print "l.insert(0,'234')", l

l.remove(23)
print 'l.remove(23)', l

print l.pop(3)
print 'l.pop(3)', l

l.index(4)
print 'l.index(4)', l

print l.count(1), 'count'

l.reverse()
print l, 'reverse'

l.sort()
print l, 'sort'

del l[0]

print l[0]



list1 = [1,2,4,5]
list2 = list1

print list1 is list2 # Since use the same memory

list1[2] = 3
list1.append('23')
list1.extend(['23'])
print list1 is list2 # Since use the same memory

# Reasigning the list it will create new list
list1 = list1[:3]+[3]

print list1 is list2 # Since use the same memory
# l1 = [1,2,3,4,5]
# l1 = range(1000)
# from datetime import datetime
# from math import sqrt
#
# t1=datetime.now()
# l = [i**2 for i in l1]
# for i in range(len(l)):
#     for j in range(len(l)):
#         a = l[i]
#         b = l[j]
#         if i != j:
#             c = a+b
#             if c in l:
#                 pass
#                 # print 'Found', a,b,c
#                 # print sqrt(a), sqrt(b), sqrt(c)
# t2=datetime.now()
# print "Time diff is %s" %(t2-t1)


def findpos(l,v):
    for i in range(len(l)):
        if l[i]==v:
            pos = i
            break
    else:  # Execute if No break and completed noraml way
        pos = -1
    return pos

print findpos([2,4,1],12)


# Array Vs list
"""
Array

Single block of memory, fixed size of memory
Indexing is fast
Insertion/Delete is expensive . We have to shift it down by 1


List

Flexible size
Next element is linked
Access time propotional to i positon
Insertion/Deletion is easy like Pumping

"""



x = [1,2,2]

x = y

y is reference of x

y[0] = 11 # x also will change

y = x[:] or list(x) will create new list



"""

Methods: functions that belongs to ojects
"""
