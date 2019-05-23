/*
 * Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
 */

#include <stdio.h>

#include "sort.h"

void sort(int *data, int size, drawfn_t drawfn)
{
	quicksort(data, size, drawfn);
}
