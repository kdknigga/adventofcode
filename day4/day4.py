#!/usr/bin/python

import os, sys
import re

room_pattern = re.compile("([a-z\-]+)-([0-9]+)\[([a-z]{5})\]")

def calculate_checksum(word):
	letter_counts = {}
	calculated_checksum = ""

	for letter in set(word.replace("-", "")):
		if word.count(letter) in letter_counts:
			letter_counts[word.count(letter)].append(letter)
		else:
			letter_counts[word.count(letter)] = [letter,]

	for letter_count in sorted(letter_counts, reverse=True):
		for letter in sorted(letter_counts[letter_count]):
			calculated_checksum = calculated_checksum + letter

	return calculated_checksum[:5]

sector_sum = 0

with open(sys.argv[1]) as f:
        for cyphertext, sector, checksum in [room_pattern.match(line).groups() for line in f]:
		test_checksum = calculate_checksum(cyphertext)
		#print checksum + " :: " + test_checksum
		if checksum == test_checksum:
			sector_sum += int(sector)

print "Sector sum: " + str(sector_sum)

