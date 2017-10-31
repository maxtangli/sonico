~~~~
gcc -g -Wall -o insert_sort ins.c # -g : save symbol table
gdb insert_sort -tui
run 12 5
list
next
step

break 20
break source/bed.c:35
break bed.c:parseArguments
info breakpoints
delete 1
clear 20
watch var # break when var changed

print var
disp var # automatically print when break
set var = val

info threads
thread 3
~~~~
