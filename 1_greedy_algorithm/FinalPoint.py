''' 
There is a player who can move to right, left, up, down.
The player start from (1,1) and can only move one cell at one time.
The cell size of place is N x N.
Return the x, y of the cell where player placed.

e.g.
input               output
5                   3 4
R R R U D D
'''
# Starting point
x, y = 1, 1
# Set the size of place
n = int(input())
# Get an characters of L, R, U, D 
plans = input().split()

# The way of moving
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        # Find out next movement.
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # If the next movement is over the place, ignore the next step.
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny 

print(x, y)