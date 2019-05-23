# Sorting visualizer

## Requirements

This works on Arch Linux running python 3.7.3
Other versions may work.

pygame 1.9.4 is used.
Install by:

```
pip3 install pygame --user
```

## Running

```
./main.py
```

or

```
python3 main.py
```

A window will appear, visualizing the different sorting algorithms.

## Adding your own sorting algorithm

Write your algorithm in a function that takes two parameters: the data list and a function to draw said list.
Then in the main.py file, add the line

```python
	vis.visualize(your_algorithm)
```

Spice up the algorithm with the drawing function to visualize it propperly.

## Implemented sorting algorithms

 * Radix sort
 * Heap sort
 * Merge sort
 * Quicksort
 * Selection sort
 * Insertion sort
 * Bubble sort

## Changing the visualization function

This is done by setting the mode property

```python
from visualizer import Visualize
from sort import radixsort

vis = Visualize()
vis.mode = "bars"
vis.visualize(radixsort)
```

The code above will visualize the radix sorting algorithm with bars

Currently implemented modes:
 * rainbow (this is the default)
 * grayscale
 * boxes
 * bars
 * bars_ordered (bars are green if they are greater than or equal to the one before, red otherwise)

## Other options

The window dimentions may be set with the `dim` variable when initializing `Visualize`

`block_size` is the with/height of the stripes in the rainbow, boxes and/or bars.
`num` is the number of stripes/bars etc.

# Visualizing C functions

Implement your c algorithm and add a call to it in the `c_sort.c:sort()` function.

Your sorting function needs to have the following signature:

```c
void my_sort_func(int *data, int size, int(*drawfn)(int* data));
```

To visualize a snapshot in the sorting, call the `drawfn(data)` function, with the data you wish to present as the only parameter.

Run `make` to compile the shared library and run

```bash
python3 c_sort.py
```

If you are on Windows, you may need to change the `Makefile` to generate a `dynlib` or `dll` something instead of a `so`. Then the `c_sort.py` file also needs to be changed to open the correct library.
