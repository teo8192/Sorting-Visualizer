#!/usr/bin/env python3
"""
This will visualize stuff
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from time import sleep
from sort import (quicksort, bubblesort,
                  mergesort, heapsort, insertion_sort,
                  selection_sort, destructionsort)
from visualizer import Visualize

def main():
    """
    Visualize all dem stuff
    """
    vis = Visualize()
    vis.visualize(heapsort)
    sleep(2)
    vis.visualize(mergesort)
    sleep(2)
    vis.visualize(quicksort)
    sleep(2)
    vis.visualize(selection_sort)
    sleep(2)
    vis.visualize(insertion_sort)
    sleep(2)
    vis.visualize(bubblesort)
    sleep(2)
    vis.visualize(destructionsort)

if __name__ == '__main__':
    main()
