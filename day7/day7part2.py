#!/usr/bin/python

import os, sys, argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-d", "--debug", action='count')
args = parser.parse_args()

def debug_print(string, level=1):
	if args.debug >= level:
		print >> sys.stderr, string

def find_aba(string):
	if (string[0] == string[2]) and (string[0] != string[1] ):
		debug_print("find_aba: testing string: " + string + " :: True", 3)
		return True
	else:
		debug_print("find_aba: testing string: " + string + " :: False", 3)
		return False

ssl_count = 0
babregex = re.compile("\[[a-z0-9]*bab[a-z0-9]*\]")

with open(args.input_file) as f:
	for line in [ line.strip() for line in f ]:
		ssl_line = False
		in_brackets = False
		for i in range(len(line) - 2):
			test_string = line[i:i+3]
			if "[" in test_string:
				in_brackets = True
				continue

			if "]" in test_string:
				in_brackets = False
				continue

			if not in_brackets:
				if find_aba(test_string):
					bab = test_string[1] + test_string[0] + test_string[1]
					regex = "\[[a-z0-9]*" + bab + "[a-z0-9]*\]"
					debug_print("Found aba: " + test_string + ", Looking for bab: " + bab + ", Using regex: " + regex, 2)
					if re.search(regex, line):
						debug_print("Found bab: " + bab, 2)
						ssl_line = True

		if ssl_line:
			ssl_count += 1
			debug_print("ABBA True:  " + line)
		else:
			debug_print("ABBA False: " + line)

		debug_print("")


print "Total SSL lines: " + str(ssl_count)
