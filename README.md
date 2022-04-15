TODO
get all data displaying nicely inside heroku 
sell check
readme
wireframe
bug
flowcharts
deployment
table of contents 
dropdown menu

# BATTLESHIP WARZONE

link to the live project below.
https://battleship-warzone.herokuapp.com/

![amiresponsive](/images/Screenshot%202022-04-15%20at%2012.12.16.png)

# how to play
BATTLESHIP Warzone is a python terminal version of the original battleship board game, that runs in a mock terminal on heroku.
The aim of the game is to plot your ships arround an 8 x 8 board while your opponent does the same, then each player has to try guess the coordinates of the other playters ship, the first player to correctly guess all of the locations of their opponents ships wins the game, there are 5 ships, ranging from a 2 man ship(takes up 2 places on the board) to a 5 man ship which takes up 5. 

# features
### Show board
this feature displays an 8x8 board split into columns and rows, the rows are numbered and the columns are aranged alphabetically.

### Place ships
this feature allows the user to place ships of varying sizes down on the board in a column and row they choose, the computer will also place ships down on its board and act as your opponent, credit[youtube video, advanced python battleship game]
### Error handling
error handling was a very important feature to implement into this game, as any error that was not delt with could cause the program not to run and make the game unplayable, I written functions that will ask for the users input again if an error with there chosen input arises eg. overlaping ships(two ships placed in the same location), ship does not fit (ship placed in an area where some of it would be outside the parameters of the board), invalid placement(if the user tries to place a ship outside of the 8x8 board)
### User input
this feature allows the user to place ships where they choose on the 8x8 board, these choises will be saved and used as the position of their ships for the entirety of the game. 
### Opponent
the opponent in this game is the computers random variable generator used in conjunction with the place_ships function, this function makes the computer generate a random integer between 0 and 7 and aplies the integer to a row and then a column this will place a ship in the selected row and collumn, during the game the opponet will use more or less the same logic to coordinate attacks on your ships.
### Winnersboard
the winners board is a feature that allows all players of the game to see a list of the last 20 winners, when a player finishes a game they will be told if they won or lost, with a display of some ascii art, they will then be prompted to enter 'W' (for a win) or 'L' (for a loss) if 'W' is entered the players name will be appended to the list of winners, if 'L' is selected the player will be given the option to play again or not.
### Ship size 
this feature is one that comes straight from the original Battle Ship game, where there are 5 ships of diffrent sizes, there is a 2 man ship (takes up 2 spaces) two 3 man ships (3 spaces each), a 4 man ship (4 spaces) and a 5 man ship (5 spaces).
### turns
this feature is necessary as the game is originaly played on a turn by turn basis where player 1 would attack then player 2 attacks and so on. Both players boards are printed to the terminal and as soon as the user attacks the computer will attack back, this makes for a fair and intense game of battle ship
### score
the score is counted in the count_score function which starts at '0', when a player or the computer correctly guesses the coordinates of thir opponents ship the board will be marked by an 'x' and the count will be incrimented by 1, if the users playing board reaches a count of 17 this means they have guessed all places of their opponents ships and win the game, the same goes for the computer if the computers play board count = 17 this means they have guessed where all of the users ships are and will win the game.

# data model



# testing
I have manualy tested this games throughout every step of its creation, since deployment I have played many games from start to finish and am yet to find any errors that were not fixed before deployment, I have also sent the link of the deployed heroku app to a few friends and colleagues, no bugs or issues have been reported. I also checked the code using the pep8 validator, the first time i did this I had alot of warnings, theese mostly consisted of "line too long" and "trailing whitespace at the end of line", after some careful refactoring all of these warnings were eliminated and the pep8 validator did not return any issues.


# bugs
while writing the code for this project i ran into a few bugs that were mostly syntax errors, one major bug I had was my place_ship function was stuck in a loop, and could never get to the end of the function to start the game, this was caused by my me mixing up row and collumn when writing the code, i ended up with 2 while loops that would not break while the row was in '12345678, when i changed the second 'row' to column the bug was fixed 


# deployment
I deployed my program using a mock terminal on heroku, i did this by:

. Updateing my requirements.txt file in the terminal using the command pip3 freeze > requirements.txt

. Pushing my most recent code to Github

. Sign up and login to Heroku

. Click the 'new app' button

. Created a name for my app (has to be unique)

. Selected my region

. Click the 'Create app' button

. From there I went into settings

. Config Vars  and clicked Reveal Config Vars

. Added my ports which were:
 key = PORT value = 800
 key = CREDS value = (my creds.json file copy and pasted in)

. Next I Added the buildpacks python and nodejs in that order

. With the setting finished I went over to the deploy tab

. I conected my Github account and entered my repo name and clicked search

. Connected to the Github repository

. I chose the option for Automatic deploys,

. Click deploy

to veiew a heroku app you must log in and select your required app, and click open, the app will then apear in a new tab and automatically run without the use of the command python3 run.py


# credits

My mentor Mo 
My Cohort facilatator Kasia
Code Institute staff and alumni
Stack overflow
W3Schools
pep8 python validator
pyfiglet(for ascii art)
youtube channels: computerphile, Tech With Tim, Knowledge Mavens, ArjanCodes
Fellow classmates in Code Institute


















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome RoMcGill,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!