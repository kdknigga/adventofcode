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

marker_re = re.compile("\(([0-9]+)x([0-9]+)\)")

def decompress(string):
	output_string = ""
	cursor = 0
	while cursor < len(string):
		# Find next repetition marker
		marker = marker_re.search(string, cursor)

		if marker:
			debug_print("Found marker: " + marker.group(0) + " at position: " + str(marker.start()))

			# All text since the last expansion until the next
			# marker should be copied verbatim to the output
			# string.
			output_string += string[cursor:marker.start()]

			# Find repeated string, repeat it, update output string
			repeated_string = string[marker.end():marker.end() + int(marker.group(1))]
			times_repeated = int(marker.group(2))
			repeating_string = repeated_string * times_repeated
			output_string += repeating_string

			# Move cursor past the marker and the repeated string
			cursor = marker.end() + int(marker.group(1))

		else:
			# Finding no marker means the rest of the text goes
			# straight to the output string
			output_string += string[cursor:]
			cursor = len(string)

	return output_string

with open(args.input_file) as f:
	for line in [ line.strip() for line in f ]:
		decompressed_string = decompress(line)

debug_print("Expanded string: " + decompressed_string)
print "Expanded string length: " + str(len(decompressed_string))

