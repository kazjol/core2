# 课程表
# DFS BFS 拓扑排序

# 给出必修课的数目 想要修一个课还需要先修另一个课 问是否可以修完所有课 也就是是否会出现循环依赖
# 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 这个是拓扑排序的典型问题 出入度的问题 每次都要找到入度为0的节点才能完成一次排序 对于出现多个入度为0的节点时可以任选所以拓扑排序不唯一
# 拓扑排序解决的只是节点的依赖顺序 解决的是先后问题

# 用邻接表方法表示图

# BFS解法
# 1. 建立邻接表
# 2. 遍历邻接表 计算每个节点的入度
# 3. 找到入度为0的节点 全部入队 把其依赖项也就是这些项指向的项（也就是需要先完成这些节点才能修的项）入度-1
# 4. 重复3直到队列为空
from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 让我解释一下为什么在代码中使用 [0 for _ in range(numCourses)] 而不是 [0] * numCourses 来初始化列表。
        # 虽然这两种方法都能创建一个包含 numCourses 个 0 的列表，但它们有一个重要的区别：
        # [0] * numCourses 创建的是一个包含相同对象引用的列表。也就是说，列表中的所有元素都指向同一个整数对象 0。这在处理不可变类型（如整数）时没有问题，因为整数是不可变的。
        # [0 for _ in range(numCourses)] 使用列表推导式，会为***每个位置创建一个新的整数对象***指向不同位置。虽然在这个特定场景下（因为整数是不可变的），两种方法的效果是一样的，但使用列表推导式是一个更好的编程习惯，因为：
        # 它更明确地表达了"为每个位置创建一个新对象"的意图
        # 当处理可变对象时（比如列表或字典），使用 [0] * n 会导致所有元素共享同一个对象，这可能会导致意外的行为
        
        
        # 不过，由于整数（0）是不可变对象，所以即使所有元素都指向同一个 0，也不会造成任何问题。因为：
        # 当你修改列表中的某个元素时（比如 list1[0] = 1），你实际上是在让那个位置***指向一个新的整数对象（1），而不是修改原来的 0
        # ***整数是不可变的***，所以不可能"修改"0这个值本身
       
        # *** for 变量 in的格式所以 for _ in _两边有空格
        indegrees = [0 for _ in range(numCourses)] # 入度in degree度 用这种循环生成列表的方法 而不是直接初始化
        adjacency = [[] for _ in range(numCourses)] # 生成numCourses行 邻接表adjacency list 记录课程之间的依赖关系 这里其实也可以用哈希表（字典） 邻接表行数是项个数 能表示各项指向什么
        queue = deque()
        # 用邻接表建立依赖关系 入度（先修）
        for cur, pre in prerequisites: # prerequisites[i] = [ai, bi] 一个数据是两个元素 分别是cur和其先修课程pre
            indegrees[cur] += 1 # 当前课程入度+1 需要一个先修课pre
            adjacency[pre].append(cur) # 先修课程pre指向当前课程cur   pre项里面加了cur项 邻接表里的一行保存的是需要该项的所有项 也就是该pre项指向的项 画出来就是横向的一串
        # 把入度为0的课程入队
        # 遍历每个课程
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i) # 如果入度为0 则入队访问
        # BFS
        while queue: # 存在入度为0的课程
            pre = queue.popleft()
            numCourses -= 1 # 修了一个课
            for cur in adjacency[pre]: # 依赖项pre指向的项 入度-1
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur) # 入度为0的课程入队
        return not numCourses # 队列为空则说明可以修完

# DFS解法 嵌套式DFS
# 用dfs判断是否有环 也就是在dfs的时候发现待访问的节点正在被访问
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True # 边界设置 访问到已访问的节点说明已经访问到底了可以退出循环了
            if flags[i] == 1: return False # 访问到正在访问的节点说明有环 直接返回False
            flags[i] = 1 # 标记正在访问
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1  # 标记已访问
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)] # 0未访问 1正在访问 -1已访问
        # 建立邻接表
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses): # 遍历课程
            if not dfs(i, adjacency, flags): return False # 发现任一节点有环 则直接返回False 和之前的DFS不同
        return True


# 为什么要对每个节点都调用一次 dfs？
# 图可能不连通：课程依赖关系可能形成多个独立的子图（即有些课程之间没有任何依赖关系），所以必须对每个节点都进行一次 DFS，确保所有课程都被遍历到。
# 检测所有环：只有对每个节点都进行一次 DFS，才能确保不会遗漏任何一个环（即使某些节点没有被其他节点指向，也要检查它们）。
# 构建完整的拓扑序：每个节点都要被访问，才能保证最终的课程顺序是完整的。


from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 用队列实现
        # 初始化 建立邻接表 课程数的行数
        adj = [[] for _ in range(numCourses) ]
        # 初始化 对每个点记录入度
        indgree = [0 for _ in range(numCourses)]
        # 新建队列
        queue = deque()
        # 创建邻接表
        for cur,pre in prerequisites: # 因为一个数据包含两个元素
            indgree[cur] += 1 # 遍历到一项cur存在pre时入度+1
            adj[pre].append(cur) # 把需要pre作为先修的建成一行
        # 找第一个入度为0的点
        for cur,dgree in enumerate(indgree):
            if dgree == 0:
                queue.append(cur) # 入度为0的点入队
        while queue: 
            pre = queue.popleft() # 修完该课 出队 并记录
            numCourses = -1 # 修完一个课
            for i in adj[pre]: # 遍历所有依赖pre的项
                indgree[i] = -1 # 入度减一
                if indgree[i] == 0: # 如果入度为0 则入队
                    queue.append(i)

        return not numCourses # 如果numCourse为0则表示可以修完课程则返回True


# 为什么要对每个节点都调用一次 dfs？
# 图可能不连通：课程依赖关系可能形成多个独立的子图（即有些课程之间没有任何依赖关系），所以必须对每个节点都进行一次 DFS，确保所有课程都被遍历到。
# 检测所有环：只有对每个节点都进行一次 DFS，才能确保不会遗漏任何一个环（即使某些节点没有被其他节点指向，也要检查它们）。
# 构建完整的拓扑序：每个节点都要被访问，才能保证最终的课程顺序是完整的。
# 代码片段说明

# 在对每个节点都调用一次 dfs 时，不会出现重复计算的问题，原因如下：
# 1. 访问标记（flags/visited）机制
# 在 DFS 拓扑排序的实现中，通常会有一个 flags 或 visited 数组来记录每个节点的访问状态：
# 0：未访问
# 1：正在访问（递归栈上）
# -1：已经访问完成（递归栈下）
# 每次进入 dfs(i, ...) 时，都会先检查 flags[i] 的状态：
# 如果是 -1，说明这个节点已经被完整遍历过了，直接返回 True，不会重复递归。
# 如果是 1，说明遇到了环，直接返回 False。
# 只有 0 时才会真正递归下去。
# 2. 只会对每个节点递归一次
# 每个节点在第一次被递归访问时，会被标记为 1（正在访问），递归完成后标记为 -1（已访问）。
# 之后即使外层循环再次调用 dfs(i, ...)，也会因为 flags[i] == -1 直接返回，不会重复递归。
numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))
