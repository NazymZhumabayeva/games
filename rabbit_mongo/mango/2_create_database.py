import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]

print(client.list_database_names())

dblist = client.list_database_names()

if "mydatabase" in dblist:
    print("The database exist.")