# Advent of Code 2021 - Day 2 Part 1
# Author: Camron Miller
# Created: 12/02/2021
# Last Modified: 12/02/2021
# Purpose: 
#   Read in submarine instructions from a file
#   Commands:
#       Forward -> Increase horizontal position
#       Up -> Decrease vertical(depth) position
#       Down -> Increase vertcal(depth) position
#   Determine final horizontal and vertical(depth) position
#   Determine product of final horizontal and vertical(depth) position

# get data from file
sample = 'day2-sample.txt'
actual = 'day2-input.txt'

fileName = actual

try:
    fh = open(fileName)
except:
    print(f'File {fileName} not found')

commands = [x.split() for x in fh]

fh.close()

# start logic
movements = {'forward' : 0, 'up' : 0, 'down' : 0}

for command in commands:
    movements[command[0]] = movements.get(command[0], 0) + int(command[1])

print(movements)
print(f'Final Horizontal: {movements["forward"]} \nFinal Depth: {movements["down"] - movements["up"]}')
print(f'Horizontal * Depth = {movements["forward"] * (movements["down"] - movements["up"])}')