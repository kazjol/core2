# 岛屿数量
# ‘1’是陆地‘0’是水 被水完全包围的是岛屿 会给一个n*m的01矩阵，求有多少个岛屿。

# dfs关键
# check记录
# 全方向继续递归
# 边界判断
# 每次完全退出时计数


from typing import List
class Solution:
    def DFS(self, grid:List[List[str]], i:int, j:int):# 没有返回值 只是做修改动作
        self.checked[i][j] = 1 # 标记为已检查过
        for i_next, j_next in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:# 四个方向 i_next,j_next 代表下一个点
            # 越界判断之后做 是否是陆地 并且 未被检查过判断 然后继续往深走调用DFS
            if 0<=i_next<self.x and 0<=j_next<self.y and grid[i_next][j_next]=='1' and not self.checked[i_next][j_next]:
                self.DFS(grid, i_next, j_next)
        # 用self.调用同一Solution类对象的内容

    def numIslands(self, grid: List[List[str]]) -> int:
        self.x = len(grid) # 行数
        self.y = len(grid[0]) # 列数
        self.checked = [[0]*self.y for _ in range(self.x)] # 标记是否检查过
        count = 0
        for i in range(self.x):
            for j in range(self.y):
                if grid[i][j]=='1' and not self.checked[i][j]: # 找到一个陆地 并且 未被检查过
                    self.DFS(grid, i, j) # 开始深度优先搜索 结束后完成checked的标记 然后返回原始ij的位置 并完成一个岛屿的计数
                    count += 1 # 岛屿数量+1
        return count


# 嵌套dfs 还是第一个更好理解一点
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None: # 没有返回值 也可以不写->None就是默认没有返回值
            # 出界，或者不是 '1'，就不再往下递归
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'  # 插旗！避免来回横跳无限递归
            # 对四个方向调用递归
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走

        ans = 0
        # 遍历整个矩阵 对每个人点调用递归
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '1':  # 找到了一个新的岛
                    dfs(i, j)  # 把这个岛插满旗子，这样后面遍历到的 '1' 一定是新的岛 dfs调用结束会返回到开始的点
                    ans += 1
        return ans



grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid)) # 1