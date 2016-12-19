/*
A practice for divide and conquer by implementing merge sort.
*/
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <assert.h>
# include "testsSort.h"

/*
mergesort

algorithm: mergesort(a[1...n])
if (n <= 1) return a;
else return merge(mergesort(a[1...n/2]), mergesort(a[n/2+1...n]))

algorithm: merge(a[1...na], b[1...nb])
if (na == 0) return b;
elseif (nb == 0) return a;
elseif (a[1] <= b[1]) return a[1].merge(a[2...na], b[1...nb]);
elseif return b[1].merge(a[1...na], b[2...nb]);

example: 1,3,2,5,4
1,3 2,5,4
1 3 2 5,4
1 3 2 5 4
1,3 2 4,5
1,3 2,4,5
1,2,3,4,5
*/

void merge(int* a, int na, int* b, int nb, int* result) {
    assert(! (na == 0 && nb ==0));
    
    if (na == 0) {
        memcpy(result, b, nb * sizeof(int));
    } else if (nb == 0) {
        memcpy(result, a, na * sizeof(int));
    } else if (a[0] <= b[0]) {
        result[0] = a[0];
        merge(a + 1, na - 1, b, nb, result + 1);
    } else {
        result[0] = b[0];
        merge(a, na, b + 1, nb - 1, result + 1);
    }
}

void mergesort(int* a, int n) {
    if (n <= 1) return;
    
    int na = n / 2;
    int* b = a + na, nb = n - na;
    mergesort(a, na);
    mergesort(b, nb);
    
    int result[n];
    merge(a, na, b, nb, result);
    memcpy(a, result, n * sizeof(int));
}

int main() {
    testsSort(mergesort);
}