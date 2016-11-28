#!/usr/bin/python3
import re, string, sys


try:
    file_path = sys.argv[1].strip()
    # note the first argument is the 'file_name.py'
    file = open(file_path, "r")

    line_list = []
    line_count = 0
    for line in file:
        if line.strip() == "":
            pass
        else:
            line_count += 1
            text = str(line_count) + '\t' + line
            line_list.append(text)
    file.close()

    if len(sys.argv) > 2:
        # the second argument will be the file path for the output.
        file_path = sys.argv[2].strip()

    file = open(file_path, "w")
    for line in line_list:
        print(line, file=file, end="")
    file.close()

except FileNotFoundError:
    print("File was not found.")