actual = 'day1-input.txt'
sample = 'day1-sample.txt'

file = actual

try:
    fh = open(file)
except:
    print(f'File {file} not found')


depths = [int(x) for x in fh]

if len(depths) < 3:
    exit()

inc = 0
prevDepthsSum = depths[0] + depths[1] + depths[2]

for i in range(3, len(depths)):
    currDepthsSum = depths[i] + depths[i-1] + depths[i-2]

    if currDepthsSum > prevDepthsSum:
        inc += 1

    prevDepthsSum = currDepthsSum

print(inc)
