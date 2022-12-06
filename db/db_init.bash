# FOR LOCAL DB INSTANCE
export ENV=local
export DB_URI=mongodb+srv://swe:swe123@cluster0.os9dia2.mongodb.net/apt-get

cd mongodb_local
mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork

# to view MongoDB in Mongo shell, enter 'mongosh'
    # to quit Mongo Shell, enter 'quit'
# to quit local MongoDB process, enter 'pkill mongod'

# REMOTE INSTANCE
# export DB_URI = REMOTE_SECRET
