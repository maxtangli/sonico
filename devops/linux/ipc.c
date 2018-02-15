#include <stdio.h>
#include <unistd.h>

int main() {
  // pipe: oldest. cons. maybe half-duplex, for parent&child process only.
  int fd[2]; // read fd, write fd.
  if (pipe(fd) < 0) {
    perror("failed pipe.");
    return 1;
  }
  pid_t pid = fork();
  if (pid < 0) {
    perror("failed fork.");
    return 1;
  } else if (pid > 0) {
    close(fd[0]);
    sleep(1);
    // if bytes > PIPE_BUF, may overwrite other process's pipe.
    // if no read fd opened, raise SIGPIPE, return -1 and errno=EPIPE.
    int write_ret = write(fd[1], "hello sonico!", 12);
    printf("write return %d.\n", write_ret);
  } else {
    close(fd[1]);
    char line[12];
    // blocking if no contents but any child process'fd opened.
    int n = read(fd[0], line, 200);
    printf("read return %d, %s.\n", n, line);
  
    // return 0 if no contents and no write fd opened.
    n = read(fd[0], line, 200);
    printf("read return %d, %s.\n", n, line);

    // popen: fork, exec, return FILE* for io.
    FILE* fpin = popen("echo \"hello sonico!\"", "r");
    while (fgets(line, 200, fpin) != NULL) {
      printf("fgets: %s\n", line);
    }
  }

  // coprocess
  
  // FIFO: naming pipe sharable by any processes.

  // XSI IPC
  // - message queue: not recommend, use pipe instead which is same fast.
  // - semaphore: not recommend, user record lock instead which is simpler.
  // - shared memory: cons. fastest. may use mmap instead.

  // unix domain socket
  
  return 0;
}
