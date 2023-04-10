#! usr/bin/env python3

# import modules
import argparse

# create argument parser object
parser = argparse.ArgumentParser(description = 'This script reads in a GFF file line by line')

# add positional arguments
parser.add_argument('gff_file', help = 'GFF filepath', type = str)
parser.add_argument('fasta_file', help = 'FASTA filepath', type = str)

# parse arguments
args = parser.parse_args()

# read file
GFF_file = open(args.gff_file, 'r')
GFF_lines = GFF_file.readlines()
GFF_file.close()
GFF_lines.remove(GFF_lines[-1])

# GFF_lines2 = []
for line in GFF_lines:
    # print(line)
    stripped_line = line.strip()
    stripped_line2 = stripped_line.split('\t')
    length = int(stripped_line2[4]) - int(stripped_line2[3])
    print(length)

