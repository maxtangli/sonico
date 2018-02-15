# know openmpi

0. setup 0.5h
1. know send,recv. 0.9h

# setup

~~~~
wget openmpi-3.0.0.tar.gz
tar xvzf openmpi-3.0.0.tar.gz

cd openmpi-3.0.0
./configure --prefix=/home/ec2-user/sonico/openmpi/install
make all install

cd ..
export PATH=$PATH:install/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:install/bin
mpicc hello_c.c -o hello
mpiexec -np 1 ./hello

# https://www.open-mpi.org/faq/?category=running#oversubscribing
echo localhost slots=4 > my-hostfile
mpirun -np 4 --hostfile my-hostfile ./hello
mpirun -np 4 --hostfile my-hostfile ./ring
mpirun -np 4 --hostfile my-hostfile ./connectivity
~~~~

# basics

https://htor.inf.ethz.ch/teaching/mpi_tutorials/ppopp13/2013-02-24-ppopp-mpi-basic.pdf

terms
- Group(default: MPI_COMM_WORLD) + color == communicator (it is like a name for the group)
- A process is identified by a unique number within each communicator, called rank
- Simple programs typically only use the predefined communicator MPI_COMM_WORLD
- MPICH is a high-performance and widely portable implementation of MPI.

core functions
- MPI_SEND(buf, count, datatype, dest, tag, comm)
- MPI_RECV(buf, count, datatype, source, tag, comm, status)
