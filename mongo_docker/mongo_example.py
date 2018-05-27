from pymongo import MongoClient

def test2():
    client = MongoClient('10.19.226.116',27017,
                      username='neo',
                      password='victor@mongo',
                      authMechanism='SCRAM-SHA-1',
                      authSource='questions')
    #db = client.get_database()
    db = client['questions']
    print(db.name)


def test1():
   uri = "mongodb://user:password@example.com/the_database?authMechanism=MONGODB-CR"
   client = MongoClient(uri)


test2()
