

with open("day1input.txt") as f:
    lines = [int(x) for x in f.readlines()]

count = 0
for i in range(3, len(lines)):

    sa = 0
    for i2 in range(i-3, i):
        sa += lines[i2]
    
    sb = 0 
    for i2 in range(i-2, i+1):
        sb += lines[i2]

    if sb > sa:
        count += 1

print(count)
