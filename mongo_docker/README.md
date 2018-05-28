structure 
=========

DB->connection->dom.

https://www.tutorialspoint.com/mongodb/mongodb_gridfs.htm


#. Create db. 

docker run -d --name mongodb  -v `pwd`/mongo_db:/data/db -p 27017:27017  -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=root mongo --dbpath /data/db


#. connect 

mongo -u mongoadmin -u root --authenticationDatabase admin
```

```

#. insert

restrict on local ip

```
add the the following line in the mongodb.conf
bind ip = 127.0.0.1
```


#. mongo udemy example  https://github.com/StephenGrider/MongoCasts


#. mining tools

https://github.com/selvinsource/mongodb-datamining-shell
