def get_ways(grid, R, C, i, j):
    if i == R-1 and j == C-1:
        # base case
        return 1

    result = 0

    for x in range(i+1, R):
        for y in range(j+1, C):
            if grid[x][y] != grid[i][j]:
                result += get_ways(grid, R, C, x, y)

    return result


with open('h2.in') as fin:
    R, C = [int(part) for part in fin.readline().strip().split()]

    grid = [
        list(fin.readline().strip())
        for _ in range(R)
    ]

    result = get_ways(grid, R, C, 0, 0)
    print(result)
