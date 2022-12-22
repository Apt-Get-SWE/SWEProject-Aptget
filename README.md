# SWE-Project for team AptGet
Team members: Oliver Li, Leo Li, Alex Yan, Tom Zhang

## Website URL
https://www.aptget.nyc/

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

## Tech Stack
- Design: Figma
   - https://www.figma.com/file/KXnCAjAzVFg10HBzwQb6TN/AptGet?node-id=0%3A1
- Backend: Flask
- Frontend: React.js
- Database: MongoDB
   - Dashboard: https://charts.mongodb.com/charts-project-0-huvbr/public/dashboards/63308fe7-4a00-4965-8f95-d76dd99cb888

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

# Changelog
## 2022.11.4
- Make menu api

## 2022.10.30
- Create user info collection form
## 2022.10.23
- Set up local MongoDB instance for testing
- Implement Tailwind CSS
- Insert user data to MongoDB for new users
## 2022.10.16
- Create listing page figma design
- Update Google login Auth
- Create item component
## 2022.10.09
- Updated user info collection page on figma
- Using `PyMongo` to query MongoDB collections
- New `items` collection in MongoDB database
- Restructured `user` and `post` object types
## 2022.10.05
### Added
- React frontend setup
- Home page initial impl done (buttons and search bar static atm)
- Heroku setup done. Master will automatically be deployed to https://apt-get-swe.herokuapp.com/
- Set up domain aptget.nyc and Cloudflare
- Using `autopep8` in `make lint` to auto fix linting issues.
### Changed
- Using `react-restful` instead of `react-restx`. Not sure why `restx` is unable to return frontend `index.html`.

## 2022.10.02
- Initial dashboard design on Figma
- Added new db & collections to MongoDB cluster

## 2022.10.01
- Initial login page design on Figma

## 2022.09.29
- Kanban: https://trello.com/b/0wRC1BG3/kanban
