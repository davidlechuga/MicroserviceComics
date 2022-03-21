# Components
from comics import comics

# Dependecies
from flask import Flask, jsonify, request
from marvel import Marvel
import pymongo

m = Marvel("e1e92c98c981a8d5792fc1301ede5bd6",
           "5bb1498bb8aec5c6431aa89ad243e7d3b1617e20")

characters = m.characters

x = 1011334


app = Flask(__name__)

for n in range(0, 6):

    # serach for comics of this character
    all_characters = characters.comics(x)

    x = x+1
    for i in range(1, 12):
        print(all_characters['data']['results'][int(i)]['title'])

url = "mongodb://localhost:27017/mydbname"
client = pymongo.MongoClient(url)
db = client['UserData']

coll = db.Users

if client:
    print("connected")
else:
    print("not connected")

# Single Value Insert ##
db.coll.insert_one({"foo": "bar"})

#x1 = col1.insert_one(Users)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Eli te amo <3 "})


@app.route('/comics')
def usersHandler():
    return jsonify({"comics": comics})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
