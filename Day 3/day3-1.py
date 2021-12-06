# Advent of Code 2021 - Day 3 Part 1
# Author: Camron Miller
# Created: 12/06/2021
# Last Modified: 12/06/2021
# Purpose: 
#   Read in binary diagnostics from a file
#   Determine gamma rate
#       Most common bit in each position out of all entries is the bit of that position
#       Ex. 7 two bit entries have 1 as the first bit. THe most coomon first bit is 1. 
#           Therefore, the first bit of the gamma rate is 1, etc...
#   Determine the epsilon rate
#       Same process as the gamma rate, except is based on the least common bit
#   Determine the power consumption = product of the gamma and epsilon rate

# get data from file
sample = 'day3-sample.txt'
actual = 'day3-input.txt'

fileName = actual

try:
    fh = open(fileName)
except:
    print(f'File {fileName} not found')

diagnostics = [x.strip() for x in fh]

fh.close()

# a dict containing values pertaining to the most common bit for each position
# keys are the index of the bit
# if the value at the key is positive, the most common bit is 1
# if the value at the key is negative, the most common bit is 0
# if the value at the key is zero, neither 1 nor 0 is more common
commons = dict()

for x in diagnostics:
    for i in range(len(x)):
        if x[i] == '1':
            commons[i] = commons.get(i, 0) + 1
        else:
            commons[i] = commons.get(i, 0) - 1

gammaRate = ''
epsilonRate = ''

for x in commons.values():
    if x > 0:
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'

print(f'Power Consumption = {int(gammaRate, 2)} * {int(epsilonRate, 2)}')
print(f'Power Consumption = {int(gammaRate, 2) * int(epsilonRate, 2)}')


