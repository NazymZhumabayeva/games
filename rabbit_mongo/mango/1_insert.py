import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-borrg.mongodb.net/test?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["students"]
mydict = {"name": "One", "surname": "Direction", "id": "2017"}

x = mycol.insert_one(mydict)

x.inserted_id