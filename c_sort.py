#!/usr/bin/env python3
"""
Visualize C functions
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""
from ctypes import CDLL, POINTER, c_int, CFUNCTYPE
from visualizer import Visualize

class SortC(Visualize):
    """
    Make the Visualize calls able to visualize c algorithms
    """
    def __init__(self, dim=1000, mode="rainbow", block_size=None, num=None):
        super().__init__(dim, mode, block_size, num)
        self.libsort = CDLL("./libsort.so")
        self.libsort.sort.restype = None
        self.libsort.sort.argtypes = [POINTER(c_int),
                                      c_int,
                                      CFUNCTYPE(c_int, POINTER(c_int))]

    def sortfun(self):
        """
        Returns a compatible python function
        that is wrapping the c function
        """
        def fun(data, drawfn):
            def draw(dat):
                self.data = list(dat[0:(len(data))])
                drawfn()
                return len(self.data)

            self.libsort.sort((c_int * len(data))(*data),               # The array
                              len(data),                                # length of the array
                              CFUNCTYPE(c_int, (POINTER(c_int)))(draw)) # Function pointer

        return fun


    def run(self):
        """
        Runs the sorting functions
        """
        #num = self.libsort.num_func()
        self.visualize(self.sortfun())

if __name__ == '__main__':
    SortC(mode="grayscale", block_size=4).run()
