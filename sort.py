"""
Sorting algorithms
Author: Teodor Dahl Knutsen
"""

def quicksort(data, drawfn):
    """
    Entry point for quicksort
    """
    print('quicksort')
    qs(data, 0, len(data) - 1, drawfn)

#pylint: disable=invalid-name
def qs(data, lo, hi, drawfn):
    """
    Recursive quicksort
    """
    if lo < hi:
        p = partition(data, lo, hi, drawfn)
        qs(data, lo, p, drawfn)
        qs(data, p + 1, hi, drawfn)

def partition(data, lo, hi, drawfn):
    """
    Hoare partition sceme
    """
    pivot = data[int((lo + hi) / 2)]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1

        j -= 1
        while data[j] > pivot:
            j -= 1

        if i >= j:
            return j

        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        drawfn()

#
# BUBBLE SORT
#

def bubblesort(data, drawfn):
    """
    Bubblesort algorithm
    """
    print('Bubblesort')
    drawfn()
    swapped = True
    while swapped:
        swapped = False
        drawfn()
        for i in range(len(data) - 2):
            if data[i] > data[i + 1]:
                swapped = True
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp

#
# MERGE SORT
#

def merge(data, temp, lo, mid, hi, drawfn):
    """
    Merge two sub arrays
    """
    i = lo
    j = mid
    k = lo
    while k < hi:
        if i < mid and (j >= hi or data[i] <= data[j]):
            temp[k] = data[i]
            i += 1
        else:
            temp[k] = data[j]
            j += 1

        #drawfn()
        k += 1

def split(data, temp, lo, hi, drawfn):
    """
    Split a sub-array and merge it again
    """
    if hi > lo + 1:
        mid = int((lo + hi) / 2)
        split(temp, data, lo, mid, drawfn)
        split(temp, data, mid, hi, drawfn)
        merge(temp, data, lo, mid, hi, drawfn)
        i = lo
        while i < hi:
            temp[i] = data[i]
            i += 1
            drawfn(data=temp)

def mergesort(data, drawfn):
    """
    Mergesort algorithm
    """
    print('merge sort')
    split(data, [data[x] for x in range(len(data))], 0, len(data), drawfn)

#
# HEAP SORT
#

def left_child(x):
    return 2 + x + 1

def right_child(x):
    return 2 * x + 2

def parent(x):
    return int((x - 1) / 2)

def sift_down(data, start, end, drawfn):
    """
    Sift down
    """
    root = start

    while left_child(root) <= end:
        child = left_child(root)
        swap = root

        if data[swap] < data[child]:
            swap = child
        if child + 1 <= end and data[swap] < data[child + 1]:
            swap = child + 1
        if swap == root:
            return

        temp = data[root]
        data[root] = data[swap]
        data[swap] = temp

        root = swap
    drawfn()

def heapify(data, drawfn):
    """
    Turn an array into a heap
    """
    start = parent(len(data) - 1)
    while start >= 0:
        sift_down(data, start, len(data) - 1, drawfn)
        start -= 1

def heapsort(data, drawfn):
    """
    Heapsort yay
    """
    print('heap sort')
    heapify(data, drawfn)

    end = len(data) - 1
    while end > 0:
        temp = data[end]
        data[end] = data[0]
        data[0] = temp

        end -= 1

        sift_down(data, 0, end, drawfn)

#
# INSERTION SORT
#

def insertion_sort(data, drawfn):
    """
    Insertion sort
    """
    print('insertion sort')
    i = 1
    while i < len(data):
        j = i
        while j > 0 and data[j-1]>data[j]:
            tmp = data[j]
            data[j] = data[j-1]
            data[j-1] = tmp
            j -= 1
        drawfn()
        i += 1

#
# selection sort
#

def selection_sort(data, drawfn):
    """
    Selection sort
    """
    print('selection sort')
    min_idx = 0
    drawfn()
    for i in range(len(data)):
        j = i + 1
        while j < len(data):
            if data[j] < data[i] and data[min_idx] > data[j]:
                min_idx = j
            j += 1

        if min_idx != i:
            tmp = data[i]
            data[i] = data[min_idx]
            data[min_idx] = tmp
            drawfn()

        min_idx = i + 1

def destructionsort(data, drawfn):
    """
    Remove all elements that is not in order
    """
    print('destruction sort')
    least = data[0]
    for i in range(len(data)):
        if data[i] < least:
            data[i] = 0
            drawfn()
        else:
            least = data[i]
