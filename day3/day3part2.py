#!/usr/bin/python

import os, sys

possible = 0

data = []

with open(sys.argv[1]) as f:
        for line in f:
		row = map(int, line.split())
		data.append(row)

for row in range(0, len(data), 3):
	for col in [0, 1, 2]:
		side_a = data[row][col]
		side_b = data[row+1][col]
		side_c = data[row+2][col]

		print "side a: " + str(side_a) + " side b: " + str(side_b) + " side c: " + str(side_c)

		A_B_C = False
		B_C_A = False
		C_A_B = False

		if (side_a + side_b) > side_c:
			A_B_C = True
			print "A_B_C"
		if (side_b + side_c) > side_a:
			B_C_A = True
			print "B_C_A"
		if (side_c + side_a) > side_b:
			C_A_B = True
			print "C_A_B"

		if A_B_C and B_C_A and C_A_B:
			possible += 1
			print "Triangle!"

		print ""

print "Possible triangles: " + str(possible)
