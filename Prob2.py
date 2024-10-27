##################################################
# Name:Jacob Rosales
# Collaborators: none
# Estimate of time spent (hr): 1
##################################################

def is_magic_square(square):
    n = len(square)
    if not all(len(row) == n for row in square):
        return False

    target_sum = sum(square[0])

    for row in square:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        if sum(square[row][col] for row in range(n)) != target_sum:
            return False

    if sum(square[i][i] for i in range(n)) != target_sum:
        return False

    if sum(square[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    return True


small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

