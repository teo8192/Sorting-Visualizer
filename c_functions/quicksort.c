/*
 * Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
 */

#include <stdio.h>
#include "sort.h"

int partition(int *data, int min, int max, drawfn_t drawfn)
{
	int pivot = data[(min + max) / 2], i = min - 1, j = max + 1;

	drawfn(data, (int[2]){(min + max) / 2, -1});

	for (;;) {
		while (data[++i] < pivot);
		while (data[--j] > pivot);
		if (i >= j) 
			return j;

		SWAP(data[i], data[j]);
		drawfn(data, (int[2]) {i, j});
	}
}

void _quicksort(int *data, int min, int max, drawfn_t drawfn)
{
	if (min < max) {
		int p = partition(data, min, max, drawfn);
		_quicksort(data, min, p, drawfn);
		_quicksort(data, p + 1, max, drawfn);
	}
}

void quicksort(int *data, int size, drawfn_t drawfn)
{
	_quicksort(data, 0, size - 1, drawfn);
}
