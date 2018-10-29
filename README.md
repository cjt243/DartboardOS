# DartboardOS

DartboardOS is a project using python 3, kivy and sqlite to create a game scoreboard and stats database for darts.

The code is written specifically to run on the official Raspberry Pi 7" touch screen, but will work fine on a laptop screen, as the app window will auto-size on opening.

## Setup
1. Install python 3 (will add full list of libraries used)
2. Install Kivy 1.10 and Cython 0.29
3. Run setupdb.py (found in the gamedb dir)
4. Edit initialize_players.py to include your friends, and run
 
## Current Functionality

* Initialize a list of your friends into the player table.
* Scoreboard for cricket with running point totals
* Database
    * Each game is recorded in a table called game_header
    * Each hit marked is recorded in a table called game_line
    * These tables can be used to aggregate stats and records over time.

## Functionality Not Yet Implemented

* The Undo button is currently inactive
* 301 and 501 game modes
* Add a new player from the Main Menu

## Game Analytics

Currently working on apps in Qlik Sense Cloud and Tableau Public. The code and links to examples will be linked here once complete
