# Advent of Code 2021 - Day 2 Part 2
# Author: Camron Miller
# Created: 12/02/2021
# Last Modified: 12/02/2021
# Purpose: 
#   Read in submarine instructions from a file
#   Commands:
#       Forward -> Increase horizontal position,
#                  Change vertical position by product of aim and Forward command
#       Up -> Decrease aim position
#       Down -> Increase aim position
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
movements = {'forward' : 0, 'aim' : 0, 'depth' : 0}

for command in commands:
    if command[0] == 'forward':
        movements['forward'] = movements.get('forward', 0) + int(command[1])
        movements['depth'] = movements.get('depth') + (movements.get('aim', 0) * int(command[1]))
    elif command[0] == 'up':
        movements['aim'] = movements.get('aim', 0) - int(command[1])
    elif command[0] == 'down':
        movements['aim'] = movements.get('aim', 0) + int(command[1])


print(movements)
print(f'Final Horizontal: {movements["forward"]} \nFinal Depth: {movements["depth"]}')
print(f'Horizontal * Depth = {movements["forward"] * movements["depth"]}')