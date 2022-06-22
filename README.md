# Description
This is a python script which can be used to solve simple square or rectangular mazes from .txt files.<br />
Maze is defined as a text file, with dimensions X*Y (it can be a maze of any size) made of the following characters:<br />
&emsp;**X** - wall (or any other chosen symbol defined as **'wall'** in configuration file)<br />
&emsp;**' '** - road (or any other chosen symbol defined as **'path'** in configuration file)<br />
&emsp;**0** - starting point (or any other chosen symbol defined as **'start'** in configuration file)<br />
&emsp;**F** - finish (or any other chosen symbol defined as **'finish'** in configuration file)<br /><br />
The program in Python is able to find the shortest path through the maze from the 'start' character and finishing at the 'finish'.
The shortest path found is printed on the screen.<br />

# Installation
1, Clone git repository via **git clone https://github.com/TomTheMelonCat/maze.git**<br />
2, Install Python pip package :<br />
&emsp; - download [Pip](https://bootstrap.pypa.io/get-pip.py) package <br />
&emsp; - powershell -> **path/to/pip/folder python get-pip.py** <br />
&emsp; - check whether installation was successful via displaying version of pip (pip -V) <br />
3, **Requirements.txt** has to be installed with pip command (python -m pip install requirements.txt) <br />
# Configuration
1, In order to make script work correctly, valid values has to be set in the configuration file - config.yaml.<br />
&emsp;Default values have been set, so you can take them as a template and change them accordingly. <br />
2, In order to have the script working correctly, you have to have a maze in a .txt file. <br />
&emsp;Two default mazes are a part of the repository. Keep in mind, that mazes have to be in X*Y format <br />
&emsp;and must only contain valid symbols as specified in config.yaml. <br />
# Run
1, Run powershell -> **path/to/script python maze_solver.py** OR run **maze_solver.py** in a chosen IDE.
