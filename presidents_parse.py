import argparse
import csv
from collections import defaultdict

# create argument parser object
parser = argparse.ArgumentParser(description = 'This script does something with presidents')

# add positional arguments
parser.add_argument('file', help = 'presidents.csv filepath', type = str)

# parse arguments
args = parser.parse_args()

# dictionary {name: party}
party = defaultdict(dict)

party_count = defaultdict(dict)

with open(args.file) as file:

    reader = csv.reader(file)

    for line in reader:

        if not line:
            continue

        if line[0] == 'Presidency ':
            continue

        # print(line)
        pres_name = line[1].strip()
        pres_party = line[5].strip()
        party[pres_name] = pres_party

# print dictionary keys
for pres, part in party.items():
    # print(pres, 'belonged to the', part, 'party')
    value = party_count.get(part, 'first')
    if value == 'first':
        party_count[part] = 1
    else:
        party_count[part] += 1

for part, num in party_count.items():
    print('There have been', num, 'president(s) belonging to the', part, 'party.')