# Unsorted Case

# Worst case

"""
Have to scan the entire list

If the value is in last postion or not in the list.
"""
def search(seq,v):
    for x in seq:
        if x==v:
            return True
    return False

print search([1,2,4],3)


# Sorted Case

"""
    Compare the mid point of seq
    Binary search
"""


def bsearch(seq,v,left,right):
    # Assume the seq is sorted
    # Search v in seq[left:right]

    if (right-left) == 0:
        return False

    mid = (left+right)//2
    if seq[mid] == v:
        return True
    if seq[mid] < v:
        return bsearch(seq,v,mid+1,right)
    else:
        return bsearch(seq,v,left,mid)

print bsearch(range(121),134,0,121)
