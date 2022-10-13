import pymongo
client = pymongo.MongoClient("mongodb+srv://sumanth:root@cluster0.dp4u70c.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "sumanth",
    "email" : "sumanthgupta548@gmail.com",
    "surname" :  "racherla"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)