import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]
#1
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)

#2
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)
