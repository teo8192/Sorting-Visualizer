"""
Visualize different sorting algorithms
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from random import randint
import pygame

def float_to_color(val, red_val=0, blue_val=1):
    """
    Turn a floating point to a color
    red_val is the lower bound
    blue_val is the upper bound
    """
    int_val = int(1023 * (val - red_val) / (blue_val - red_val))
    if int_val < 256:
        # from red to yelow
        return (255, int_val, 0)
    if int_val < 512:
        # yellow to green
        int_val -= 256
        return (255 - int_val, 255, 0)
    if int_val < 768:
        # green to aqua
        int_val -= 512
        return (0, 255, int_val)
    # aqua to blue
    int_val -= 768
    return (0, 255 - int_val, 255)

class Visualize:
    """
    The visualize class
    """
    def __init__(self, dim=1000, mode="rainbow", block_size=None, num=None, step_through=False):
        """
        dim: with and height dimensions of the screen, a single integer
        mode: string reprecenting the mode. default: 'rainbow'
        block_size: the size of the blocks/bars/rainbow stripes.
        num: the number of blocks/stripes/bars.

        only one of num and block_size needs to be set, sice the other
        one may be derived from the information of the window dimensions

        If the block_size and num does not multiply to the dim,
        dim gets set to the product of num and block_size
        """

        if num is None and block_size is None:
            self.num = dim
            self.block_size = 1
        else:
            if num is None:
                self.block_size = block_size
                self.num = int(dim / block_size)
            else:
                self.num = num
                self.block_size = int(dim / num)

        dim = self.block_size * self.num

        self.width = dim
        self.height = self.width
        self.data = []
        self.draw_funcs = {"bars": self.draw_bars,
                           "grayscale": self.draw_grayscale,
                           "boxes": self.draw_boxes,
                           "rainbow": self.draw_rainbow,
                           "bars_ordered": self.draw_bars_order,
                           "ellipses": self.draw_ellipses}
        self._mode = mode
        self._vis_func = self.draw_funcs[self.mode]

        #pylint: disable=no-member
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self._bg = (0, 0, 0)
        self._fg = (255, 255, 255)

        self.step_through = step_through

    @property
    def visualize(self):
        """
        Visualize a sorting function
        """
        return self.visualization

    @visualize.setter
    def visualize(self, val):
        if len(val) != 2:
            return

        self.draw_funcs[val[0]] = val[1]

    @property
    def mode(self):
        """
        The visualization mode
        """
        return self._mode

    @mode.setter
    def mode(self, val):
        if self.draw_funcs[val] is not None:
            self._vis_func = self.draw_funcs[val]
            self._mode = val

    def test_data(self):
        """
        Check if data is sorted
        """
        for i in range(len(self.data) - 1):
            if self.data[i] > self.data[i + 1]:
                print('array not sorted!')
                exit()
        print('Data is sorted!')

    def visualization(self, sortfn):
        """
        Visualize the sorting function
        """
        self.gen_data()
        sortfn(self.data, self.draw)
        self.test_data()

    def gen_data(self):
        """
        Regenerate the data array
        """
        self.data = [randint(0, self.height) for _ in range(self.num)]

    def draw_ellipses(self, data, imp=None):
        """
        Visualizes data as ellipses
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            x *= self.block_size / 2
            col = float_to_color(y / self.height)
            dim = self.width - x * 2
            pygame.draw.ellipse(self.screen, col, (x, x, dim, dim))


    def draw_bars(self, data, imp=None):
        """
        Visualizes the data as bars
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            if imp is not None and imp.__contains__(x):
                col = (255, 0, 0)
            else:
                col = self._fg
            if self.block_size == 1:
                pygame.draw.line(self.screen, col, (x, self.height), (x, self.height - y))
            else:
                pygame.draw.rect(self.screen, col,
                                 (x * self.block_size, self.height - y, self.block_size, y))

    def draw_bars_order(self, data, imp=None):
        """
        Visualizes the data as bars
        """
        prev = None
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            if prev is None or y >= prev:
                col = (0, 255, 0)
            else:
                col = (255, 0, 0)
            prev = y
            if self.block_size == 1:
                pygame.draw.line(self.screen, col, (x, self.height), (x, self.height - y))
            else:
                pygame.draw.rect(self.screen, col,
                                 (x * self.block_size, self.height - y, self.block_size, y))


    def draw_boxes(self, data, imp=None):
        """
        Visualizes the data as bars
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            if imp is not None and imp.__contains__(x):
                col = (255, 0, 0)
            else:
                col = self._fg
            pygame.draw.rect(self.screen, col,
                             (x * self.block_size, self.height - y,
                              self.block_size, self.block_size))

    def draw_rainbow(self, data, imp=None):
        """
        Grayscale visualization of the data
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            col = float_to_color(y / self.height)
            #pygame.draw.line(self.screen, (col, col, col), (x, 0), (x, self.height))
            if self.block_size == 1:
                pygame.draw.line(self.screen, col, (x, 0), (x, self.height))
            else:
                pygame.draw.rect(self.screen, col,
                                 (x * self.block_size, 0, self.block_size, self.height))

    def draw_grayscale(self, data, imp=None):
        """
        Grayscale visualization of the data
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            col = y / self.height
            col *= 255
            #pygame.draw.line(self.screen, (col, col, col), (x, 0), (x, self.height))
            if self.block_size == 1:
                pygame.draw.line(self.screen, (col, col, col), (x, 0), (x, self.height))
            else:
                pygame.draw.rect(self.screen, (col, col, col),
                                 (x * self.block_size, 0, self.block_size, self.height))

    def draw(self, data=None, imp=None):
        """
        Draws the data array
        """
        if data is None:
            data = self.data

        pygame.draw.rect(self.screen, self._bg, (0, 0, self.width, self.height))

        self._vis_func(data, imp)

        pygame.display.update()

        events = pygame.event.get()
        #pylint: disable=no-member
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        while self.step_through:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return

def example():
    """
    An example usage
    """
    from sort import radixsort, quicksort_hoare

    vis = Visualize(block_size=4)

    vis.visualize(radixsort)

    vis.mode = "boxes"

    vis.visualize(quicksort_hoare)

if __name__ == '__main__':
    example()
