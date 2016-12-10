#!/usr/bin/python

from __future__ import print_function
import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-d", "--debug", action='count')
parser.add_argument("-x", "--width", type=int, default=50)
parser.add_argument("-y", "--height", type=int, default=6)
args = parser.parse_args()

def debug_print(string, level=1):
	if args.debug >= level:
		print(string, file=sys.stderr)

screen = [[0 for x in range(args.width)] for y in range(args.height)]

def rect(a, x, y):
	for row in range(y):
		for col in range(x):
			a[row][col] = 1

def rotate_col(a, col, n):
	b = []
	for row in range(len(a)):
		b.append(a[row][col])
	
	for row in range(len(b)):
		a[row][col] = b[row - n]

def rotate_row(a, row, n):
	b = list(a[row])
	for col in range(len(b)):
		a[row][col] = b[col - n]

def count_lit_pixels(a):
	return sum(map(sum, a))

def display_screen(a):
       for row in screen:
	       for col in row:
		       if col == 1:
			       print("#", end="")
		       else:
			       print(" ", end="")

	       print("")

def display_screen(a):
	for row in screen:
		for col in row:
			if col == 1:
				print("#", end="")
			else:
				print(" ", end="")

		print("")

with open(args.input_file) as f:
	for line in [ line.strip().split() for line in f ]:
		if line[0] == "rect":
			rect(screen, int(line[1].split("x")[0]), int(line[1].split("x")[1]))
		elif line[0] == "rotate":
			if line[1] == "column":
				rotate_col(screen, int(line[2].split("=")[1]), int(line[4]))
			elif line[1] == "row":
				rotate_row(screen, int(line[2].split("=")[1]), int(line[4]))
			else:
				print("Unknown rotate command: " + line[1], file=sys.stderr)
		else:
			print("Unknown command: " + line[0], file=sys.stderr)

		if args.debug >= 1:
			print(line)
			display_screen(screen)
			print("")


display_screen(screen)
print("Lit pixel count = " + str(count_lit_pixels(screen)))

