

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    #print(grid)
    #print n
    curX = startX
    curY = startY
    visited = [[False for i in range(n)] for j in range(n)]
    distance = [[0 for i in range(n)] for j in range(n)]
    stack = []
    stack.append((curX,curY,0))
    distance[curX][curY] = 0
    visited[curX][curY] = True
    while len(stack)!=0:
        elem = stack.pop(0)
        #elem_dis = distance[elem[0]][elem[1]]
        curX = elem[0]
        curY = elem[1]
        dist = elem[2]
        #print("popped elem = " + str(elem))
        # up
        tx = curX
        ty = curY
        while tx>=0 and tx<n and ty>=0 and ty<n:
            if grid[tx][ty]=="X":
                break
            if visited[tx][ty] == False:
                visited[tx][ty]=True
                distance[tx][ty]=dist+1
                stack.append([tx,ty,dist+1])
            tx+=1
        # down
        tx = curX
        ty = curY
        while tx>=0 and tx<n and ty>=0 and ty<n:
            if grid[tx][ty]=="X":
                break
            if visited[tx][ty] == False:
                visited[tx][ty]=True
                distance[tx][ty]=dist+1
                stack.append([tx,ty,dist+1])
            tx-=1
        # left
        tx = curX
        ty = curY
        while tx>=0 and tx<n and ty>=0 and ty<n:
            #print tx, ty
            if grid[tx][ty]=="X":
                break
            if visited[tx][ty] == False:
                visited[tx][ty]=True
                distance[tx][ty]=dist+1
                stack.append([tx,ty,dist+1])
            ty-=1
        # right
        tx = curX
        ty = curY
        while tx>=0 and tx<n and ty>=0 and ty<n:
            if grid[tx][ty]=="X":
                break
            if visited[tx][ty] == False:
                visited[tx][ty]=True
                distance[tx][ty]=dist+1
                stack.append([tx,ty,dist+1])
            ty+=1
        #print(stack)
    return distance[goalX][goalY]
n= input()
grid = []
for i in range(n):
    row = raw_input()
    grid.append(row)
coords = raw_input()
coords = coords.split(" ")
startX = int(coords[0])
startY = int(coords[1])
goalX = int(coords[2])
goalY = int(coords[3])
num_of_turns = minimumMoves(grid,startX,startY,goalX,goalY)
print "\n****************************"
print num_of_turns
