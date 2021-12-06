# Advent of Code 2021 - Day 3 Part 2
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

# take in a list of diagnostic numbers and the current position to check
# determine the most common bit value in the index given
# return a list of numbers with the most common bit value in the given index
def mostCommonBit(numbers, index):
    ones = list()
    zeros = list()
    common = 0

    for x in numbers:
        if x[index] == '1':
            common += 1
            ones.append(x)
        else:
            common -= 1
            zeros.append(x)

    if common < 0:
        return zeros
    else:
        return ones

# take in a list of diagnostic numbers and the current position to check
# determine the least common bit value in the index given
# return a list of numbers with the least common bit value in the given index
def leastCommonBit(numbers, index):
    ones = list()
    zeros = list()
    common = 0

    for x in numbers:
        if x[index] == '1':
            common += 1
            ones.append(x)
        else:
            common -= 1
            zeros.append(x)

    if common < 0:
        return ones
    else:
        return zeros

# get data from file
sample = 'day3-sample.txt'
actual = 'day3-input.txt'

fileName = actual

try:
    fh = open(fileName)
except:
    print(f'File {fileName} not found')

diagnostics = [x for x in fh]

fh.close()

# check to ensure there is data; if there is not, end program
if len(diagnostics) == 0:
    exit()

oxygenList = diagnostics
c02List = diagnostics
# go through list repeatedly and call methods
for i in range(len(diagnostics[0])):
    if len(oxygenList) > 1:
        oxygenList = mostCommonBit(oxygenList, i)

    if len(c02List) > 1:
        c02List = leastCommonBit(c02List, i)

    # check if one value is left in both lists, if so, stop looping
    if len(oxygenList) == 1 and len(c02List) == 1:
        break

print(f'Oxygen Generator Rating = {int(oxygenList[0], 2)}')
print(f'C02 Scrubber Rating = {int(c02List[0], 2)}')
print(f'Life Support Rating = Oxygen Generator Rating * C02 Scrubber Rating')
print(f'Life Support Rating = {int(oxygenList[0], 2) * int(c02List[0], 2)}')
