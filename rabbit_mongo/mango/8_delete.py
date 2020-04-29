import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]
#1 delete one first document that we find
myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

for x in mycol.find():
    print(x) 

#2 delete all documents that started with s
myquery = {"address": {"$regex": "^S"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

#3 delete all documents in collection
x = mycol.delete_many({})