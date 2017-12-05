# docker

todo
- [x] install 0.5h
- [x] bug: synced folders not automatically sharing in centos7 1h
- [ ] tutorial 0.5h

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
- 
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

commands
- run install softwares and create new image layer
- cmd set a default cmd, may ignored
- entrypoint not ignored 