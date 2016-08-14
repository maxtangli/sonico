/*
A practice for divide and conquer by implementing quick sort.
*/
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <assert.h>
# include "testsSort.h"

/*
algorithm: quickSort(a[1...n])

if n <= 1, return;

iPivot = partition(a[1...n]);
quickSort(a[1...iPivot-1]);
quickSort(a[iPivot+1...n]);

algorithm: partition(a[1...n])

see code.

*/

void swap(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int* a, int n) {
    assert(n >= 2);
    
    int *p = a;
    swap(p, a + n / 2);
    
    int *l = p + 1, *r = a + n - 1;
    while (1) {
        while (l != r && *l <= *p) ++l;
        while (l != r && *r > *p) --r;
        if (l != r) swap(l, r);
        else {
            int* m = *l <= *p ? l: l - 1;
            swap(m, p);
            
            int ln = m - a;
            return ln;
        }
    }    
}

// shorter code but more swap times
int partition_short(int* a, int n) {
    assert(n >= 2);
    
    swap(a, a + n / 2);
    int *p = a, pivot = a[0], *r = a + n - 1;
    for (int *i = a + 1; i <= r; ++i) {
        // invariant: a[1]...*p <= pe < *(p+1) ... *i
        if (*i < pivot) swap(++p, i); // note: equal elements are free to belong to left or right
    }
    swap(p, a);
    
    int ln = p - a;
    return ln;
}

void quickSort(int* a, int n) {
    if (n <= 1) return;
    
    int ln = partition_short(a, n), *l = a;
    int rn = n - 1 - ln, *r = a + n - rn;
    quickSort(l, ln);
    quickSort(r, rn);
}

// http://stackoverflow.com/questions/19437135/internal-implementation-of-qsort
// a possible implementation in K&R second edition, section 5.11, page 120
/*
void qsort(void *v[], int left, int right, int (*comp)(void *, void *)) {
    int i, last;
    void swap(void *v[], int, int);

    if (left >= right)
        return;
    swap(v, left, (left + right)/2);
    last = left;
    for (i = left+1; i <= right; i++)
        if ((*comp)(v[i], v[left]) < 0) // Here's the function call
            swap(v, ++last, i);
    swap(v, left, last);
    qsort(v, left, last-1, comp);
    qsort(v, last+1, right, comp);
}
*/

int main() {
    testsSort(quickSort);
}