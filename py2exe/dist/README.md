vvvvvv-scripting-toolkit
========================

A set of tools to make scripting in VVVVVV custom levels just that bit easier

###How to use
####extract.py

Extracts the scripts from a level name specified by the user (without the .vvvvvv extension), replaces all | characters with \n (newlines), and writes it to a file. This way, the scripts may be looked at and edited with an external text editor

####import.py

Imports scripts from a file into a specified level name. It replaces all \n (newline) characters with | chars, keeping with the original level's format. It makes a backup of the level being modified to:

`<path-to-VVVVVV-folder>/vvvvvv_level_backups/<levelname><dateandtime>.vvvvvv`

before any data is written.

###How to run
####Windows
You must have Python 2.7.x installed from <http://python.org/>. Older versions may or may not work, but Python 3.x will NOT work without putting the script files through 2to3. Once you have that installed, simply double-click on either extract.py or import.py to start the process.

####Mac OS X or Linux
On Mac OS X or Linux, simply open the Terminal, navigate to the folder containing the scripts, and execute

`$ python <scriptname>.py`

e.g. if you've downloaded the archive to `~/Downloads`, and you wish to run the extract.py script, you execute the following series of commands:

`$ cd Downloads/vvvvvv-scripting-toolkit-head`

`$ python extract.py`

