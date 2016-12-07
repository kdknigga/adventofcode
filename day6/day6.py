#!/usr/bin/python

import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--modified", action='store_true')
args = parser.parse_args()


encoded_message = []
decoded_message = dict()

with open(args.input_file) as f:
        for line in f:
                encoded_message.append(line.strip())

for columnnum in range(len(encoded_message[0])):
        column = [ encoded_message[rownum][columnnum] for rownum in range(len(encoded_message)) ]
        if args.modified:
                decoded_message[columnnum] = min(set(column), key=column.count)
        else:
                decoded_message[columnnum] = max(set(column), key=column.count)

print "".join(decoded_message.values())
