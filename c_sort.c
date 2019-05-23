/*
 * Author: Teodor Dahl Knutsen <teodor@dahlknutsen.no>
 */

#include <stdio.h>

#include "c_functions/sort.h"

void sort(int *data, int size, drawfn_t drawfn)
{
	//heapsort(data, size, drawfn);
	//quicksort(data, size, drawfn);
	lomuto(data, size, drawfn);

	// DO NOT REMOVE, NEEDS TO BE HERE!
	// This will set the data in the python object 
	// to the correct value
	drawfn(data);
}

