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



GFF_lines2 = []
for line in GFF_lines:
    if line == '\n':
        GFF_lines.remove(line)
        continue
    line = line.strip()
    line = line.split('\t')

    # define column variables
    organism = line[0]
    source = line[1]
    feature_type = line[2]
    start = int(line[3])
    end = int(line[4])

    # fix length
    line[5] = str(end - start + 1)

    length = line[5]
    strand = line[6]
    attributes = line[8]

    print(feature_type + '\t' + length)

    GFF_lines2.append(line)