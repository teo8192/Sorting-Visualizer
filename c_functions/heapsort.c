// Application files
#include "sort.h"

#define iLeftChild(x) (2 * (x) + 1)
#define iRightChild(x) (2 * (x) + 2)
#define iParent(x) (((x) - 1) / 2)

static void sift_down(int *data, int start, int end, drawfn_t drawfn)
{
	int root = start;

	while(iLeftChild(root) <= end) {
		int child = iLeftChild(root);
		int swap = root;

		if (data[swap] < data[child])
			swap = child;
		if (child + 1 <= end && data[swap] < data[child + 1])
			swap = child + 1;
		if (swap == root)
			return;
		else {
			SWAP(data[root], data[swap]);
			drawfn(data);
			root = swap;
		}
	}
}

static void heapify(int *data, int size, drawfn_t drawfn)
{
	for (int start = iParent(size - 1); start >= 0; --start)
		sift_down(data, start, size - 1, drawfn);
}

void heapsort(int *data, int size, drawfn_t drawfn)
{
	heapify(data, size, drawfn);

	int end = size - 1;
	while (end > 0) {
		SWAP(data[end], data[0]);
		end--;
		sift_down(data, 0, end, drawfn);
	}
}
