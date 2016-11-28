#!/usr/bin/python3
import re, string, sys


# the chapter count is arbitrary.
try:
    file_path = sys.argv[1].strip()
    # note the first argument is the 'file_name.py'
    file = open(file_path, "r")

    line_list = []
    line_count = 0
    chapter_count = 1
    for line in file:
        if line.strip() == "":
            pass
        else:
            if line_count > 100:
                line_count = 0
                chapter_count += 1
            line_count += 1
            temp_line = line.rstrip("\n")
            text = str(chapter_count) + "-" + str(line_count) + '\t' + temp_line
            line_list.append(text)
    file.close()

    if len(sys.argv) > 2:
        # the second argument will be the file path for the output.
        file_path = sys.argv[2].strip()

    file = open(file_path, "w")
    for line in line_list:
        print(line, file=file)
    file.close()

except FileNotFoundError:
    print("File was not found.")