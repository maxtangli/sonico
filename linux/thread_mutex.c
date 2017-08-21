#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>

// mutex init: static case.
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
int shared = 0;

void shared_plus(bool use_lock) {
  if (!use_lock) {
    if (shared == 0) ++shared;
    return;
  }

  // blocking until lock ok.
  // for non-blocking case, use pthread_mutex_trylock().
  // for limited time blocking case, use pthread_mutex_timedlock().
  // for shared-exclusive case, use rwlock functions e.g. rdlock, wrlock.
  if (pthread_mutex_lock(&lock) != 0) {
    puts("failed pthread_mutex_lock.");
    exit(1);
  }
  if (shared == 0) ++shared;
  if (pthread_mutex_unlock(&lock) != 0) {
    puts("failed pthread_mutex_unlock.");
    exit(1);
  }

  // deadlock
  // - avoid: lock by same sequence.
  // - cancel: if trylock() failed, release all locks. 
}

void thr_print(const char* s) {
  shared_plus(true);
  printf("hey I'm %s thread, my tid is [%d], shared[%d].\n", s, pthread_self(), shared);
}

void* thr_fn(void* arg) {
  thr_print("child");
  return ((void*)0);
}

int main() {
  // mutex init: dynamic case.
  if (pthread_mutex_init(&lock, NULL) != 0) {
    puts("failed pthread_mutex_init.");
    return 1;
  }

  pthread_t child_tid;
  int create_ret = pthread_create(&child_tid, NULL, thr_fn, NULL);
  if (create_ret != 0) {
    puts("failed pthread_create.");
    return 1; 
  }

  thr_print("control");
  sleep(1);

  if (pthread_mutex_destroy(&lock) != 0) {
    puts("failed pthread_mutex_destroy.");
    return 1;
  }

  return 0; 
}
