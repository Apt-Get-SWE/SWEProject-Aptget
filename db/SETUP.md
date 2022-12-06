# Local MongoDB Database Setup
Steps:
1. Install MongoDB instance
2. Install MongoDB Shell

## How to install MongoDB Database
Follow the instructions @ https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database#setting-up-mongodb-on-macos

## Environment Setup
- For local connection, use `export ENV=local`
- For remote connection, use `export DB_URI=SECRET_URI`

- To run the local database, enter:
    `cd mongodb_local`
    `mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork`

- To terminate the database process, enter:
    `pkill mongod`


