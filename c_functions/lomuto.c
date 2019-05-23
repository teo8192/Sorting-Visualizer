#include "sort.h"
#include <pthread.h>
#include <stdio.h>

//#define MIN_ELEM_THREAD 100000
#define MAX_THREAD 16

int MIN_ELEM_THREAD = 100000;

typedef struct Arg {
	int *data, min, max;
	drawfn_t drawfn;
} Arg_t;

static void _quicksort(int *data, int min, int max, drawfn_t drawfn);

/* Select pivot and partition data */
static int partition(int *data, int min, int max, drawfn_t drawfn)
{
	static pthread_mutex_t mutex_lock;
	int i = min;

	for (int j = min; j < max; ++j)
		if (data[j] < data[max]) {
			SWAP(data[i], data[j]);

			if (i % 2 == 0) {
				pthread_mutex_lock(&mutex_lock);
				drawfn(data, (int[2]){i, j});
				pthread_mutex_unlock(&mutex_lock);
			}
			++i;
		}

	SWAP(data[i], data[max]);

	/*pthread_mutex_lock(&mutex_lock);*/
	/*drawfn(data);*/
	/*pthread_mutex_unlock(&mutex_lock);*/
	return i;
}

/* Recursive quicksort algorithm */
static void _quicksort(int *data, int min, int max, drawfn_t drawfn)
{
	if (min < max) {
		int p = partition(data, min, max, drawfn);
		_quicksort(data, min, p-1, drawfn);
		_quicksort(data, p+1, max, drawfn);
	}
}

static void *_quicksort_mth(Arg_t *arg)
{
	static pthread_mutex_t mutex_lock;
	static int num_thread = 1;
	pthread_t second;

	if (arg->min < arg->max) {
		int p = partition(arg->data, arg->min, arg->max, arg->drawfn);

		if (arg->max - arg->min < MIN_ELEM_THREAD) {
			_quicksort(arg->data, arg->min, p-1, arg->drawfn);
			_quicksort(arg->data, p+1, arg->max, arg->drawfn);
		} else if (num_thread > MAX_THREAD) {
			_quicksort_mth( &(Arg_t) { .data=arg->data, .min=arg->min, .max=p-1, .drawfn=arg->drawfn});
			_quicksort_mth(&(Arg_t) { .data=arg->data, .min=p+1, .max=arg->max, .drawfn=arg->drawfn});
		} else {
			pthread_mutex_lock(&mutex_lock);
			num_thread++;
			pthread_mutex_unlock(&mutex_lock);

			pthread_create(&second, NULL, (void*(*)(void*)) _quicksort_mth,
					&(Arg_t) { .data=arg->data, .min=arg->min, .max=p-1, .drawfn=arg->drawfn });

			_quicksort_mth(&(Arg_t) { .data=arg->data, .min=p+1, .max=arg->max, .drawfn=arg->drawfn});

			pthread_join(second, NULL);

			pthread_mutex_lock(&mutex_lock);
			num_thread--;
			pthread_mutex_unlock(&mutex_lock);
		}
	}
}

void lomuto(int *data, int size, drawfn_t drawfn)
{
	MIN_ELEM_THREAD = size >> 3;
	//_quicksort(data, 0, size - 1);
	_quicksort_mth(&(Arg_t) { .data=data, .min=0, .max=size - 1, .drawfn=drawfn });
}
