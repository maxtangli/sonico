# linux

0. setup env, hello. 1h

# note: vim

~~~~
:scriptnames // list .vim files loaded, including .vimrc
:verbose map <F5>

~/.vimrc
map <F5> :w<CR>:!gcc % && ./a.out;rm a.out<CR>
~~~~
