#include <unistd.h>
#include <stdio.h>

int main() {
  // pid
  // - pid0 swapper: process schedule.
  // - pid1 /sbin/init: boot linux.
  pid_t pid = getpid();
  printf("pid:%d\n",pid);

  // fork concepts
  // - child process: a copy of stack,heap,rss,bss, share data.
  // - COW=copy on write: create actual copy of the part when modification ocuurs. 
  // - sharing fd: difficult to sync.
  // fork usage
  // - copy self to execute different code. e.g. server fork a child process to handle request. 
  // - execute other program. e.g. shell fork a child process to call exec().
  pid_t fork_pid = fork();
  pid = getpid();
  if (fork_pid == -1) {
    // failed if
    // - too many process in system
    // - too many process for user(> CHILD_MAX)
    puts("failed to fork.");
    return 1;
  } else if (fork_pid > 0) {
    // sleep(1);
    printf("parent %d's child %d, parent %d.\n", pid, fork_pid, getppid());
  } else {
    // if child process terminated earlier, it becomes a zombie process, send SIGCHLD to parent(ignored by default handler, however).
    // if parent process terminated earlier, pid1=init becomes the next parent.
    // init will call wait() whenever a child process terminated, thus prevent zombie rush.
    printf("child %d's parent %d.\n", pid, getppid());
  }

  return 0;
}
