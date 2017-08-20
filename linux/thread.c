#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
void thr_print(const char* s) {
  printf("hey I'm %s thread, my tid is [%d].\n", s, pthread_self());
}

void thr_cleanup(void* arg) {
  thr_print((const char*)arg);
}

void* thr_fn(void* arg) {
  pthread_cleanup_push(thr_cleanup, "child cleanup");

  sleep(1);
  thr_print("child");
  
  pthread_cleanup_pop(0);
  // pthread_exit(0);
  return ((void*)0);
}

int main() {
  // thread pros.
  // - easy event handling by assigning each asyn event to a thread.
  // - easy memory and fd share.
  // - better throughput for dividable task.
  // - better response time for interactive task. 

  pthread_t child_tid; // child thread may run before pthread_create() returns.
  int create_ret = pthread_create(&child_tid, NULL, thr_fn, NULL);
  if (create_ret != 0) {
    puts("failed pthread_create.");
    return 1; 
  }

  // force thread exit.
  int cancel_ret = pthread_cancel(child_tid);
  if (cancel_ret != 0) {
    puts("failed cancel_ret.");
    return 1;
  }
 
  thr_print("control");

  // blocking until specified thread returns.
  int join_ret = pthread_join(child_tid, NULL);
  if (join_ret != 0) {
    puts("failed pthread_join.");
    return 1;
  }
  //sleep(1);
 
  return 0; // when control thread return, all child thread end.
}
