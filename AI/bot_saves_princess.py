#!/usr/bin/python


def displayPathtoPrincess(n, grid):
    # locate m and p
    m_i, m_j = 0, 0
    p_i, p_j = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'm':
                m_i, m_j = i, j
            if grid[i][j] == 'p':
                p_i, p_j = i, j

    # print(m_i, m_j)
    # print(p_i, p_j)

    # from m to p
    if p_i > m_i:
        for i in range(p_i - m_i):
            print("RIGHT")
    else:
        for i in range(m_i - p_i):
            print("LEFT")

    if p_j > m_j:
        for i in range(p_j - m_j):
            print("DOWN")
    else:
        for i in range(m_j - p_j):
            print("UP")


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
