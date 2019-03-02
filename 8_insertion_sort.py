"""
Insertion Sort O(n2)

Firt Paper : Put in new stack

Second Paper:
    lower mark than first? place below first paper
    Higher mark than first? place above first paper

Third Paper

    insert into the correct positon with respect to first two papers

"""

def InsertionSort(seq):
    # Build longer and longer sorted slices
    # In each iteration seq[0:sliceEnd] already sorted

    # Move first element after sorted slice left
    # till it is in the correct place

    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos- 1])=(seq[pos-1],seq[pos])
            pos = pos - 1

l = [23,2,6,4,42]
InsertionSort(l)
print l
