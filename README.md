# SWE-Project for team AptGet

Team members: Oliver Li, Leo Li, Alex Yan, Tom Zhang

## Website URL
<https://www.aptget.nyc/>

## Project Description

A online trading platform for buying and selling items between apartment residents in New York. The furniture turnover rate in New York is high, with people frequently moving, and leaving furnitures in good condition out on the street or in trash rooms. A marketplace for these furnitures with a building/neighborhood approach makes it easy for new and old residents to buy and sell furnitures.

## How to run tests in local environment

1. You need mongodb installed, follow instructions [here](db/SETUP.md) to install
2. Install all dependencies by running `make` (Suggest doing this in a new virtual environment)
3. Set variable `export CLOUD=0` and start up local mongodb server by running `mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork`. (This needs to be run on macOS or Linux)
4. Run test with `make all_tests`.

## How to run server in local environment

1. You need npm and mongodb installed. Follow instructions [here](db/SETUP.md) to install mongodb
2. Set variable `export CLOUD=0` and start up local mongodb server by running `mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork`. (This needs to be run on macOS or Linux)
3. `make`
4. `make run`

## How to run frontend only in local environment
1. You need npm installed
2. `cd server/frontend`
3. `npm install`
4. Set environment variable `REACT_APP_DEV=1`
5. `npm start`

## Tech Stack

- Design: Figma
  - <https://www.figma.com/file/KXnCAjAzVFg10HBzwQb6TN/AptGet?node-id=0%3A1>
- Backend: Flask
- Frontend: React.js
- Database: MongoDB
  - Dashboard: <https://charts.mongodb.com/charts-project-0-huvbr/public/dashboards/63308fe7-4a00-4965-8f95-d76dd99cb888>

## Endpoints

- Log in & register account to post item
  - Use google-auth, log in and register with google accounts
- Clicking into item shows more details
- Dashboard for customers to view items
- Dashboard for seller to...
  - post item
  - edit item
  - delete item
  - post item
- Buying out / bidding buttons on item page
- Search by building address
- Post commenting
- User profile pages
- Post requests for items
