import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "students" in collist:
    print("The collection exists.")