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

key = Keypad()

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

                print key.key
