#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import utils

def extract(level_name=None, save_file=None):
    # Initializing variables
    filedata = ""
    script_data = None
    vvvvvv_dir = None

    # Get current opsys
    vvvvvv_dir = utils.get_vvvvvv_dir()

    # Checks whether level_name specified beforehand (for quiet execution)
    if not level_name:
        # request filename from user
        while True:
            level_name = None
            level_name = utils.get_level_name()
            if not level_name:
                print "You must enter a level name"
                continue
            
            # get level data
            raw_data = utils.get_raw_data(vvvvvv_dir, level_name)

            if not raw_data:
                print "Error: level does not exist"
                continue
            else:
                break

    else:
        raw_data = utils.get_raw_data(vvvvvv_dir, level_name)

    # get script data
    script_data = utils.get_script_data(raw_data)

    if not script_data:
        print "No script found"
        quit()

    final_data = utils.cleanup_data(script_data)

    print "Done!"

    # checks if save_file specified beforehand (for quiet execution)
    if not save_file:
        cwd = os.getcwd()
        print
        print "What file do you wish me to save the data to?"
        print "Current working directory is: "
        print
        print cwd
        print
        print "You may enter a filename to save in current directory,"
        print "enter a relative path, or a full path."
        print
        print "Else, press return to accept the default, which is: "
        print
        print level_name + ".6vscript"
        print
        save_file = raw_input("Save file: ")
        if not save_file:
            save_file = level_name + ".6vscript"

    else:
        pass

    with open(save_file, 'w') as outfile:
        for line in final_data:
            outfile.write(line + '\n')

        print save_file + " written"
        
if __name__ == "__main__":
    extract()
