# 课程表II
# 和207题类似，但是要返回学习顺序  实际存在多个正确的学习顺序 但是只用返回一个

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        result = [] # 新增保存结果的列表
        
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
            
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
            
        while queue:
            pre = queue.popleft()
            result.append(pre) # 修完一个课程 加入结果列表
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
                
        return result if len(result) == numCourses else []

class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(i, adjacency, flags, result):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags, result): return False
            flags[i] = -1
            result.append(i) # 标记为-1 表示已经修完这个课程 加入结果队列
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        result = []
        
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            
        for i in range(numCourses):
            if not dfs(i, adjacency, flags, result): return []
            
        return result[::-1] if len(result) == numCourses else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))
print(Solution2().findOrder(numCourses, prerequisites))
