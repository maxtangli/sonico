#ifndef TESTS_SORT_H
#define TESTS_SORT_H

void assertArray(int* expected, int* result, int* origin, int n);
void testSort(int* origin, int n, void(*sort)(int* a, int n));
void testsSort(void(*sort)(int* a, int n));

#endif // TESTS_SORT_H