"""
Sorting algorithms
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

def swap_array(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

def quicksort_lomuto(data, drawfn):
    """
    Entry point for quicksort
    """
    print('quicksort lomuto')
    qs_lomuto(data, 0, len(data) - 1, drawfn)

#pylint: disable=invalid-name
def qs_lomuto(data, lo, hi, drawfn):
    """
    Recursive quicksort
    """
    if lo < hi:
        p = partition_lomuto(data, lo, hi, drawfn)
        qs_lomuto(data, lo, p - 1, drawfn)
        qs_lomuto(data, p + 1, hi, drawfn)

def partition_lomuto(data, lo, hi, drawfn):
    """
    lomuto partition sceme
    """
    i = lo
    j = lo
    while j < hi:
        if data[j] < data[hi]:
            swap_array(data, i, j)
            drawfn()
            i += 1
        j += 1
    swap_array(data, i, hi)
    return i

def quicksort_hoare(data, drawfn):
    """
    Entry point for quicksort
    """
    print('quicksort hoare')
    qs_hoare(data, 0, len(data) - 1, drawfn)

#pylint: disable=invalid-name
def qs_hoare(data, lo, hi, drawfn):
    """
    Recursive quicksort
    """
    if lo < hi:
        p = partition_hoare(data, lo, hi, drawfn)
        qs_hoare(data, lo, p, drawfn)
        qs_hoare(data, p + 1, hi, drawfn)


def partition_hoare(data, lo, hi, drawfn):
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

        swap_array(data, i, j)
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
        for i in range(len(data) - 2):
            if data[i] > data[i + 1]:
                if i % 10 == 0:
                    drawfn()
                swapped = True
                swap_array(data, i, i + 1)
    drawfn()

#
# MERGE SORT
#

def merge(data, temp, lo, mid, hi):
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

        k += 1

def split(data, temp, lo, hi, drawfn):
    """
    Split a sub-array and merge it again
    """
    if hi > lo + 1:
        mid = int((lo + hi) / 2)
        split(temp, data, lo, mid, drawfn)
        split(temp, data, mid, hi, drawfn)
        merge(temp, data, lo, mid, hi)

        # This shit right here is not a part of the sorting algorithm,
        # but only to visulise it nicely
        i = lo
        while i < hi:
            temp[i] = data[i]
            drawfn(data=temp)
            i += 1

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
    """
    The index of the left child in a heap
    """
    return 2 * x + 1

def right_child(x):
    """
    Index of the right child in a heap
    """
    return 2 * x + 2

def parent(x):
    """
    Index of a parent in a heap
    """
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

        swap_array(data, root, swap)

        root = swap
        drawfn()

def heapify(data, drawfn):
    """
    Turn an array into a heap
    """
    for start in [len(data) - 1 - x for x in range(len(data))]:
        sift_down(data, start, len(data) - 1, drawfn)

    # start = parent(len(data) - 1)
    # while start >= 0:
        # sift_down(data, start, len(data) - 1, drawfn)
        # start -= 1

def heapsort(data, drawfn):
    """
    Heapsort
    This will turn an array into a heap,
    then take the largest element of that heap
    and put it on the end of a list
    O(n log n)
    """
    print('heap sort')
    heapify(data, drawfn)

    end = len(data) - 1
    while end > 0:
        swap_array(data, end, 0)

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
    for i in [x + 1 for x in range(len(data)-1)]:
        j = i
        while j > 0 and data[j-1] > data[j]:
            swap_array(data, j, j - 1)
            # do not use too long time, but still show what happens
            # if i % 20 == 0:
                # drawfn()
            j -= 1
        drawfn()

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
            swap_array(data, i, min_idx)
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

#
# RADIX SORT
#

def get_max(data):
    """
    Reutrns the max
    """
    mx = data[0]
    for i in data:
        if i > mx:
            mx = i
    return mx

def count_sort(data, exp, drawfn):
    """
    Count and sort
    """
    output = [0 for _ in range(len(data))]
    count = [0 for _ in range(10)]

    for d in data:
        count[int(d/exp) % 10] += 1

    for i in [x + 1 for x in range(9)]:
        count[i] += count[i - 1]

    i = len(data) - 1
    while i >= 0:
        output[count[int(data[i] / exp) % 10] - 1] = data[i]
        count[int(data[i] / exp) % 10] -= 1
        i -= 1

    for i, o in enumerate(output):
        data[i] = o
        drawfn()

def radixsort(data, drawfn):
    """
    Radix sort algorithm
    """
    print('radix sort')
    m = get_max(data)
    exp = 1
    while int(m / exp) > 0:
        count_sort(data, exp, drawfn)
        exp *= 10
