# Project Title

Maze solver

## Description

This is a python script which can be used to solve simple square or rectangular mazes from .txt files. <br />
Maze is defined as a text file, with dimensions X*Y (it can be a maze of any size) made of the following characters:<br />

* X - wall (or any other chosen symbol defined as *'wall'* in configuration file)
* ' ' - road (or any other chosen symbol defined as *'path'* in configuration file)
* 0 - starting point (or any other chosen symbol defined as *'start'* in configuration file)
* F - finish (or any other chosen symbol defined as *'finish'* in configuration file)

The program in Python is able to find the shortest path through the maze from the 'start' character and finishing at the 
'finish'. The shortest path found is printed on the screen.

## Getting Started

### Dependencies

* Python version 3.7 and higher required
* Python pip package
* Requirements.txt has to be installed via `python -m pip install requirements.txt`

### Installing

* Clone git repository via `git clone https://github.com/TomTheMelonCat/maze.git`

### Executing program

* Program can be run in any chosen IDE
* Second option is to run the script straight from CMD or PowerShell via `path/to/script python maze_solver.py`

## Author

*Jiří Kadlec*  
[@GitHub](https://github.com/TomTheMelonCat/)

## Version History

* 0.2
    * Various bug fixes and optimizations/descriptions
* 0.1
    * Initial Release
