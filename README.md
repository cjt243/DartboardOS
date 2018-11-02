# DartboardOS

DartboardOS is a project using python 3, kivy and sqlite to create a game scoreboard and stats database for darts.

The code is written specifically to run on the official Raspberry Pi 7" touch screen, but will work fine on a laptop screen, as the app window will auto-size on opening.

## [Get Started](https://github.com/cjt243/DartboardOS/blob/master/getstarted.md)


## Preview

![](https://github.com/cjt243/DartboardOS/blob/master/assets/Preview/gamepreview.png)

## Current Functionality

* Initialize a list of your friends into the player table.
* Scoreboard for cricket with running point totals
* Undo hits in reverse sequence (in case you fat finger a slash mark)
* Database
    * Each game is recorded in a table called game_header
    * Each hit marked is recorded in a table called game_line
    * These tables can be used to aggregate stats and records over time.

## Functionality Not Yet Implemented

* 301 and 501 game modes
* Add a new player from the Main Menu

## Game Analytics

Currently working on apps in Qlik Sense Cloud and Tableau Public. The code and links to examples will be linked here once complete
