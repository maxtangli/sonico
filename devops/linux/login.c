#include <stdio.h>

int main() {
  // BSD login
  // - pid0 swapper: process schedule.
  // - pid1 /sbin/init: boot linux.
  // - init: foreach config in  /etc/ttys, fork. handle SIGCHLD: fork.
  // - init child: exec getty.
  // - getty: open-rw terminal. when user connected, redirect fd 0,1,2, user input username, execle(/bin/login, -p username...).
  // - login: handle password by getpwnam(), getpass(), crypt(), pw_passwd, exit(1) if failed.

  // linux login
  // - e.g. /etc/inittab, /etc/*.conf. 

  // BSD network login
  // - init: sh /etc/rc
  // - /etc/rc: after processing, inetd's parent is init.
  // - inetd: if connected, fork and exec xx e.g. telnetd.

  puts("fork exec to login!");  
  return 0;
}
