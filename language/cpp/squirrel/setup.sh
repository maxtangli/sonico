#!/bin/sh
wget https://downloads.sourceforge.net/project/squirrel/squirrel3/squirrel%203.1%20stable/squirrel_3_1_stable.tar.gz
tar xvzf squirrel_3_1_stable.tar.gz
cd squirrel3
make sq64

cd ..
ln -s squirrel3/bin/sq sq
echo 'print("hello, squirrel!")' > hello.cnut
./sq hello.cnut
