# know openmpi

0. setup 0.5h

# setup

~~~~
wget openmpi-3.0.0.tar.gz
tar xvzf openmpi-3.0.0.tar.gz

cd openmpi-3.0.0
./configure --prefix=/home/ec2-user/sonico/cpp/mpi/install
make all install

cd ..
cp openmpi-3.0.0/examples/hello_c.c ./
gcc hello_c.c -o hello -I install/include/ -Linstall/lib/ -l:libmpi.so

echo $LD_LIBRARY_PATH
export LD_LIBRARY_PATH=install/lib/
./hello
~~~~
