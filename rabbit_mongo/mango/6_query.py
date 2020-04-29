import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]
#1
query = {"name": "Nazym"}

students = mycol.find(query)

for x in students:
    print(x)
#2
#------adresses started with letters >=S
query = {"address": {"$gt": "S"}}
students = mycol.find(query)
for x in students:
    print(x)

#3
#-----addresses started with letter S
query = {"address": {"$regex": "^S"}} 
students = mycol.find(query) 
for x in students: 
    print(x)



