#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>

// since filesystem read ahead, small buf_size won't be slow
#define BUF_SIZE 32

int main() {
 // 0,1,2,16
 printf("%d,%d,%d,%d\n",STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO, FOPEN_MAX);

 int fd = open("file.txt", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
 if (fd == -1) {
   // may failed by permission denied without proper mode setting.
   printf("failed open. %s\n", strerror(errno));  
   return 1;
 }
 
 off_t currpos = lseek(fd, 0, SEEK_CUR);
 printf("currpos: %d\n", currpos);

 char buf[BUF_SIZE] = "hello, linux!";
 // delayed write: fd(data) in buffer -> write queue
 ssize_t write_bytes = write(fd, buf, sizeof(buf));
 if (write_bytes == -1) {
  printf("failed write. %s\n", strerror(errno));
  return 1;
 }

 // buffer -> write queue
 sync();
 // like O_SYNC. fd(data+properties) in buffer -> write queue -> disk
 fsync(fd);
 // like O_RSYNC. fd(data) in buffer -> write queue -> disk
 fdatasync(fd); 

 // use fcntl(), ioctl() to control fd.

 memset(buf, 0, sizeof(buf));
 lseek(fd, 0, SEEK_SET);
 ssize_t read_bytes = read(fd, buf, write_bytes);
 if (read_bytes == -1 || read_bytes != write_bytes) {
  printf("failed read. %s\n", strerror(errno));
  return 1;
 }
 printf("%s\n", buf);

 int ret = close(fd);
 if (ret == -1) {
   printf("failed close. %s\n", strerror(errno));
   return 1;
 }

 printf("done!\n");
 return 0;
}
