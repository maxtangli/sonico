/*
A practice for divide and conquer by implementing merge-sort.
*/
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <assert.h>

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
    int* b = a + na;
    int nb = n - na;
    mergesort(a, na);
    mergesort(b, nb);
    
    int result[n];
    merge(a, na, b, nb, result);
    memcpy(a, result, n * sizeof(int));
}

void debugArray(int* a, int n) {
    for (int i=0; i<n; ++i) printf("%d,",a[i]);
    puts("");
}

void assertArray(int* expected, int* result, int n) {
    if (memcmp(expected, result, n) != 0) {
        printf("failed: expected[");
        for (int i=0; i<n; ++i) printf("%d,", expected[i]);
        printf("] but result[");
        for (int i=0; i<n; ++i) printf("%d,", result[i]);
        puts("]");
    } else {
        puts("ok");
    }
}

int compare_ints(const void* a, const void* b)
{
    int arg1 = *(const int*)a, arg2 = *(const int*)b;
    return (arg1 > arg2) - (arg1 < arg2);
}

void testMergesort(int* origin, int n) {    
    int expected[n];
    memcpy(expected, origin, n * sizeof(int));
    qsort(expected, n, sizeof(int), compare_ints);
    
    mergesort(origin, n);
    assertArray(expected, origin, n);
}

void testsMergeSort() {
    testMergesort((int[]){1}, 1);
    testMergesort((int[]){1,2}, 2);
    testMergesort((int[]){2,1}, 2);
    testMergesort((int[]){1,2,3}, 3);
    testMergesort((int[]){1,3,2}, 3);
    testMergesort((int[]){2,1,3}, 3);
    testMergesort((int[]){2,3,1}, 3);
    testMergesort((int[]){3,1,2}, 3);
    testMergesort((int[]){3,2,1}, 3);
    testMergesort((int[]){2,4,1,3}, 4);
    testMergesort((int[]){2,4,1,5,3}, 5);
    testMergesort((int[]){2,1,3,5,4,6}, 6);
}

void testMerge(int* expected, int* a, int na, int* b, int nb) {
    int result[na + nb];
    merge(a, na, b, nb, result);
    assertArray(expected, result, na + nb);
}

void testsMerge() {
    testMerge((int[]){1,2,3,4,5,6}, (int[]){1,2,3}, 3, (int[]){4,5,6}, 3);
}

int main() {
    testsMergeSort();
}