# Progress and Goals: Design Project Spring 2023

## What has been completed in the project
- Set up a local and cloud mongoDB configuration. The local config is used for local and unit testing, while the cloud is used by the actual website. This meets the requirement for the mongo set up.
- New db and collections added to MongoDB cluster
- Domain setup: aptget.nyc and Cloudflare
- Deployed our website through heroku to aptget.nyc
- Created endpoints for login, post, user address, and paramter serialization. All endpoints work on the swagger ui, and have success and failure tests written for unit testing.
- New user logins inserts user info into MongoDB collection
- We have a home page frontend written in react js, and have integrated some endpoints to work on the home page.
- Initial designs on Figma for dashboard and login pages

## Goals for this Semester
### Goal 1: Implement Buying Out & Bidding Buttons
- Requirement: To allow users to buy out or bid on an item
- Expectation: To implement the functionality of buying out and bidding on the item page. The React frontend should call our backend APIs to trigger certain update actions to the MongoDB database to store the user's actions.

## Goal 2: Add Search by Building Address
- Requirement: To allow users to search for items based on building address
- Expectation: To implement the search functionality based on building address. The React frontend should call our backend APIs to retrieve a row in our MongoDB's Address collection to locate the exact building the user is searching for. If the building is not in our database, we should add a row to the Address collection.

## Goal 3: Implement Post Commenting
- Requirement: To allow users to post comments on an item
- Expectation: To implement the functionality of commenting on an item. The React frontend should use our backend APIs to store user comment messages in MongoDB.

## Goal 4: User Profile Pages
- Requirement: To allow users to view their profile information
- Expectation: To implement user profile pages with personal information and a history of their actions on the platform (e.g. items posted, items bought/bid on). The React frontend should access our backend APIs that should fetch all information related to the specific user such that the frontend can display those information.

## Goal 5: Listing Items
- Requirement: To allow users to list items they want to put up for selling
- Expectation: To implement the functionality for users to list items they wish to sell on the website. We should have a frontend page with a form that allows the user to fill out all relevant information. Then, the form information should be submitted to one of our backend APIs, which should then create a row in the Item collection.
