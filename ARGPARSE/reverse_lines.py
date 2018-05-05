#!/usr/bin/env python3.6
import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename_read', help='the file to read')
parser.add_argument('filename_write', help='the file to write')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

with open(args.filename_read, 'r') as inputfile:
    with open(args.filename_write, 'w') as outputfile:
        lines_list = inputfile.readlines()
        lines_list_reversed = lines_list[::-1]

        # conditional for if the limit argument is not null
        if args.limit:
            lines_list_reversed = lines_list_reversed[:args.limit]

        for line in lines_list_reversed:
            outputfile.write(line)
