#include <stdio.h>
#include <unistd.h>
#include <sys/select.h>
int main() {
  // blocking io
  // - read empty-data file: e.g. pipe, terminal, network.
  // - write full-data file: e.g. pipe, network.
  // - open specify file: e.g. terminal, FIFO.
  // - read/write file with record locking=byte-range locking.
  // - some ioctl() functions.
  // - some process communication functions.
  // ...

  // non-blocking io
  // 1. open(O_NONBLOCK), open + fcntl(O_NONBLOCK) -> polling: cons. cpu costly.
  // 2. multi thread, block io thread: cons. complex.

  // io multiplexing: pros. support multiple io efficiently.
  // 1. select, pselect
  fd_set readset, writeset;
  FD_ZERO(&readset);
  FD_ZERO(&writeset);
  FD_SET(0, &readset);
  FD_SET(1, &writeset);
  FD_SET(2, &writeset);
  int maxfdpl = 4; // max=FD_SETSIZE
  // select return: ready fd count >=0. -1 if error.
  int select_ret = select(maxfdpl, &readset, &writeset, NULL, NULL);
  printf("select return %d,isset(%d,%d,%d).\n", select_ret, 
      FD_ISSET(0, &readset), FD_ISSET(1, &writeset), FD_ISSET(2, &writeset));
  // pselect: support ns instead of ms. support sigmast.
  
  return 0;
}
