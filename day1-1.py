actual = 'day1-input.txt'
sample = 'day1-sample.txt'

file = actual

try:
    fh = open(file)
except:
    print(f'File {file} not found')


depths = [int(x) for x in fh]

inc = 0

for i in range(len(depths)):
    if i == 0:
        prevDepth = depths[i]
        continue

    if prevDepth < depths[i]:
        inc += 1

    prevDepth = depths[i]

print(inc)
