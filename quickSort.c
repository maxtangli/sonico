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
    
    int *p = a + n - 1;
    int *l = a, *r = p - 1;
    while (1) {
        while (l != r && *l <= *p) ++l;
        while (l != r && *r > *p) --r;
        if (l != r) swap(l, r);
        else {
            int* m = *l <= *p ? l + 1 : l;
            swap(m, p);
            
            int ln = m - a;
            return ln;
        }
    }    
}

void quickSort(int* a, int n) {
    if (n <= 1) return;
    
    int ln = partition(a, n), *l = a;
    int rn = n - 1 - ln, *r = a + rn;
    quickSort(l, ln);
    quickSort(r, rn);
}

int main() {
    testsSort(quickSort);
}