#!/usr/bin/python

import os, sys

class Keypad(object):
        def __init__(self):
                self.key = 5

        def up(self):
                if not (self.key == 1 or self.key == 2 or self.key == 3):
                        self.key = self.key - 3

        def down(self):
                if not (self.key == 7 or self.key == 8 or self.key == 9):
                        self.key = self.key + 3

        def right(self):
                if not (self.key == 3 or self.key == 6 or self.key == 9):
                        self.key = self.key + 1

        def left(self):
                if not (self.key == 1 or self.key == 4 or self.key == 7):
                        self.key = self.key - 1

class GoofyKeypad(object):
        def __init__(self):
                self.key = "5"

        def up(self):
		#print "Moving up from " + self.key
                if not (self.key == "5" or self.key == "2" or self.key == "1" or self.key == "4" or self.key == "9"):
                        if not (self.key == "3" or self.key == "D"):
                                self.key = hex(int(str(self.key), 16) - 4)[2:].upper()
                        else:
                                self.key = hex(int(str(self.key), 16) - 2)[2:].upper()

        def down(self):
		#print "Moving down from " + self.key
                if not (self.key == "5" or self.key == "A" or self.key == "D" or self.key == "C" or self.key == "9"):
			if not (self.key == "1" or self.key == "B"):
                        	self.key = hex(int(str(self.key), 16) + 4)[2:].upper()
			else:
				self.key = hex(int(str(self.key), 16) + 2)[2:].upper()

        def right(self):
		#print "Moving right from " + self.key
                if not (self.key == "1" or self.key == "4" or self.key == "9" or self.key == "C" or self.key == "D"):
                        self.key = hex(int(str(self.key), 16) + 1)[2:].upper()

        def left(self):
		#print "Moving left from " + self.key
                if not (self.key == "1" or self.key == "2" or self.key == "5" or self.key == "A" or self.key == "D"):
                        self.key = hex(int(str(self.key), 16) - 1)[2:].upper()

key = GoofyKeypad()

with open(sys.argv[1]) as f:
        for line in f:
                for move in line:
                        if move == "U":
                                key.up()
                        elif move == "D":
                                key.down()
                        elif move == "R":
                                key.right()
                        elif move == "L":
                                key.left()

                print hex(int(key.key, 16))[2:].upper()
