#!/usr/bin/python

import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-d", "--debug", action='count')
args = parser.parse_args()

def debug_print(string, level=1):
	if args.debug >= level:
		print >> sys.stderr, string

def find_abba(string):
	if (string[0] == string[3]) and (string[1] == string[2]) and (string[0] != string[1] ):
		debug_print("find_abba: testing string: " + string + " :: True", 3)
		return True
	else:
		debug_print("find_abba: testing string: " + string + " :: False", 3)
		return False

abba_count = 0

with open(args.input_file) as f:
	for line in [ line.strip() for line in f ]:
		abba_line = False
		in_brackets = False
		for i in range(len(line) - 3):
			if line[i] == "[":
				in_brackets = True
				continue

			if line[i] == "]":
				in_brackets = False
				continue

			if not in_brackets:
				if find_abba(line[i:i+4]):
					abba_line = True
			else:
				if find_abba(line[i:i+4]):
					debug_print("Found ABBA in brackets.  This line isn't a match", 2)
					abba_line = False
					break

		if abba_line:
			abba_count += 1
			debug_print("ABBA True:  " + line)
		else:
			debug_print("ABBA False: " + line)

		debug_print("")


print "Total ABBA lines: " + str(abba_count)
