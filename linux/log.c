#include <syslog.h>
#include <stdio.h>

int main() {
  openlog("sonico", LOG_PERROR, LOG_USER);
  // generate log
  // - user process call syslog() to write log into /dev/log
  syslog(LOG_ERR, "example error message by %s.", "sonico");
  // - network send log into UDP 514
  // - kernel routine call log() to write log into /dev/klog

  // syslogd deamon read logs, configured by /etc/syslog.conf

  closelog();
}
