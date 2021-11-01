from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["test"]
collections = db["person"]

# collections.insert_one({"nickname":"dkryu3", "email":"dkryu3@v-go.io"})

result_list = collections.find().sort("nickname", -1)

for result in result_list:
    print(result)

