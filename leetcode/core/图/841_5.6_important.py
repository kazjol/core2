# 钥匙和房间
# bfs dfs
# 拿到钥匙才能开房间 0号房间可以直接进



'''
   主要区别：
访问顺序：
BFS：一层一层访问，保证访问顺序
DFS：一条路径走到底，再回溯
数据结构：
BFS：使用队列（queue）存储待访问的节点
DFS：使用递归调用栈存储访问路径
适用场景：
BFS：适合找最短路径
DFS：适合找可行解
实现方式：
BFS：用 while 循环维护队列 while维护的是一层的所有元素
DFS：用 for 循环尝试所有可能路径 栈保存的是全部当下能访问的元素
所以你的理解是对的：BFS 的关键是 while 循环来维护队列，而 DFS 的关键是 for 循环来尝试所有可能的路径。这是两种搜索策略的本质区别。
'''

from typing import List
from functools import lru_cache

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 标记访问过的房间 最后数组长度等于房间数目则说明全部访问过
        visited = []
        # bfs每次用一个房间有的所有钥匙访问完 再访问其他的房间
        queue = [0] # 0号房间可以直接进
        key = []
        # 遍历所有房间
        while queue:
            room = queue.pop() # 出队首元素
            visited.append(room) # 标记访问过
            key = rooms[room] # 记录一个房间的所有钥匙
            for k in key: # 全部入队
                if k not in visited: # 未访问过
                    queue.append(k) # 入队
                continue # 跳过已经访问过的钥匙
        if len(visited) >= len(rooms): # 全部访问过
            return True
        else:
            return False

# dfs 把所有拿到的钥匙压栈然后遍历栈 直到栈为空
class Solution2:
    def dfs(self, rooms, cur_room, visited):
        # 如果当前房间已访问，直接返回
        if cur_room in visited:
            return
        
        # 标记当前房间为已访问
        visited.append(cur_room)
        
        # 获取当前房间的所有钥匙，并尝试访问每个新房间
        for key in rooms[cur_room]:
            if key not in visited: # 递归函数的设计一定要设置边界条件啊！！！！要不然怎么退出 
                self.dfs(rooms, key, visited)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = []
        self.dfs(rooms, 0, visited)
        return len(visited) == n


# 使用lru_cache的DFS解法 这个是嵌套dfs的写法不是调用
class Solution3:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()  # 使用集合来记录已访问的房间，查找效率更高
        

        # 内存使用:
        # lru_cache: 有大小限制，适合处理大量数据
        # cache: 无大小限制，适合处理小量数据
        # 使用方式:
        # lru_cache: 需要配置参数（如 maxsize, typed）
        # cache: 直接使用，无需配置
        # 性能考虑:
        # lru_cache: 当缓存满时会删除最久未使用的项，内存使用更可控
        # cache: 会一直增长，直到程序结束，可能占用更多内存

        #         适用场景:
        # lru_cache:
        # 当需要限制内存使用时
        # 当只需要最近的结果时
        # 当参数组合可能很多时
        # cache:
        # 当需要缓存所有结果时
        # 当内存使用不是主要考虑因素时
        # 当参数组合较少时
        @lru_cache(maxsize=128)  # 限制缓存大小为128
        def dfs(room: int) -> bool:
            # 如果房间已访问，返回False
            # 原因1: 避免重复访问，因为已经探索过从这个房间出发的所有路径
            # 原因2: 防止循环访问，比如房间1->2->1->2...的无限循环
            # 原因3: 剪枝优化，避免不必要的递归调用
            if room in visited:
                return False  # 这个False只会返回到调用这个dfs的上一层，不会结束整个递归
            
            # 标记当前房间为已访问
            visited.add(room)
            # 用cache的话需要用到可哈希（按关键字匹配）的类型 需要转list为set
            # 因为list是只能索引的类型 然后就是转成set之后就不能用append了因为这个函数是填新元素到索引末尾 
            # 而可哈希的类型没有索引这一说
            
            # 如果所有房间都已访问，返回True
            # 这说明我们找到了一条可以访问所有房间的路径
            if len(visited) == n:
                return True  # 这个True会一直返回到最顶层，表示找到了答案
                # 一旦找到答案，就不需要继续探索其他路径了
                # 因为我们已经找到了一个可行解
            

            # for 循环是实现 DFS 算法的核心部分，它既保证了能找到答案（如果存在的话），又能在找到答案后快速返回，提高了算法的效率。
            # 尝试访问当前房间能打开的所有房间
            for next_room in rooms[room]:
                # 如果找到一条能访问所有房间的路径，就返回True
                # 这样可以在找到答案后立即返回，不需要继续探索其他路径
                if dfs(next_room):  # 如果找到一条能访问所有房间的路径  这里dfs的返回类型设置的是bool
                    return True  
                    # 如果子路径返回True，说明找到了答案，继续向上返回True
                    # 会在for循环里一直True到底然后返回True
                    # 一旦找到答案，就立即返回，不再尝试其他路径



                # 如果子路径返回False，会继续循环尝试下一个房间
                # 不会立即返回False，而是尝试所有可能的路径
                # 因为当前路径失败不代表其他路径也失败
            
            # 如果从当前房间出发的所有路径都无法访问所有房间，返回False
            # 这个False会返回到调用这个dfs的上一层，让上一层继续尝试其他路径
            return False  # 只有当所有可能的路径都尝试过且都返回False时，才会执行到这里
            # 这确保了不会错过任何可能的解决方案
        
        return dfs(0)  # 从0号房间开始访问


