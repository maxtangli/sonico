# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "testsSort.h"

void printArray(int* a, int n) {
    for (int i=0; i<n; ++i) printf("%d,", a[i]);
}

void assertArray(int* expected, int* result, int* origin, int n) {
    if (memcmp(expected, result, n) != 0) {
        printf("failed: expected[");
        printArray(expected, n);
        printf("] but result[");
        printArray(result, n);
        printf("] in origin[");
        printArray(origin, n);
        puts("].");
    } else {
        puts("ok");
    }
}

int compare_ints(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

void testSort(int* origin, int n, void(*sort)(int* a, int n)) {    
    int backup[n], expected[n];
    memcpy(backup, origin, n * sizeof(int));
    memcpy(expected, origin, n * sizeof(int));
    qsort(expected, n, sizeof(int), compare_ints);
    
    sort(origin, n);
    assertArray(expected, origin, backup, n);
}

void testsSort(void(*sort)(int* a, int n)) {
    testSort((int[]){1}, 1, sort);
    testSort((int[]){1,2}, 2, sort);
    testSort((int[]){2,1}, 2, sort);
    testSort((int[]){1,2,3}, 3, sort);
    testSort((int[]){1,3,2}, 3, sort);
    testSort((int[]){2,1,3}, 3, sort);
    testSort((int[]){2,3,1}, 3, sort);
    testSort((int[]){3,1,2}, 3, sort);
    testSort((int[]){3,2,1}, 3, sort);
    testSort((int[]){1,2,3,4}, 4, sort);
    testSort((int[]){1,2,4,3}, 4, sort);
    testSort((int[]){1,3,2,4}, 4, sort);
    testSort((int[]){1,3,4,2}, 4, sort);
    testSort((int[]){1,4,2,3}, 4, sort);
    testSort((int[]){1,4,3,2}, 4, sort);
    testSort((int[]){2,4,1,5,3}, 5, sort);
    testSort((int[]){2,1,3,5,4,6}, 6, sort);
}