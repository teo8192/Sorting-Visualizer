#ifndef __SORT_H_
#define __SORT_H_

#define SWAP(a,b) ((&(a) == &(b)) ? (a) : ((a)^=(b),(b)^=(a),(a)^=(b)))

typedef int(*drawfn_t)(int*);
typedef void(*sortfunc_t)(int*, int, drawfn_t);

void bubblesort(int *data, int size, drawfn_t drawfn);
void insertion_sort(int *data, int size, drawfn_t drawfn);
void selection_sort(int *data, int size, drawfn_t drawfn);
void mergesort(int *data, int size, drawfn_t drawfn);
void heapsort(int *data, int size, drawfn_t drawfn);
void quicksort(int *data, int size, drawfn_t drawfn);

void lomuto(int *data, int size, drawfn_t drawfn);

#endif
