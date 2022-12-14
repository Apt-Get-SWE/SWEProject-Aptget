# Setting up a local MongoDB database

To install a local MongoDB database, follow the instructions here: https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database

## Environment Setup

For <b>remote</b> connections, run

- `export CLOUD=1`
- `export USER=USERNAME`
- `export PASS=PASSWORD`

where `USER` is the URI username and `PASS` is the URI password. 

To run the local database on a <b>UNIX</b> system, run:
- `cd PATH_TO_DB_DIRECTORY`
- `mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork`

To run the local database on Windows or Linux, follow the instructions in the link above.

To terminate the local database process, run `pkill mongod`


