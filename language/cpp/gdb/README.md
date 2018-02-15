~~~~
gcc -g -Wall -o insert_sort ins.c # -g : save symbol table
gdb insert_sort -tui
run 12 5
gdb -tui --args insert_sort 12 5

list
where
info threads
thread 3

break 20
break source/bed.c:35
break bed.c:parseArguments
info break
disable 1
enable 1
delete 1
delete
clear 20

next
step
cont

watch var # break when var changed
print var
disp var # automatically print when break
set var = val
~~~~
