import pymongo
import datetime

# mongodb running in container on port 9999, mount a volume to persist data

# object using standard connection arguments
# client = pymongo.MongoClient("localhost", 9999)

client = pymongo.MongoClient('mongodb://localhost:9999')
db = client.testdb  # creating a db called testdb
users = db.users  # creating a collection called users

# inserting a document in the 'users' collection
user1 = {'username': 'kevinm', 'password': 'password1', 'favorite_number': 37,
         'hobbies': ['music', 'programming', 'martial_arts']}
user2 = {'username': 'kevinp', 'password': 'password1', 'favorite_number': 38,
         'hobbies': ['music', 'programming', 'martial_arts']}
user3 = {'username': 'kevino', 'password': 'password1', 'favorite_number': 39,
         'hobbies': ['music', 'programming', 'martial_arts']}

more_users = [user2, user3]


# this inserts the user1 document into the users collection
# also calls the inserted_id method so that we can get the mongo id for the document inserted
# can use Robo 3T (formerly robomongo as gui for mongodb)
user_id = users.insert_one(user1).inserted_id
#print(user_id)

# this inserts multiple user documents (no need for a for loop)
users.insert_many(more_users)

# tell you how many documents you have in the users collection
print(users.find().count())

# tell you have many documents contain a k,v pair with favorite_number is 39 in the users collection
print(users.find({'favorite_number': 39}).count())

# great use case for count is making sure someone isn't trying to sign up with an already taken username
# so if users.find({'username': user_input}).count() > 0: reject ....

# using multiple conditions when performing a find (eg fav num is 39 AND username is kevino)
# if users.find({'username': 'kevino'}, {'favorite_number': 39}): do something

current_time = datetime.datetime.now()

# so now when you insert a document you can include a timestamp
users.insert_one({'username': 'chaka', 'date': current_time})

# so now you can use operators to find documents using various calculations of the current_time
# eg show me posts that were created over the past 30 days
thirty_day_delta = datetime.timedelta(days=30)
thirty_days_ago = current_time - thirty_day_delta

# finding posts/documents created 30 days or less in the past
print(users.find({'date': {'$gte': thirty_days_ago}}).count())
# $gt == greater than, $gte == greater than or equal to
# $ne == not equal to
# $exists, to see if a document with the value exists
# note, greater than means newer as the greater date is larger/newer than the date being compared to ***

# index, see pymongo.docx for more details
db.users.create_index([('username', pymongo.ASCENDING)])

