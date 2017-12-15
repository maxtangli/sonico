#/bin/sh
src=${1:-main.js}

cp package.json.bak package.json
sed -i -- "s/main.js/$src/g" package.json
docker build -t maxtangli/workspace .

docker run -p 5277:5277 maxtangli/workspace

cp package.json.bak package.json
