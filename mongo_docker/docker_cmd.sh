sudo rm -fr mongo_db
mkdir mongo_db
#docker run --name mongo   -v `pwd`/mongo_db:/data/db -p 27017:27017 -d  mongo --dbpath /data/db
#docker run --name mongo -v /my/custom:/etc/mongo -d mongo --config /etc/mongo/mongod.conf
docker rm -f mongodb
docker run -d --name mongodb  -v `pwd`/mongo_db:/data/db -p 27017:27017  -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=root mongo --dbpath /data/db
