# Advanced Programming in the UNIX Environment, Third Edition

0. setup env, hello. 1h
1. file 0.8h

# note: vim

~~~~
:scriptnames // list .vim files loaded, including .vimrc
:verbose map <F5>

~/.vimrc
map <F5> :w<CR>:!gcc % && ./a.out;rm a.out<CR>
~~~~
