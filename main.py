#!/usr/bin/env python3
"""
This will visualize stuff
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from time import sleep
from sort import (quicksort, bubblesort,
                  mergesort, heapsort, insertion_sort,
                  selection_sort, destructionsort, radixsort)
from visualizer import Visualize

def main():
    """
    Visualize all dem stuff
    """
    #vis = Visualize(500)
    vis = Visualize()

    vis.visualize(radixsort)
    vis.visualize(heapsort)
    vis.visualize(mergesort)
    vis.visualize(quicksort)
    vis.visualize(selection_sort)
    vis.visualize(insertion_sort)
    vis.visualize(bubblesort)
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
