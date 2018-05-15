#!/usr/bin/env python3.6

# Script that allows a user to specify a 1) file name to read 2) the number of lines to read out of the file
# and 3) the name of a file to write the lines to
# the script then reverses the order of those lines and writes them to new file name

# this script is an exercise in use a more robust CLI argument parsing environment

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename_read', help='the file to read')
parser.add_argument('filename_write', help='the file to write')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

# good discussion on why it is best to put the entire 'with open' block inside of the try block
# https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python

try:
    with open(args.filename_read, 'r') as inputfile:
        with open(args.filename_write, 'w') as outputfile:
            lines_list = inputfile.readlines()
            lines_list_reversed = lines_list[::-1]

            # conditional for if the limit argument is not null
            if args.limit:
                lines_list_reversed = lines_list_reversed[:args.limit]

            for line in lines_list_reversed:
                outputfile.write(line)
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
