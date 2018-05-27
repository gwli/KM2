mkdir mongo_db
docker run --name mongo   -v `pwd`/mongo_db:/data/db -p 27017:27017 -d  mongo --dbpath /data/db
