#!/usr/bin/env python3
"""
This will visualize stuff
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from sort import (quicksort_lomuto, quicksort_hoare, bubblesort,
                  mergesort, heapsort, insertion_sort,
                  selection_sort, destructionsort, radixsort)
from visualizer import Visualize

def main():
    """
    Visualize all dem stuff
    """
    #vis = Visualize(500)
    vis = Visualize(block_size=4)

    vis.mode = "rainbow"
    vis.visualize(radixsort)
    vis.mode = "bars_ordered"
    vis.visualize(mergesort)
    vis.mode = "boxes"
    vis.visualize(quicksort_hoare)
    #vis.mode = "boxes"
    vis.visualize(bubblesort)
    #vis.mode = "bars"
    vis.visualize(heapsort)
    vis.visualize(quicksort_lomuto)
    vis.visualize(selection_sort)
    vis.visualize(insertion_sort)
    vis.mode = "grayscale"
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
