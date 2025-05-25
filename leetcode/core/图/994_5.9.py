# 腐烂的橘子
# 多源bfs 数组 矩阵
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：0,1,2
# 每分钟2的周围四个方向的1会变成2 返回1全变成2的最小时间 ps：0不受影响

# 对于单源BFS是每次访问整个层 对多源BFS就是对所有的源端都做BFS 一次访问多个整层同时操作


# 对所有的2都访问四个方向 然后标记访问过的2 每次访问所有没有访问过的2
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 用现成的类型队列 能直接调用很多打包好的函数 直接设列表的方法是栈
        q = deque()
        fresh = 0  # 记录新鲜橘子的数量
        time = 0   # 记录时间
        
        # 首先找到所有腐烂的橘子，并统计新鲜橘子的数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # 如果没有新鲜橘子，直接返回0
        if fresh == 0:
            return 0
            
        # BFS处理腐烂过程
        while q and fresh > 0:
            # 处理当前层的所有腐烂橘子
            # 改进了时间计算方式：
            # 使用 size = len(q) 来记录当前层的腐烂橘子数量
            # 每次处理完一层（即同一分钟内的所有腐烂过程）才增加时间
            # 这样可以确保同一分钟内的腐烂过程是同时发生的
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                # 检查四个方向
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1: # 边界判断和是否新鲜判断
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            time += 1
        
        # 如果还有新鲜橘子，返回-1
        return -1 if fresh > 0 else time # 三元运算符 如果fresh>0 返回-1 否则返回time



# od解法
D = [(0, 1), (1, 0), (-1, 0), (0, -1)] # 方便四个方向的访问
class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 初始化答案变量、新鲜橘子数量、网格长宽
        level, fresh_num, x, y = 0, 0, len(grid), len(grid[0])
        # 初始化队列，维护BFS过程
        q = deque()
        # 初始化二维列表，用于BFS过程中的检查
        checkList = [[0] * y for _ in range(x)]
        # 第一次遍历整个二维网格，找到所有初始腐烂的橘子，统计新鲜橘子的个数
        for i in range(x):
            for j in range(y):
                # 找到初始腐烂的橘子
                if grid[i][j] == 2:
                    # 将腐烂的橘子放入队列中
                    q.append((i, j))
                    # 同时修改二维检查列表的对应元素为1
                    checkList[i][j] = 1
                # 找到初始新鲜的橘子
                elif grid[i][j] == 1:
                    # 统计新鲜橘子的数目
                    fresh_num += 1

        # 若新鲜橘子数量为0，则直接返回0
        if fresh_num == 0:
            return 0

        # 进行BFS搜索的循环，套用BFS万能模板
        while len(q) > 0:
            # 获得当前队列长度，为当前层搜索的个数
            qSize = len(q)
            # 搜索层数+1
            level += 1
            # 循环qSize次，出队qSize次
            for _ in range(qSize):
                # 出队
                i, j = q.popleft()

                # 考虑上下左右四个方向的其他位置
                for dx, dy in D:
                    nxt_i, nxt_j = i + dx, j + dy

                    # 满足三个条件
                    # 1. 边界判断 2. 未检查过 3. 新鲜橘子
                    if 0 <= nxt_i < x and 0 <= nxt_j < y and checkList[nxt_i][nxt_j] == 0 and grid[nxt_i][nxt_j] == 1:
                        # 新鲜橘子入队，标记检查，新鲜橘子数目-1
                        q.append((nxt_i, nxt_j))
                        checkList[nxt_i][nxt_j] = 1
                        fresh_num -= 1

        # 若BFS结束，仍存在新鲜橘子，说明有些橘子无法腐烂，返回-1
        # 否则返回level-1，为腐烂所有新鲜橘子所需的时间
        return -1 if fresh_num > 0 else level - 1

# 灵神 这个思路和我原来的思路最像
class Solution3:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0 # 我原来用的是mul操作次数和fresh是反着的定义 但是计算次数是一样的 还有就是fresh更回归题目更好理解
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1  # 统计新鲜橘子个数
                elif x == 2:
                    q.append((i, j))  # 一开始就腐烂的橘子

        ans = 0
        while q and fresh:
            ans += 1  # 经过一分钟
            tmp = q #  一次要做到遍历一层的橘子 也就是当前腐烂的全部橘子 腾空全部队列
            q = []
            for x, y in tmp:  # 已经腐烂的橘子 遍历一整层
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):  # 四方向
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # 新鲜橘子
                        fresh -= 1
                        grid[i][j] = 2  # 变成腐烂橘子
                        q.append((i, j))

        return -1 if fresh else ans


# 测试
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))  # 4




print('\n\ntest:')
# a是初始化的列表 列表的元素是二元组 二元组可索引
# n元组（tuple）在Python中完全可以使用索引访问其中的元素。元组是一个不可变的序列类型，可以通过索引（从0开始）来访问其中的元素。
# 不是所有不可变的数据类型都能用索引。让我解释一下：
# 可以使用索引的不可变数据类型：
# 元组 (tuple)
# 字符串 (str)
# 字节串 (bytes)
# 命名元组 (namedtuple)
# 不能使用索引的不可变数据类型：
# 集合 (set)
# 冻结集合 (frozenset)
# 字典 (dict) - 虽然字典本身是可变的，但它的键必须是不可变的



# 可以使用索引的不可变类型都是序列类型（sequence types），它们的特点是：
# 元素是有序的
# 可以通过位置（索引）访问
# 包括：元组、字符串、字节串等
# 不能使用索引的不可变类型通常是无序的集合类型：
# 集合（set）
# 冻结集合（frozenset）
# 这些类型设计用于快速查找元素是否存在，而不是通过位置访问
# 特殊情况：字典的键
# 字典的键必须是不可变的
# 但字典本身是可变的
# 可以使用不可变类型（如元组、字符串）作为键
# 不能使用可变类型（如列表）作为键
# 所以，更准确的说法是：序列类型的不可变数据类型可以使用索引，而不是所有不可变数据类型都可以使用索引。这是因为索引访问需要元素有固定的顺序，而有些不可变类型（如集合）是无序的。

# 总而言之查找是根据匹配就是哈希类型就是不可索引的
a = []
a.append((1,2))
print(a)
print(a[0][0])
print(a[0][1])
check = [[False,False,False],[True,True,False]]
print(check != True)
check = [[True,True,True],[True,True,True]]
print(check != True)
check = [[1,1],[1,1],[1,1]]
print(check != 1)

# 不可变的数据类型
# 字符串 (str)：
# 一旦创建就不能修改
# 任何修改操作都会创建新的字符串对象
# 元组 (tuple)：
# 有序的不可变序列
# 可以包含不同类型的元素
# 一旦创建就不能修改