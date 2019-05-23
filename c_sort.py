"""
Visualize C functions
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""
from ctypes import *
from array import array
from visualizer import Visualize

class SortC(Visualize):
    def __init__(self, dim=1000, mode="rainbow", block_size=None, num=None):
        super().__init__(dim, mode, block_size, num)
        self.libsort = CDLL("./libsort.so")
        self.sortfunction = None

    def sortfun(self):
        def fun(data, drawfn):
            def draw(dat):
                self.data = list(dat[0:(len(data))])
                drawfn()
                return 0

            drawfun = CFUNCTYPE(c_int, (POINTER(c_int)))(draw)
            dataarr = (c_int * len(data))(*data)

            self.libsort.sort.restype = None
            self.libsort.sort.argtypes = [POINTER(c_int),
                                          c_int,
                                          CFUNCTYPE(c_int, POINTER(c_int))]

            self.libsort.sort(dataarr, len(data), drawfun)

            # sortfunc(dataarr,
                     # len(data),
                     # drawfun)

        return fun


    def run(self):
        """
        Runs the sorting functions
        """
        #num = self.libsort.num_func()
        self.visualize(self.sortfun())

if __name__ == '__main__':
    SortC().run()
