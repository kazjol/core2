# 省份数量
# dfs bfs 并查集 图
# 返回直接相连或间接相连的连通块的数量 也就是岛屿的数量 间接相连 ab相连 bc相连，则ac间接相连
# 输入n*n矩阵 也就是n个城市 矩阵里的元素代表城市间是否直接相连

# 并查集 合并 查找 集合 并查集的主要作用就是用来做路径压缩 把在同一祖先结点下的结点全部直接连到祖先结点下 使得路径长度为1 但是一般应该要综合考量 因为路径压缩的同时也会影响到单层遍历时间
# 并查集 记录的是父节点的信息 同一个并查集集合的元素的祖先节点是相同的
# 如果有父节点就往上找 直到找到祖先结点




# 在类里面定义局部共享成员 self.成员 只存在于单一的对象内 只能被该对象访问且只有一份
from collections import deque
from typing import List


class UnionFind: # 并查集模板类 里面必须要有的函数
    def __init__(self): # 构造函数初始化对象
        """
        记录每个节点的父节点
        """
        self.father = {} # 初始化父节点
        self.num_of_sets = 0 # 记录集合的数量

    def find(self, x):
        """
        查找根节点
        路径压缩
        """
        root = x
        # 查找祖先
        while self.father[root] != None: # while循环迭代找父亲最后找到找祖先
            root = self.father[root]

        # 路径压缩 逐个向上
        while x != root: # 也就是x有祖先
            original_father = self.father[x] # x的直接父节点是original_father
            self.father[x] = root # 直接把当前的x挂到root祖先结点下面
            x = original_father # x变到保存父节点的信息 然后通过while循环一直迭代 把x的一条向上路径的每个父节点都挂到了root祖先结点下面

        return root

    def merge(self, x, y):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y) # 查找祖先find函数返回的是祖先结点 不是相同祖先则说明是两个连通块->做合并


        if root_x != root_y:
            self.father[root_x] = root_y # 把y挂到x的父节点下面

            self.num_of_sets -= 1  # 合并 集合数量减一



    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y)

    def add(self, x): # 新加结点的关键在于设置其父节点的信息
        """
        添加新节点
        """
        if x not in self.father: # 结点的父节点信息设为空 也就是单独成一个连通块
            self.father[x] = None
            # 新加一个单点 集合的数量+1
            self.num_of_sets += 1



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind() # 初始化空并查集对象
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected [i][j]: # 直接连通
                    uf.merge(i, j)

        return uf.num_of_sets


# dfs解法
class Solution2:
    def dfs(self, isConnected, checkList, i):
        # 对于传入的点i，将其标记为已检查过
        checkList[i] = 1
        # 遍历其他点j
        for j in range(self.n):
            # 1. 若j点未检查过  2. 与i相连  3. j和i不是同一个点
            if checkList[j] == 0 and isConnected[i][j] == 1 and i != j:
                # 对j进行DFS 继续找与j相连的点
                self.dfs(isConnected, checkList, j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 获得城市数量
        self.n = len(isConnected)
        ans = 0
        # 检查列表的长度是n
        checkList = [0] * self.n

        # 遍历每一个点i
        for i in range(self.n):
            # 如果该点没检查过，
            if checkList[i] == 0:
                # 则从点i出发，进行DFS
                self.dfs(isConnected, checkList, i)
                # 做完本次DFS，省份数量+1 得到一个连通块
                ans += 1
        return ans

# bfs解法

class Solution3:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        # 获得城市数量
        n = len(isConnected)
        # 检查列表的长度是n
        checkList = [0] * n
        # 遍历每一个点i
        for i in range(n):
            if checkList[i] == 0:   # 若未i检查过
                q = deque([i])      # 把i加入q中，作为BFS的起始位置 广度优先遍历用队列 deque函数需要一个可迭代的对象作为参数[i]构成了一个单元素列表 元组可以直接加因为元组是可索引的
                checkList[i] = 1    # 将i标记为已检查过
               
               # 按行遍历 而不用看上下 是因为矩阵是对称的 3，4连通则4，3一定连通
                while(q):           # 从i开始，进行BFS
                    x = q.popleft()     # 弹出q队头的点x，考虑与其相连的点y
                    for y in range(n):  # 遍历其他点y，若y点未检查过，且与x相连 x,y只是下标 每次遍历同行的所有元素
                        if x != y and checkList[y] == 0 and isConnected[x][y] == 1:
                            q.append(y)         # 则把y加入队列中 广度遍历保存每个相邻的有效点
                            checkList[y] = 1    # 同时把y标记为已检查过
                # 完成本次BFS，省份（连通块）数量+1
                ans += 1
        return ans

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))