#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>
int main() {
 // 0,1,2,16
 printf("%d,%d,%d,%d\n",STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO, FOPEN_MAX);

 int fd = open("file.txt", O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
 if (fd == -1) {
   // may failed by permission denied without proper mode setting.
   printf("failed open. %s\n", strerror(errno));  
   return 1;
 }
 
 off_t currpos = lseek(fd, 0, SEEK_CUR);
 printf("currpos: %d\n", currpos);

 int ret = close(fd);
 if (ret == -1) {
   printf("failed close. %s\n", strerror(errno));
   return -1;
 }

 printf("done!\n");
 return 0;
}
