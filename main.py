#!/usr/bin/env python3
"""
This will visualize stuff
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from time import sleep
from sort import (quicksort_lomuto, quicksort_hoare, bubblesort,
                  mergesort, heapsort, insertion_sort,
                  selection_sort, destructionsort, radixsort)
from visualizer import Visualize

def main():
    """
    Visualize all dem stuff
    """
    #vis = Visualize(500)
    vis = Visualize(w=4)

    vis.mode = "boxes"
    vis.visualize(bubblesort)

    vis.visualize(heapsort)
    vis.visualize(quicksort_lomuto)
    vis.visualize(quicksort_hoare)
    vis.visualize(radixsort)
    vis.visualize(mergesort)
    vis.visualize(selection_sort)
    vis.visualize(insertion_sort)
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
