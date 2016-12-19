/*
A practice for dynamic programming by implementing knapsack.
*/
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <assert.h>
# include <math.h>

/*

algorithm: ukp(c, w[1...n], v[1...n])

return max i:wi<=c {ukp(c-wi)+vi}

algorithm: bkp()

TODO

algorithm: 01kp()

TODO

*/

int max(int x, int y) {
    return (int)fmax(x, y);
}

// unbounded knapsack problem 
// TODO pass selection result to int* s
int ukp(int c, int* w, int* v, int n) {
    int sv = 0;
    for (int i = 0; i < n; ++i) {
        if (w[i] <= c) 
            sv = max(sv, ukp(c - w[i], w, v, n) + v[i]);
    }
    return sv;
}

void testUkp(int expected, int c, int* w, int* v, int n) {
    int actual = ukp(c, w, v, n);
    if (actual != expected) {
        puts("Failed.");
    }
}

void tests() {
    // https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
    // P02 is a set of 5 weights and profits for a knapsack of capacity 26.
    // note that ukp and 01kp's solution is same for this dataset.
    testUkp(13+23+15, 26, (int[]){12,7,11,8,9}, (int[]){24,13,23,15,16}, 5);
    
    puts("tests() done.");
}

int main() {
    tests();
}