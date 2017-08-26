# Advanced Programming in the UNIX Environment, Third Edition

0. setup env, hello. 1h
1. file, io. 2.1h
2. process env. 1.1h
3. process control. 0.6h
4. BSD login. 1.2h
5. thread create. 1h
6. thread sync. 0.7h
7. log. 0.3h
8. io: select. 0.9h
9. io: poll. 0.5h
10. IPC: pipe etc. 1.3h
11. network IPC: socket.

# note: vim

~~~~
:scriptnames // list .vim files loaded, including .vimrc
:verbose map <F5>

~/.vimrc
map <F5> :w<CR>:!gcc pthread % && ./a.out;rm a.out<CR>
~~~~
