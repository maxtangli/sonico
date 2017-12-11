# docker

todo
- [x] install 0.5h
- [x] bug: synced folders not automatically sharing in centos7 1h
- [x] vagrant: multi-machine 1h
- [x] tutorial: get started. 2h

- [ ] know more.

overview
- docker: an open platform for developing, shipping, and running applications.
- impl: separate applications from infrastructure. deploy is same for develop and production. written in Go and use linux kernel features e.g. namespace such as pid, ipc, net, mnt, uts etc. to isolate; cgroups to limit resource; UnionFS to provide virtual filesystem for containers.
- usecase: fast, consistent delivery; responsive deployment and scaling; running more workloads on the same hardware.

docker engine
- cli client: docker command.
- rest api: talk to server.
- server: dockerd daemon process. responsible for create and manage docker objects e.g. image, container, network, volume.

# get started

install
- windows: docker <- hyper-v <- windows10 pro <- not free.
- centos: https://docs.docker.com/engine/installation/linux/docker-ce/centos/
- run without sudo: sudo usermod -aG docker $USER
- start on boot: sudo systemctl enable docker

bug: synced folders not automatically sharing in centos 7
- problem: https://github.com/hashicorp/vagrant/issues/7811
- solution: vagrant plugin install vagrant-vbguest -> use bento/centos-7.3 instead.

container: https://docs.docker.com/get-started/part2/
~~~~
# build&run
docker build -t friendlyhello .

docker run -p 80:80 friendlyhello

docker run -d -p 80:80 friendlyhello
docker container ls
docker container stop <Container NAME or ID>

docker container ls -a
docker container rm $(docker container ls -a -q)

docker image ls -a
docker image rm $(docker image ls -a -q)

# share
docker login

docker tag friendlyhello maxtangli/get-started:part2
docker images

docker push maxtangli/get-started:part2
docker run -p 80:80 maxtangli/get-started:part2
~~~~

service
- https://docs.docker.com/get-started/part3/
- task: a single container running in a service.
- service: composition of tasks to serve a goal.
~~~~
docker swarm init

vim docker-compose.yml
docker stack deploy -c docker-compose.yml getstartedlab

docker service ls
docker service ps getstartedlab_web
curl -4 http://localhost

docker stack rm getstartedlab

docker swarm leave --force
~~~~

swarm
- https://docs.docker.com/get-started/part4/
- swarm: a group of machines that are running Docker and joined into a cluster.
- swarm manager: the only machine in a swarm to execute docker command.
- swarm manager's strategies to run containers: emptiest node, global etc.
~~~~
#install VirtualBox
#see https://wiki.centos.org/HowTos/Virtualization/VirtualBox
sudo yum install wget
cd /etc/yum.repos.d
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
sudo yum install VirtualBox-5.2
# ... 5min passed
sudo usermod -a -G vboxusers vagrant
# VirtualBox inside VirtualBox wont work

docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls

docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"
docker-machine ssh myvm2 "docker swarm join --token <token> <ip>:2377"
docker-machine ssh myvm1 "docker node ls"

docker-machine env myvm1
eval $(docker-machine env myvm1)
docker-machine ls

docker stack deploy -c docker-compose.yml getstartedlab
docker stack ps getstartedlab

docker stack rm getstartedlab
eval $(docker-machine env -u)
~~~~

stack
- stack: a group of interrelated services that share dependencies, and can be orchestrated and scaled together.
~~~~
vim docker-compose.yml
docker stack deploy -c docker-compose.yml getstartedlab
docker service ls
~~~~

network
- network: a natural way to isolate containers from other containers or other networks.
- default network: bridge.
~~~~
docker network ls
docker run -itd --name=networktest ubuntu
~~~~

commands
- run install softwares and create new image layer
- cmd set a default cmd, may ignored
- entrypoint not ignored 