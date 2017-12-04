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

https://docs.docker.com/get-started/part2/
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

https://docs.docker.com/get-started/part3/#introduction
~~~~
~~~~

commands
- run install softwares and create new image layer
- cmd set a default cmd, may ignored
- entrypoint not ignored 