#include <unistd.h>
#include <string.h>
int main() {
 char* s = "hello, linux!";
 write(1,s,strlen(s));
}
