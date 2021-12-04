import re

numbers = []
tables = []

with open("day4input.txt") as f:
    numbers = [int(x) for x in f.readline().strip().split(",")]
    while True:
        blank = f.readline()
        if blank == "":
            break
        table = []
        for i in range(0,5):
            line = f.readline().strip()
            matches = re.findall(r"\d+", line)
            table.append([int(x) for x in matches])
        tables.append(table)

def check_row(table, row_idx):
    for col_idx in range(0,5):
        if table[row_idx][col_idx] != -1:
            return False 
    return True

def check_col(table, col_idx):
    for row_idx in range(0,5):
        if table[row_idx][col_idx] != -1:
            return False 
    return True

def apply_number_to_table(table, number):
    for row_idx in range(0,5):
        for col_idx in range(0,5):
            if table[row_idx][col_idx] == number:
                table[row_idx][col_idx] = -1
                if check_row(table,row_idx):
                    return True 
                if check_col(table,col_idx):
                    return True
                return False
    return False

def find_winner(numbers, tables):
    for num in numbers:
        for table in tables:
            if apply_number_to_table(table, num):
                return (num,table)

def find_last_winner(numbers, tables):

    res = (0,None)
    for num in numbers:
        new_tables = []
        for table in tables:
            if apply_number_to_table(table, num):
                res = (num,table)
            else:
                new_tables.append(table)
        tables = new_tables

    return res

def sum_numbers(table):
    sum = 0
    for row_idx in range(0,5):
        for col_idx in range(0,5):
            if table[row_idx][col_idx] >= 0:
                sum += table[row_idx][col_idx]
    return sum

(win_num,win_table) = find_last_winner(numbers,tables)

print(win_num * sum_numbers(win_table))

print("Read")
