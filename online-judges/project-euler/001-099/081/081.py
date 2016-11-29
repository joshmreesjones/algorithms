# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
# by only moving to the right and down, is indicated in *starred* numbers and is equal to 2427.

# *131*  673   234   103   018
# *201* *096* *342*  965   150
#  630   803  *746* *422*  111
#  537   699   497  *121*  956
#  805   732   524  *037* *331*

# Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix,
# from the top left to the bottom right by only moving right and down.

filename = "matrix.txt"
matrix = [[int(n) for n in line.strip().split(",")] for line in open(filename, "r").readlines()]

width = len(matrix[0])
height = len(matrix)

count = 0

def min_path_sum(row, col):
    global count
    count += 1
    if count % 1000000 == 0:
        print(count)
        print("107507208733336000000000")

    at_bottom = (row == height - 1)
    at_right = (col == width - 1)

    if at_bottom and at_right:
        return matrix[row][col]

    elif (not at_bottom) and (not at_right):
        sum_down = min_path_sum(row + 1, col)
        sum_right = min_path_sum(row, col + 1)

        return matrix[row][col] + min(sum_down, sum_right)

    else:
        if at_bottom:
            return matrix[row][col] + min_path_sum(row, col + 1)
        elif at_right:
            return matrix[row][col] + min_path_sum(row + 1, col)

print(min_path_sum(0, 0))
