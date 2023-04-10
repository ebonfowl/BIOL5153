#! usr/bin/env python3

# import modules
import argparse

# create argument parser object
parser = argparse.ArgumentParser(description='This script reads in a GFF file line by line')

# add positional arguments
parser.add_argument('gff_file', help = 'GFF filename', type = str)
parser.add_argument('fasta_file', help = 'FASTA filename', type = str)

# parse arguments
args = parser.parse_args()

# read file
GFF_file = open(args.gff_file, 'r')
GFF_lines = GFF_file.readlines()