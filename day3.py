import re

with open("day3input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def get_bit_counts(values, idx):
    zero_counts = 0
    one_counts = 0
    for val in values:
        char = val[idx]
        if char == "0":
            zero_counts += 1
        elif char == "1":
            one_counts += 1
        else:
            raise NameError("Bad char")
    return (zero_counts,one_counts)

def get_counts(values):
    zero_counts = []
    one_counts = []
    for idx in range(0, len(values[0])):
        (zc,oc) = get_bit_counts(values, idx)
        zero_counts.append(zc)
        one_counts.append(oc)

    return (zero_counts,one_counts)

def get_gamma_epsilon(values):

    (zero_counts,one_counts) = get_counts(values)

    gamma = ""
    epsilon = ""

    for idx in range(0, len(zero_counts)):
        if zero_counts[idx] < one_counts[idx]:
            gamma += "1"
            epsilon += "0"
        else:    
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return (gamma, epsilon)

def filter_values_with_char_at(values, idx, reqchar):
    res = []
    for val in values:
        if val[idx] == reqchar:
            res.append(val)
    return res

def filter_greater_values(values, idx):
    (zero_counts,one_counts) = get_bit_counts(values, idx)
    reqchar =""
    if one_counts >= zero_counts:
        reqchar = "1"
    else:
        reqchar = "0"
    return filter_values_with_char_at(values, idx, reqchar)    

def filter_lesser_values(values, idx):
    (zero_counts,one_counts) = get_bit_counts(values, idx)
    reqchar =""
    if one_counts < zero_counts:
        reqchar = "1"
    else:
        reqchar = "0"
    return filter_values_with_char_at(values, idx, reqchar)    

oxygen = lines 
pos = 0
while len(oxygen) > 1:
    oxygen = filter_greater_values(oxygen,pos)
    pos += 1

co2 = lines 
pos = 0
while len(co2) > 1:
    co2 = filter_lesser_values(co2,pos)
    pos += 1

(gamma,epsilon) = get_gamma_epsilon(lines)
print(gamma)
print(epsilon)
print(gamma * epsilon)

oxygen = int(oxygen[0],2)
co2 = int(co2[0],2)
print(oxygen)
print(co2)
print(oxygen*co2)

