#!/usr/bin/env python3
"""
This will visualize stuff
"""

from time import sleep
from sort import (quicksort, bubblesort,
                  mergesort, heapsort, insertion_sort,
                  selection_sort, stalinsort)
from viz import Visualize

def main():
    """
    Visualize all dem stuff
    """
    vis = Visualize()
    vis.visualize(heapsort)
    sleep(2)
    vis.gen_data()
    vis.visualize(mergesort)
    sleep(2)
    vis.gen_data()
    vis.visualize(quicksort)
    sleep(2)
    vis.gen_data()
    vis.visualize(selection_sort)
    sleep(2)
    vis.gen_data()
    vis.visualize(insertion_sort)
    sleep(2)
    vis.gen_data()
    vis.visualize(bubblesort)
    sleep(2)
    vis.gen_data()
    vis.visualize(stalinsort)

if __name__ == '__main__':
    main()