class Solution4:
    def dfs(self, rooms, cur_room, visited):
        # 标记访问
        visited[cur_room] = True
        # 尝试访问当前房间能打开的所有房间
        '''
            对于dfs而言 核心就是这个for循环对的实现 无论是边界条件的设置还是递归的深入 for都是非常核心的   
        '''
        for key in rooms[cur_room]:
            # 如果钥匙不在访问过的房间中 就递归访问 继续往下走继续调用dfs是dfs的体现
            if not visited[key]:
                self.dfs(rooms, key, visited)
            # else:
            #    continue


    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 局部变量初始化全为未访问
        visited = len(rooms) * [False]
        # 递归入口 0号房进入
        self.dfs(rooms, 0, visited)
        # all()都为true才true 所有房间都访问过返回True 否则返回False
        return all(visited)
rooms = [[1,2],[2,1],[1]]
print(Solution().canVisitAllRooms(rooms))
print(Solution2().canVisitAllRooms(rooms))
print(Solution3().canVisitAllRooms(rooms))
print(Solution4().canVisitAllRooms(rooms))




# dfs核心思想：
# dfs(0)
#   ├── 访问房间0
#   ├── 尝试房间1
#   │   ├── 访问房间1
#   │   ├── 尝试房间2
#   │   │   ├── 访问房间2
#   │   │   ├── 尝试房间1 (已访问，返回False)
#   │   │   └── 返回False (因为从房间2出发无法访问所有房间)
#   │   └── 返回False (因为从房间1出发无法访问所有房间)
#   └── 尝试房间2 (继续探索其他路径)
#       ├── 访问房间2
#       ├── 尝试房间1 (已访问，返回False)
#       └── 返回False

# False 的传播：
# 当 dfs 返回 False 时，只是告诉它的调用者"这条路径不行"
# 调用者会继续尝试其他路径
# 只有当所有路径都尝试过且都返回 False 时，才会最终返回 False
# True 的传播：
# 当 dfs 返回 True 时，表示找到了答案
# 这个 True 会一直向上传播到最顶层
# 一旦找到答案，就会立即返回，不需要继续探索其他路径
# 递归的层级：
# 每个 dfs 调用都是独立的
# 返回 False 只会影响当前路径
# 不会影响其他并行路径的探索


# dfs(0)
#   ├── 访问房间0
#   ├── 尝试房间1
#   │   ├── 访问房间1
#   │   ├── 尝试房间2
#   │   │   ├── 访问房间2
#   │   │   └── 发现已访问所有房间
#   │   │   └── 返回True  # 立即返回，不再尝试其他路径
#   │   └── 返回True      # 立即返回，不再尝试其他路径
#   └── 返回True          # 立即返回，不再尝试其他路径


# True 的快速返回：
# 一旦找到答案，立即返回
# 不需要尝试其他路径
# 因为已经找到了一个可行解
# 这提高了算法的效率
# False 的逐层返回：
# 需要尝试所有可能的路径
# 确保不会错过任何解决方案
# 当前路径失败不代表其他路径也失败
# 这保证了算法的正确性