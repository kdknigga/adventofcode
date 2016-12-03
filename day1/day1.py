#!/usr/bin/python

import os, sys

input_file = open(sys.argv[1])
directions = input_file.read().split(", ")
input_file.close()

position = [0, 0]
heading = "N"

crossover_points = []
position_history = []
position_history.append(position)

def rotate(start_heading, turn_direction):
        if start_heading == "N":
                if turn_direction == "R":
                        return "E"
                elif turn_direction == "L":
                        return "W"
                else:
                        print >> sys.stderr, "Unknown turn direction " + turn_direction
                        sys.exit(1)

        elif start_heading == "E":
                if turn_direction == "R":
                        return "S"
                elif turn_direction == "L":
                        return "N"
                else:
                        print >> sys.stderr, "Unknown turn direction " + turn_direction
                        sys.exit(1)

        elif start_heading == "S":
                if turn_direction == "R":
                        return "W"
                elif turn_direction == "L":
                        return "E"
                else:
                        print >> sys.stderr, "Unknown turn direction " + turn_direction
                        sys.exit(1)

        elif start_heading == "W":
                if turn_direction == "R":
                        return "N"
                elif turn_direction == "L":
                        return "S"
                else:
                        print >> sys.stderr, "Unknown turn direction " + turn_direction
                        sys.exit(1)

        else:
                print >> sys.stderr, "Unknown starting heading " + start_heading
                sys.exit(1)

def advance(position, heading, n, position_history):
        x, y = position
        if heading == "N":
                for step in range(n):
                        y += 1
                        if [x, y] in position_history:
                                #print "I've been here before: " + str([x, y]) + "  Distance: " + str(abs(x) + abs(y))
                                crossover_points.append([x, y])
                        position_history.append([x, y])
                return [x, y]
        elif heading == "S":
                for step in range(n):
                        y -= 1
                        if [x, y] in position_history:
                                #print "I've been here before: " + str([x, y]) + "  Distance: " + str(abs(x) + abs(y))
                                crossover_points.append([x, y])
                        position_history.append([x, y])
                return [x, y]
        elif heading == "E":
                for step in range(n):
                        x += 1
                        if [x, y] in position_history:
                                #print "I've been here before: " + str([x, y]) + "  Distance: " + str(abs(x) + abs(y))
                                crossover_points.append([x, y])
                        position_history.append([x, y])
                return [x, y]
        elif heading == "W":
                for step in range(n):
                        x -= 1
                        if [x, y] in position_history:
                                #print "I've been here before: " + str([x, y]) + "  Distance: " + str(abs(x) + abs(y))
                                crossover_points.append([x, y])
                        position_history.append([x, y])
                return [x, y]
        else:
                print >> sys.stderr, "Unknown heading " + heading
                sys.exit(1)

for step in directions:
        #print "Position: " + str(position) + "  Heading: " + heading
        #print "Turn " + step[0] + " and go " + step[1:] + " spaces"
        heading = rotate(heading, step[0])
        position = advance(position, heading, int(step[1:]), position_history)

print "Final Position: " + str(position) + "  Distance: " + str(abs(position[0]) + abs(position[1]))
if len(crossover_points) > 0:
	print "First Crossover Point: " + str(crossover_points[0]) + "  Distance: " + str(abs(crossover_points[0][0]) + abs(crossover_points[0][1]))
