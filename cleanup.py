#!/usr/bin/env python3
"""
Moves files with a given extension from a source folder to a
defined destination.
"""
import os
import argparse
from shutil import move

PARSER = argparse.ArgumentParser(prog='cleanup')
PARSER.add_argument("--dry-run", help="Cleanup Dry Run. Doesn't actually move the files", 
        action="store_true")
PARSER.add_argument("source", help="Cleanup Source")
PARSER.add_argument("dest", help="Cleanup Destination")
PARSER.add_argument("ext", help="Files with extension to clean up, Ex. pdf")

ARGS = PARSER.parse_args()

PATH_S = ARGS.source
PATH_D = ARGS.dest
EXT = ARGS.ext

def get_file_list(source, extension):
    """ Return a collection of files that match the extentsion given

    Keyword arguments:
    source -- folder to traverse
    extension -- file extension to collect
    """
    list_ = list()
    for i in os.scandir(source):
        if i.is_file() and i.name.endswith(extension):
            list_.append(i.name)
    return list_


def move_files(source, dest, file_list):
    """ Moves files from the file list to a destination
    folder.

    Keyword Arguments:
    source -- folder to traverse
    dest -- file path to store moved files
    file_list -- files that will be moved
    """

    return [move(os.path.join(source, f), dest) for f in file_list]


def dry_run(source, dest, extension):
    """ Tests the move process without affecting the files

    Keyword Arguments:
    source -- folder to travers
    dest -- file path to store moved files
    extension -- files of extension to move
    """

    source_list = get_file_list(source, extension)
    file_count = len(source_list)

    if not os.path.exists(dest):
        return print("The path {0} does not exist".format(dest))

    print("Copying {0} files".format(file_count))
    print('----------')
    return [print("From: {0}{2} --> {1}{2}".format(source, dest, f)) for f in source_list]


if ARGS.dry_run:
    print('Dry Run, nothing is actualy being copied.\n')
    dry_run(PATH_S, PATH_D, EXT)
else:
    FILES_TO_MOVE = get_file_list(PATH_S, EXT)
    try:
        move_files(PATH_S, PATH_D, FILES_TO_MOVE)
    except:
        print('Something went wrong')
