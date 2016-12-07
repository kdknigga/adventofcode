#!/usr/bin/python

import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-d", "--debug", action='count')
args = parser.parse_args()

def debug_print(string, level=1):
	if args.debug >= level:
		print >> sys.stderr, string

with open(args.input_file) as f:
	for line in [ line.strip() for line in f ]:
