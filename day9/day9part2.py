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
	string_len = 0
	debug_print("Incoming string: %s" % (string, ), 2)

	while string:
		# Find next repetition marker
		marker = marker_re.search(string)

		if marker:
			debug_print("Found marker: " + marker.group(0))

			# Count characters before the marker and
			# and then discard them along with the marker
			debug_print("Found %d chars before the marker" % (len(string[:marker.start()]), ), 2)
			string_len += len(string[:marker.start()])
			string = string[marker.end():]
			debug_print("string trimmed to \"%s\"" % (string, ), 2)

			# Find repeated string, repeat it, and trim it
			repeated_string = string[:int(marker.group(1))]
			times_repeated = int(marker.group(2))
			debug_print("Repeating \"%s\" %d times" % (repeated_string, times_repeated))
			repeating_string = repeated_string * times_repeated
			string = string[len(repeated_string):]
			debug_print("string trimmed to \"%s\"" % (string, ), 2)

			# the repeating string might have markers in it, so
			# send it back through decompress()
			debug_print("Sending \"%s\" back through decompress()" % (repeating_string, ), 2)
			len_from_substring = decompress(repeating_string)
			debug_print("Substring length of %d returned" % (len_from_substring, ), 2)
			string_len += len_from_substring

		else:
			# Finding no marker means add the remaining len
			# to string_len and discard
			debug_print("Found %s (%d) at the end of the string" % (string, len(string)), 2)
			string_len += len(string)
			string = ""

	debug_print("Sending %d up to caller" % (string_len, ), 2)
	return string_len

with open(args.input_file) as f:
	for line in [ line.strip() for line in f ]:
		string_len = decompress(line)

print "Length: %d" % (string_len, )
