/*
A practice for divide and conquer by implementing nth-minimum.
*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

/*
algorithm: min(a[1...n], nth)

pivot = a[rand];
split a into 3 groups by pivot: l[1...ln], m[1...mn], r[1...rn].

if nth <= ln, return min(l[1...ln], nth);
else if nth <= ln + mn, return pivot;
else return min(r[1...rn], nth - ln - mn);

*/

int min(int* a, int n, int nth) {
    assert(1 <= nth && nth <= n);
    
    int l[n], m[n], r[n], ln = 0, mn = 0, rn = 0;
    
    int pivot = a[0];
    for (int i = 0; i < n; ++i) {
        int elem = a[i];
        if (elem < pivot) l[ln++] = elem;
        else if (elem == pivot) m[mn++] = elem;
        else r[rn++] = elem;
    }
    
    if (nth <= ln) return min(l, ln, nth);
    else if (nth <= ln + mn) return pivot;
    else return min(r, rn, nth - ln - mn);
}

int compare_ints(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void test(int* a, int n) {
    int b[n];
    memcpy(b, a, n * sizeof(int));
    qsort(b, n, sizeof(int), compare_ints);
    
    for (int nth = 1; nth <= n; ++nth) {
        int expected = b[nth-1];
        int actual = min(a, n, nth);
        if (expected == actual) puts("OK");
        else {
            printf("failed: expected %d but actual %d in [", expected, actual);
            for(int i=0; i<n; ++i) printf("%d,", a[i]);
            puts("].");
        }
    }
    
}

void tests() {
    test((int[]){1}, 1);
    test((int[]){1,2}, 2);
    test((int[]){5,1,7,3,9,2,8,4,6}, 9);
}

int main() {
    tests();
}