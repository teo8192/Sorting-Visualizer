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
    vis = Visualize(block_size=4)
    #vis = Visualize(500)

    vis.visualize(radixsort)
    vis.mode = "ellipses"
    vis.visualize(mergesort)
    vis.mode = "grayscale"
    vis.visualize(quicksort_hoare)
    vis.mode = "boxes"
    vis.visualize(heapsort)
    vis.mode = "bars"
    vis.visualize(quicksort_lomuto)
    vis.mode = "bars_ordered"
    vis.visualize(selection_sort)
    exit()
    vis.mode = "boxes"
    #vis.mode = "boxes"
    vis.visualize(bubblesort)
    #vis.mode = "bars"
    vis.mode = "boxes"
    vis.visualize(insertion_sort)
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
