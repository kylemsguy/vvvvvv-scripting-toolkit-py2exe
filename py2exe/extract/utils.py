## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import sys
import shutil
from HTMLParser import HTMLParser
from os.path import expanduser
from time import strftime

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def get_vvvvvv_dir():
    home_dir = expanduser("~") # Gets home dir
    
    if sys.platform.startswith("linux"):
        vvvvvv_dir = home_dir + "/.vvvvvv/"

    elif sys.platform.startswith("win"):
        vvvvvv_dir = home_dir + "/Documents/VVVVVV/"
        if not os.path.isdir(vvvvvv_dir):
            vvvvvv_dir = home_dir + "/My Documents/VVVVVV"

    elif sys.platform.startswith("darwin"):
        vvvvvv_dir = home_dir + "/Documents/VVVVVV/"

    else:
        print "Error: unsupported platform"
        quit()

    if not os.path.isdir(vvvvvv_dir):
        print "VVVVVV directory not found. Please run VVVVVV at least once",
        print "prior to using this utility."
        exit()

    return vvvvvv_dir

def get_raw_data(vvvvvv_dir, level_name):
    # get level data
    filename = level_name + ".vvvvvv"    
    level_path = vvvvvv_dir + filename
    try:
        with open(level_path, 'r') as infile:
            return infile.readlines()
    except IOError:
        return False

def write_level_data(vvvvvv_dir, level_name, level_data):
    filename = level_name + ".vvvvvv"
    out_data = ''.join(level_data)
    level_path = vvvvvv_dir + filename
    try:
        with open(level_path, "w") as outfile:
            outfile.write(out_data)
    except IOError:
        return False

    else:
        return True

def get_script_filedata(script_path):
    try:
        with open(script_path) as infile:
            return infile.readlines()

    except IOError:
        return False

def get_script_data(raw_data):
    # get script data
    for line in raw_data:
        if "<script>" in line:
            return line

    if not script_data:
        return False

def import_script_data(raw_data, script_data):
    for i in range(len(raw_data)):
        if "<script>" in raw_data[i]:
            raw_data[i] = script_data
            return True
        else:
            continue

    return False

def cleanup_data(script_data):
    # remove <script></script> tags
    tagless_data = strip_tags(script_data)

    # remove any leading spaces etc
    sanitized_data = tagless_data.lstrip()

    # split into lines by pipe chars
    final_data = sanitized_data.split('|')

    return final_data

def script_to_raw(script_data):

    raw_data = []

    for line in script_data:
        raw_data.append(line.rstrip("\n"))

    joined_raw_data = '|'.join(raw_data)

    final_raw_data = "\t<script>" + joined_raw_data + "</script>\n"

    return final_raw_data

def get_level_name():
    level_name = raw_input("ID of level (do not include extension): ")
    return level_name

def level_backup(level_name):
    # check if backup dir exists
    leveldir = get_vvvvvv_dir()
    backupdir = get_vvvvvv_dir() + "vvvvvv_level_backups/"
    if not os.path.isdir(backupdir):
        # make the dir
        os.mkdir(backupdir)

    curr_time = strftime("%Y-%m-%d %H%M")
    shutil.copyfile(leveldir + level_name + ".vvvvvv",
                    backupdir + level_name + curr_time + ".vvvvvv")

    return backupdir + level_name + curr_time + ".vvvvvv"
