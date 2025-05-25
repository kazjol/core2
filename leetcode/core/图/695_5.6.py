# 岛屿的最大面积
# 计算岛屿的最大面积
from collections import deque
# 还是先找岛屿只不过在每次的最后加上一个面积判断
from typing import List
# DFS
class Solution:
    def DFS(self, grid:List[List[int]], i:int, j:int):# 返回面积
        self.checked[i][j] = 1 # 用self.调用就可以调用整个类里有定义过的成员 且是同一对象的成员 改变的也是同一份
        self.area += 1
        for i_next, j_next in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0<=i_next<self.x and 0<=j_next<self.y and grid[i_next][j_next] == 1 and self.checked[i_next][j_next] == 0:

                self.DFS(grid, i_next, j_next)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.x = len(grid)
        self.y = len(grid[0])
        self.checked = [[0] * len(grid[0]) for _ in range(len(grid))]
        self.area = 0
        res = 0
        for i in range(self.x):
            for j in range(self.y):
                if grid[i][j] == 1 and self.checked[i][j] == 0:
                    self.DFS(grid, i, j)
                    res = max(res, self.area)
                    self.area = 0 # 找完一个岛屿后重置面积
        return res

# BFS
# 初始化上下左右四个方向的数组 二元组列表
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x_len, y_len = len(grid), len(grid[0])       # 获得网格长宽
        ans = 0                                      # 初始化陆地数目为0
        # 初始化和grid一样大小的二维数组checkList用于DFS遍历过程中的检查
        # 二维矩阵的初始化 x行y列 x项每项y个元素
        checkList = [[0] * y_len for _ in range(x_len)]
        # 双重遍历grid数组
        # 行优先
        for i in range(x_len):
            for j in range(y_len):
                # 若该点为陆地且还没有进行过搜寻
                # 找到了一个BFS搜索的起始位置(i,j)
                if grid[i][j] == 1 and checkList[i][j] == 0:
                    # 对于该片连通块，构建一个队列，初始化包含该点
                    q = deque()
                    q.append((i,j))
                    # 修改checkList[i][j]为1，表示该点已经搜寻过
                    checkList[i][j] = 1
                    # 进行BFS之前，初始化该连通块的面积为0
                    area = 0
                    # 进行BFS，退出循环的条件是队列为空
                    # BFS的核心就在while
                    while len(q) > 0:
                        # 弹出栈队头的点(x,y) 搜寻该点上下左右的近邻点
                        x, y = q.popleft()
                        area += 1
                        # 遍历(x,y)上下左右的四个方向的近邻点
                        # 访问二元组构成的列表
                        for dx, dy in DIRECTIONS:
                            x_next, y_next = x+dx, y+dy
                            # 如果近邻点满足三个条件
                            # 1. 坐标在网格内    2. 未检查过    3. 该点为陆地 越界判断和满足条件的判断
                            if (0 <= x_next < x_len and 0 <= y_next < y_len and checkList[x_next][y_next] == 0
                                    and grid[x_next][y_next] == 1):
                                    # 对近邻点做两件事：
                                    # 1. 入队       2. 标记为已检查过
                                    q.append((x_next, y_next))
                                    checkList[x_next][y_next] = 1
                    # 更新答案
                    ans = max(ans, area)
        return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid)) # 6
print(Solution2().maxAreaOfIsland(grid)) # 6
