import csv
import os
import sys
import re

working_directory = os.getcwd()

file = "refined_fall_2018_courselist.csv"

with open(file, "r") as csvinput:
    reader = csv.reader(csvinput)
    # This grabs the headers and re-creates a set of new ones
    header = next(reader)
    header[1] = "enrollment"
    new_file = [] # All of our new rows o in here
    new_file.append(header)

    for row in reader:
        if "" in row or "null" in row:
            continue
        else:
            enrollment_all = row[1]
            enrollment = re.search(':\s+(\d+)', enrollment_all).groups()[0]
            row[1] = enrollment
            new_file.append(row)

    with open(f"cleaned_q_scores_2018.csv", 'w') as csvoutput:
        print(f"Writing for file")
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(new_file)
