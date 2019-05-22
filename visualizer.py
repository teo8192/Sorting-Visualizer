"""
Visualize different sorting algorithms
Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
"""

from random import randint
import pygame

class Visualize:
    """
    The visualize class
    """
    def __init__(self, dim=1000):
        self.width = dim
        self.height = self.width
        self.data = []
        #pylint: disable=no-member
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))

    def test_data(self):
        """
        Check if data is sorted
        """
        for i in range(len(self.data) - 1):
            if self.data[i] > self.data[i + 1]:
                print('array not sorted!')
                exit()
        print('Data is sorted!')

    def visualize(self, sortfn):
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
        self.data = [randint(0, self.height) for _ in range(self.width)]

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

        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.height))
        #pylint: disable=invalid-name
        for x, y in enumerate(data):
            pygame.draw.line(self.screen, (255, 255, 255), (x, self.height), (x, self.height - y))

        pygame.display.update()
