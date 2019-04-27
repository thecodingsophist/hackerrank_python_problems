def countMatches(grid1, grid2):
    # Write your code here
    return
#THESE ARE HELPER METHODS USED IN COUNTMATCHES:

# REDUCE FUNCTION ACCOUNTS FOR WHERE EACH 1 IS, WHERE EACH 1 IS REPLACED WITH
# A NEW LOCATION/MAP: REDUCED_NUM, AND MOD(REDUCED_NUM) GIVES THE HORIZONTAL LOCATION OF THE 1
# WHILE FLOOR(REDUCED_NUM) GIVES THE VERTICAL LOCATION OF THE 1

def reduce(grid):
    reduced = []
    num = 0
    for row in grid:
        reduced_row = []
        for binary in row:
            if binary == '1':
                reduced_row.append(num)
            num += 1
        reduced.append(reduced_row)
    print(reduced)
    return reduced

# THIS METHOD ONLY ACCOUTNS FOR LISTS WITH 2 or GREATER LEN

def find_consecutive_numbers(list):
    i = 0
    a_list = []
    b_list = [list[0]]
    while i+1 < len(list):
        if list[i] + 1 == list[i + 1]:
            new_array = False
            b_list.append(list[i + 1])
        if new_array:
            a_list.append(b_list)
            b_list = []
        new_array = True
        i += 1
    print(a_list)
    return a_list

#find_consecutive_numbers([4, 5, 7, 8])

i=0, 1, 2
a_list = []
b_list = 4, 5
len(list) = 4

list[0] + 1
a_list = [4, 5]




# GLUE FUNCTION GLUES SMALLER PIECES OF 1's INTO ACTUAL REGIONS WHERE ACCORDING TO THE RULES:
# EACH ADJACENT 1 IS (UP/DOWN BUT NOT DIAGONAL) PART OF A UNIQUE REGION.

def glue_horizontally(reduced, grid):
    horizontal_regions = []
    for row in reduced:
        if len(row) == 1:
            horizontal_regions.append([num])
        else:
            pass


    return

if __name__ == '__main__':
    # countMatches(['001', '011', '100'], ['001', '011', '101'])
    # reduce(['001', '011', '100'])
    # glue_horizontally([[2], [4, 5, 7]])
    find_consecutive_numbers([4, 5, 7, 8])
