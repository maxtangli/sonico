#include <stdlib.h>
#include <stdio.h>
#include <signal.h>

void say_goodbye(){
  static int i = 0;
  // getenv(): return a pointer to internal string.
  printf("goodbye, %s's process! +%d\n", getenv("USER"), ++i);
}

void handle_abort(int param) {
  say_goodbye();
}

/*
memory layout, a logical example.
- heap<->stack
- bss: uninitialized data.
- data: intialized data.
- text: code. typically shared by processes.
*/

int main(int argc, char *argv[]) { 
  // register exit() callback stack.
  atexit(say_goodbye);
  atexit(say_goodbye);
  // register quick_exit() callback stack.
  at_quick_exit(say_goodbye);
  at_quick_exit(say_goodbye);
  // regis:qqqqqter ONE signal handler. 
  signal(SIGABRT, SIG_DFL);
  signal(SIGABRT, SIG_IGN);
  signal(SIGABRT, handle_abort);

  // cleanup and terminate process:
  // 1. destroy thread objects(c++11).
  // 2. destroy static objects(c++), invoke callbacks registered by atexit().
  // 3. flush and close c streams, remove tmpfile.
  // 4. return control to host env.
  //exit(0); // same with main return 0;

  // terminate process without normal cleanup:
  // 1. remove tmpfile.
  // 2. return control to host env.
  //_Exit(0);
  
  // terminate process without normal cleanup but custom callbacks.
  // 1. invoke callbacks registered by at_quick_exist(). 
  // 2. remove tmpfile.
  // 3. return control to host env.
  //quick_exit(0);

  // raise SIGABRT to terminate process without normal cleanuo.
  abort(); // same with raise(SIGABRT);

  puts("won't print this line.");
  return 0;
}

