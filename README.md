# Love Burger 

- Love Burger as the name suggest is a an app that helps the burger shop to monitor its stock automatically.
- It helps the employ to fill out the stock which will be automated.


[Link to the website](https://hangman-pp.herokuapp.com/)

![An image previewing all devices](/assets/screenshots/preview.png)

## Contents
- [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
- [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
- [Teachnical Design](#technical-design)
    - [Flowchart](#flowchart)
- [Technology Used](#technology-used)
    - [Language used](#language-used)
    -[Python Libraries used](#python-libraries-used)
    - [Other websites/tools used](#other-websitestools-used)
    - [3rd Party Python Libraries used](#3rd-party-python-libraries-used)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Tested Devices with Browsers](#tested-devices-with-browsers)
    - [Validator Testing](#validator-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deploying in Heroku](#deploying-the-website-in-heroko)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning of Repository i GitHub](#cloning-the-repository-in-github)
- [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
- [Thank You](#thank-you)

## Project Goals
### User Stories

-Love Burger application
-Can look for the last 5 days sales
-Can see the previous stock.
-Can see the upcoming stock
-Can update the sales resulting in the stock update

### Site Owner Goals

- Create an application which is easy and clear to user
- Ensure errors are handled and displayed to user
- Ensure that user is able to use
- Ensure that user can exit the application

## User Experience
### Target Audience

- Targetted audiece would be a shop owner that sells burger. 
- I would recommend that it helps the users to monitor there stock and update as per the sale

### User Requirements and Expectations

- A simple and easy application
- Straightforward Navigation

### User Manual
<details><summary>Click here to view instructions</summary>

#### Load Application

- On loading the application, users are presented with heading of the application which  displays design and the title.
- Under the heading, a question is prompted if the user is existing user or not.
- Operation: Please enter the an option: '1','2','3','4'
- If user inputs do not correspond with available option then they

#### Sign Up & Login

- There is no signup as it is a secured with the respective google account whereby, it can only be executed in the respective installed device


#### Rules

- Once users have been logged in, they will be asked if they want to see the rules
- Operation: Do you want to see the rules: Y/N

#### Start Application

- If user decide to see different option, they need to just type in the number and click enter
- If user decide to exit they can use anyother key other than the option and click enter

#### Application

- Operation: Enter an option:
    - '1' for updating today's sale, 
    - '2' to print the last 5 day sales 
    - '3' for printing the upcoming stock update 
    - '4' for printing the stock leftout for this week 
    - 'Anyother key' for Exiting the applicationUser need to enter a letter to start the game

## User Stories

### Users

1. I want to be able to update today's sale
2. I want to print the last 5 day sales
3. I want to print the upcoming stock update
4. I want to print the stock leftout for this week
5. I want to exit the application

### Site Owner

6. I want users to have a positive experience whilst playing the game
7. I want the user to get errors displayed in case of wrong input
8. I want data entry to be validated, to guide the user on how to correctly format the input

## Technical Design

## FlowChart

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart

<details>
    <summary>Flowchart</summary>
    <p>Love Burger</p>
    <img src = "assets/screenshots/Lucid.png" alt = "A screenshot of flowchart">
</details>

## Technology Used
### Language Used

  - Python

### Python Libraries used

- os - used to clear terminal
- random - used to choose random words
- time - used to displayed delayed areas in the terminal
- colorama - for the coloring
- gspread - for communicating with gsheets

### Other websites/tools used

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart
- [GitHub](https://github.com/) was used for saving and storing files.
- [codeanywhere](https://www.codeanywhere.com/) was the IDE used for writing code.
- [Heroku](https://www.heroku.com/) was used as the deploying platform for this site.

### 3rd Party Python Libraries used

- [Google sheets API](https://github.com/burnash/gspread) was used to store and check the user input and authorize the user identity
- [Google OAuth](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to connect the project with the google account.
- [Colorama](https://pypi.org/project/colorama/) was used for better visual display

## Features

### Home page display

- Once the user run the program this area is displayed
- The area consist of a display showing the heading
- It also prompts the users to provide input if they are an existing user
- User stories covered: 1
<details>
    <summary>Home Page screenshot</summary>
    <img src="assets/screenshots/home.png" alt="Game load page">
</details>  


## Testing
- Manual testing of application
- Testing on Browsers
- Tested Devices with Browsers
- Validator Testing

### Manual Testing
<details><summary>See user stories testing</summary>

1. I want update today sales

<details>
    <summary>Screenshots</summary>
    <p>home</p>
    <img src="assets/screenshots/home.png" alt="Sign up area">
</details> 

2. I want print last 5 day sales

<details>
    <summary>Screenshots</summary>
    <p>home</p>
    <img src="assets/screenshots/options1.png" alt="Sign up area">
</details> 

3. I want to be able to log-in if I return to the game

|<details>
    <summary>Screenshots</summary>
    <p>home</p>
    <img src="assets/screenshots/options3.png" alt="Sign up area">
</details> 

4. I want to be able to read the rules of the game

<details>
    <summary>Screenshots</summary>
    <p>home</p>
    <img src="assets/screenshots/options4.png" alt="Sign up area">
</details> 

5. I want to be able to restart game when I'm logged in

<details>
    <summary>Screenshots</summary>
    <p>home</p>
    <img src="assets/screenshots/options5.png" alt="Sign up area">
</details> 



### Testing on Browsers
- I tested that this game works in different browsers - Chrome and Safari and was able to deploy successfully

### Tested Devices with Browsers
- iPhone 12
    - Safari
- Samsung S22 Ultra
    - Chrome
- Macbook Pro 2019 16-inch
    - Chrome
    - Safari

### Validator Testing
#### PEP8 Python Validator
[PEP8 Python Validator](https://pep8ci.herokuapp.com/) was used to validate the code.

This validator was provided by Code Institute.

No errors were found.


### Unfixed Bugs

- No unfixed bugs

## Deployment

### Deploying the website in Heroko:
- The website was deployed to Heroko using following steps:
#### Login or create an account at Heroku
- Make an account in Heroko and login


#### Creating an app
  - Create new app in the top right of the screen and add an app name.
  - Select region
  - Then click "create app".

#### Open settings Tab
  ##### Click on config var
  - Store CREDS file from gspread in key and add the values
  - Store PORT in key and value


##### Connect to Github
  - Choose repositories you want to connect
  - Click "Connect"

##### Automatic and Manual deploy
  - Choose a method to deploy
  - After Deploy is clicked it will install various file

##### Final Deployment
  - A view button will display
  - Once clicked the website will open


## Credits

### Content
- The text content was provided by the site owner.
- Idea of stock application has been taken from tutorial around the world

### Code
#### The following ideas were borrowed from [Love Sandwiches](https://github.com/Sinha5714/Love_Sandwiches)

-  validate_user_details function
-  How to import gspread
-  How to import Credentials from google.oauth



### Thank You
- to my mentor Mo Shami for supporting me with his feedback through the entire project
- special thanks to my husband Remo Liebetrau to help me finding out the issues in the game
- to Code Institute and Slack community for helping me when I was getting stuck with some challenges.