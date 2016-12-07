#!/usr/bin/python

import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()

with open(args.input_file) as f:
        for line in f:
