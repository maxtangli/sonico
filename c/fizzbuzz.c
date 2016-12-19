/*
A search for interesting implementations of Fizz-Buzz.
*/
#include <stdio.h>

// https://github.com/Keith-S-Thompson/fizzbuzz-c/blob/master/fizzbuzz07.c
/*
#include <stdio.h>
int main(void) {
    for (int i = 1; i <= 100; i ++) {
        !(i%15) && puts("FizzBuzz") ||
        !(i%3)  && puts("Fizz") ||
        !(i%5)  && puts("Buzz") ||
        printf("%d\n", i);
    }
}
*/

// https://github.com/Keith-S-Thompson/fizzbuzz-c/blob/master/fizzbuzz42.c
/*
#include <stdio.h>
int main(void) {
    for (int i = 1; i <= 100; i ++) {
        printf(printf("%s%s",
                      i%3 ? "" : "Fizz",
                      i%5 ? "" : "Buzz") ? "\n" : "%d\n", i);
    }
}
*/

// https://github.com/Keith-S-Thompson/fizzbuzz-c/blob/master/fizzbuzz62.c
/*
#include <stdio.h>
int main(void) {
    for (int i = 1; i <= 100; i ++) {
        printf(i % 15 == 0 ? "FizzBuzz\n" :
               i %  3 == 0 ? "Fizz\n" :
               i %  5 == 0 ? "Buzz\n" :
                             "%d\n",
               i);
    }
}
*/

// https://github.com/Keith-S-Thompson/fizzbuzz-c/blob/master/fizzbuzz72.c
/*
#include <stdio.h>
#define I printf("%d\n",i++);
#define F puts("Fizz");i++;
#define B puts("Buzz");i++;
#define Z puts("FizzBuzz");i++;
#define S s:
int main(void) {
    int i = 1;
    goto s;
    do { I F I I Z S I I F I B F I I F B } while (i < 100);
}
*/

// https://github.com/Keith-S-Thompson/fizzbuzz-c/blob/master/fizzbuzz78.c
/*
#include <stdio.h>
#include <stdint.h>
int main(void) {
    for(uint16_t i=18561;(i&127)<=100;i+=18561)(i&49152)==49152&&(i&=~
    49152),(i&14336)==10240&&(i&=~14336),(i&1920)==1920&&(i&=~1920),(!
    (i&1920))&&puts("FizzBuzz")||(!(i&49152))&&puts("Fizz")||(!(i&14336
    ))&&puts("Buzz")||printf("%u\n",i&127);
}
*/

// http://perl.guru.org/scott/misc/golf.html
/*
main(i){for(;i<101;puts(i++%5?"":"Buzz"))printf(i%3?i%5?"%d":"":"Fizz",i);}
*/

// http://ask.metafilter.com/198838/How-is-it-possible-to-write-fizzbuzz-in-73-bytes-of-C
// note: only work if the four bytes preceding the "Buzz" string are all zeroes
/*
main(i){for(;i<101;puts("Buzz"-i*i++%5))printf(i%3?i%5?"%d":0:"Fizz",i);}
*/

// my version. criterion: easy understanding > simple > short > performance.
void fizzbuzz(int n) {
    for (int i=1; i<=n; ++i) {
        if (i%3&&i%5) printf("%d",i);
        if (i%3==0) printf("Fizz");
        if (i%5==0) printf("Buzz");
        printf(",");
    }
}

// expected output: 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz
int main() {
    fizzbuzz(15);
}