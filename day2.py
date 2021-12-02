import re

with open("day2input.txt") as f:
    lines = f.readlines()


x = 0
y = 0
aim = 0

for line in lines:
    match = re.match(r"(\w*)\s(\d*)", line)
    if not match:
        raise NameError("Expected match")

    dir = match.group(1)
    count = int(match.group(2))

    #print(f"Dir {dir}, count {count}")

    if dir == "forward":
        x += count
        y += aim * count
    elif dir == "up":
        aim -= count
    elif dir == "down":
        aim += count
    else:
        raise NameError("Unknown dir")

print(x)
print(y)
print(x*y)
