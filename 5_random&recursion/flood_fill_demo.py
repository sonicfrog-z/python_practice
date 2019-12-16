map_ = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

R = len(map_)
C = len(map_[0])

# DO NOT DO THE FOLLOWING
# flooded = [[False] * C] * R
flooded = [[False] * C for _ in range(R)]


def flood_fill(i, j):
    flooded[i][j] = True
    if i > 0 and map_[i-1][j] == 1 and not flooded[i-1][j]:
        flood_fill(i-1, j)
    if i < R-1 and map_[i+1][j] == 1 and not flooded[i+1][j]:
        flood_fill(i+1, j)
    if j > 0 and map_[i][j-1] == 1 and not flooded[i][j-1]:
        flood_fill(i, j-1)
    if j < C-1 and map_[i][j+1] == 1 and not flooded[i][j+1]:
        flood_fill(i, j+1)


islands = 0
for i in range(R):
    for j in range(C):
        if map_[i][j] == 1 and not flooded[i][j]:
            islands += 1
            flood_fill(i, j)

print(islands)