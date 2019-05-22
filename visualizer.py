"""
Visualize different sorting algorithms
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from random import randint
import pygame

def float_to_color(val, red_val=0, blue_val=1):
    """
    Turn a floating point to a color
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
    def __init__(self, dim=1000, mode="bars", w=1, num=1000):
        self.width = dim
        self.height = self.width
        self.data = []
        self.draw_funcs = {"bars": self.draw_bars,
                           "grayscale": self.draw_grayscale,
                           "boxes": self.draw_boxes,
                           "rainbow": self.draw_rainbow}
        self._mode = mode
        self._vis_func = self.draw_funcs[self.mode]
        self.num = num
        self.block_size = w
        if num * w != dim:
            self.block_size = w
            self.num = int(dim / w)
        #pylint: disable=no-member
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self._bg = (0, 0, 0)
        self._fg = (255, 255, 255)

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

    def draw_bars(self, data):
        """
        Visualizes the data as bars
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            if self.block_size == 1:
                pygame.draw.line(self.screen, self._fg, (x, self.height), (x, self.height - y))
            else:
                pygame.draw.rect(self.screen, self._fg,
                                 (x * self.block_size, self.height - y, self.block_size, y))

    def draw_boxes(self, data):
        """
        Visualizes the data as bars
        """
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            pygame.draw.rect(self.screen, self._fg,
                             (x * self.block_size, self.height - y,
                              self.block_size, self.block_size))

    def draw_rainbow(self, data):
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

    def draw_grayscale(self, data):
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

    def draw(self, data=None):
        """
        Draws the data array
        """
        if data is None:
            data = self.data
        #pylint: disable=no-member
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.draw.rect(self.screen, self._bg, (0, 0, self.width, self.height))

        self._vis_func(data)

        pygame.display.update()
