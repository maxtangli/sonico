#/bin/sh
docker stop $(docker ps -a -q -f ancestor=maxtangli/dockerize) > /dev/null

cid=$(docker run -p 5277:8080 -d maxtangli/dockerize)
docker ps
sleep 1

echo
curl localhost:5277
echo

docker stop $cid
docker ps