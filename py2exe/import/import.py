#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import shutil
import utils

def import_script(script_name=None, level_name=None):
    # get name of script file
    if not script_name: #if script_file not defined
        while True:
            print "Please enter the name of the script file."
            print "The current working directory is "
            print
            print os.getcwd()
            script_name = raw_input("Path to .6vscript file: ")
            if not script_name:
                print "You must specify a script to import."
                continue
            else:
                try:
                    with open(script_name): pass
                except IOError:
                    print 'File not found.'
                else:
                    break

        print

    # Checks whether level_name specified beforehand (for quiet execution)
    if not level_name:
        while True:
            print "Please enter the filename of the level"
            print "(do not include .vvvvvv or else bad things will happen)"
            level_name = utils.get_level_name()

            if not level_name:
                print "You must enter a level name"
                continue

            else:
                break

    # backup level file
    print "Backing up level file..."
    backup_file = utils.level_backup(level_name)
    print "Backup saved to " + backup_file

    # get raw level data from file
    level_data = utils.get_raw_data(utils.get_vvvvvv_dir(), level_name)

    # get raw script data from file
    raw_script_data = utils.get_script_filedata(script_name)

    # convert script data to raw data
    script_data = utils.script_to_raw(raw_script_data)

    if not script_data:
        raise IOError

    utils.import_script_data(level_data, script_data)

    # going hot!
    success = utils.write_level_data(utils.get_vvvvvv_dir(), level_name, level_data)
    if success:
        print "File successfully written."

    else:
        print "An error occurred when writing the file."

if __name__ == "__main__":
    import_script()
