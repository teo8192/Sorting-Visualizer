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

    vis.mode = "bars"
    vis.visualize(radixsort)
    vis.visualize(mergesort)
    vis.mode = "boxes"
    vis.visualize(quicksort_hoare)
    #vis.mode = "boxes"
    vis.visualize(bubblesort)
    #vis.mode = "bars"
    vis.mode = "boxes"
    vis.visualize(heapsort)
    vis.visualize(quicksort_lomuto)
    vis.visualize(selection_sort)
    vis.visualize(insertion_sort)
    vis.mode = "bars_ordered"
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
