"""Dictionary will read fast because list has to find the index before multiplying the count"""

import random
import time

NAMES = ["Anand", "Anu", "Sowmi", "Raj", "Manoj", "Rajesh",
         "Pandiyan", "Ashik", "lakshmi", "Radha", "Supraja"]

print NAMES

def create_dataset():
    """ create a dataset with 5 million records """
    data = open('data.txt', 'w')
    limit = 5000000
    for _ in range(limit):
        name = random.choice(NAMES) + '\n'
        data.write(name)

# create_dataset()

def list_view():
    """ list view to read the data set """
    user_counts = []
    for _ in NAMES:
        user_counts.append(0)
    data = open('data.txt', 'r')
    lines = data.readlines()
    for row in lines:
        row = row.rstrip()
        if row != '':
            user_counts[NAMES.index(row)] += 1
    return user_counts

def dict_view():
    """ dict view to read the data set """
    user_counts = {}
    for row in NAMES:
        user_counts[row] = 0
    data = open('data.txt', 'r')
    lines = data.readlines()
    for row in lines:
        row = row.rstrip()
        if row != '':
            user_counts[row] += 1
    return user_counts

T1 = time.time()
print list_view()
T2 = time.time()
print "Time difference for List View is => %s " % (T2-T1)

T1 = time.time()
print dict_view()
T2 = time.time()
print "Time difference for Dict View is => %s " % (T2-T1)
