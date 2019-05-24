#!/usr/bin/env python3
"""
Visualize C functions
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""
from ctypes import CDLL, POINTER, c_int, CFUNCTYPE
from visualizer import Visualize

DRAW_SIGNATURE = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

class SortC(Visualize):
    """
    Make the Visualize calls able to visualize c algorithms
    """
    def __init__(self, dim=1000, mode="rainbow", block_size=None, num=None, step_through=False):
        super().__init__(dim, mode, block_size, num, step_through)
        self.libsort = CDLL("./libsort.so")
        self.libsort.sort.restype = None
        self.libsort.sort.argtypes = [POINTER(c_int),
                                      c_int,
                                      DRAW_SIGNATURE]

    def sortfun(self):
        """
        Returns a compatible python function
        that is wrapping the c function
        """
        def fun(data, drawfn):
            def draw(dat, imp):
                self.data = list(dat[0:(len(data))])
                if imp:
                    important = list(imp[0:2])
                    drawfn(imp=important)
                else:
                    drawfn()
                return len(self.data)

            self.libsort.sort((c_int * len(data))(*data), # The array
                              len(data),                  # length of the array
                              DRAW_SIGNATURE(draw))                  # Function pointer

        return fun


    def run(self):
        """
        Runs the sorting functions
        """
        #num = self.libsort.num_func()
        self.visualize(self.sortfun())

if __name__ == '__main__':
    SortC(mode="bars", dim=1800).run()
