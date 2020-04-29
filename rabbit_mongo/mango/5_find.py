import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]

x = mycol.find_one()
print(x)

#for finding all objects

students = mycol.find()

for x in students:
    print(x) #output all objects
    print(x['name']) #output names

students = mycol.find({}, {"_id": 0, "name": 1, "address": 1})    #without ids 
for x in students:
    print(x) 