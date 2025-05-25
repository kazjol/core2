# 子集II
# 给你一个整数数组 nums ，其中可能包含重复元素和78的区别，请你返回该数组所有可能的 子集（幂集）。

'''
# 1、枚举法画多叉树 每个结点都是子集

# 2、但是对于回溯树（二叉树）来说只有叶子结点才是子集 所以对于二叉树要选到最后一个树 确定一条完整的路径才能加入子集
  只需要找定一个元素 然后往后做选或不选的决策 画完一整棵二叉树 
  每次都是递归到最深（叶子） 然后退栈（退到上一层）（删除末尾元素重选） 记录路径 存为子集
  退到上一层可以记录相邻点的路径
  
# 二叉树的代码的逻辑是：先每个都选 然后每次退栈再选择不选 然后重复操作 
  二叉分别是 选/不选

'''

'''
枚举
'''

# []
# ├── 选1 → [1]
# │   ├── 选2 → [1,2]
# │   │   └── 选3 → [1,2,3]  (for循环结束) 退栈  
# │   └── 选3 → [1,3]  (for循环结束) 退栈
# │   
# ├── 选2 → [2]
# │   └── 选3 → [2,3]  (for循环结束) 退栈
# └──  选3 → [3]  (for循环结束) 退栈 
# 
#     1      2     3
#    / \    / 
#   2   3  3
#  / 
# 3   
# 
# 


'''
二叉树
'''
# []
# ├── 选1
# │   [1]
# │   ├── 选2
# │   │   [1,2]
# │   │   ├── 选3
# │   │   │   [1,2,3]
# │   │   └── 不选3
# │   │       [1,2]
# │   └── 不选2
# │       [1]
# │       ├── 选3
# │       │   [1,3]
# │       └── 不选3
# │           [1]
# └── 不选1
#     []
#     ├── 选2
#     │   [2]
#     │   ├── 选3
#     │   │   [2,3]
#     │   └── 不选3
#     │       [2]
#     └── 不选2
#         []
#         ├── 选3
#         │   [3]
#         └── 不选3
#             []

#                             []
#                 /                       \
#       选1    [1]                      不选1  []
#          /           \                 /           \
#   选2 [1,2]     不选2 [1]      选2 [2]      不选2 []
#      /     \         /   \         /    \         /    \
# 选3[1,2,3]不选3[1,2]选3[1,3]不选3[1]选3[2,3]不选3[2]选3[3]不选3[]



'''
二叉树法必须完整确定一条路径（从根到叶子），才会加入子集
枚举法在递归过程中不断变化 path，每次变化都会加入结果集

1:结果集加入时机：
    枚举法：每次递归前先将 path 加入结果集（标记为 ✓）
    选和不选二叉树法：只有递归到 i == n 时才将 path 加入结果集（标记为 ✓） 完整的确定一条路径（可能后面的多层都不选）才加入结果集
2:递归结构：
    枚举法：通过 for 循环枚举每个数，递归结构更扁平
    选和不选二叉树法：显式分为“选”和“不选”两个分支，递归结构更像二叉树
3:跳过重复数的方式：
    枚举法：通过 j > i and nums[j] == nums[j-1] 跳过重复数
    选和不选二叉树法：通过 while 循环跳过所有等于 nums[i] 的数
'''
from typing import List

# 枚举法的模块化
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 方便取子集 处理重复元素
        res = []
        subset = []
        self.backtrack(nums, 0, subset, res)
        return res
    
    # 这个回溯的模块 采用的是枚举法
    # 枚举法 在回溯的时候通过for循环选后续的元素 不会选之前选过的 eg：[1,2,2] 选了第一个2后 回溯到第一个2 不会选第二个2 因为第一个2已经选过了 j不会回退只会向前 选同层没选过的元素
    # eg2：[1,2,3]对 第一层此时i=0 能选1，2，3 但是当选1时j能选2，3 当选2时j能选3 但是当选3时j=3 j只能向前 没有下一层可选 不满足j<len(nums) 退出for循环 回溯到上一层  
    # 所以子集的元素顺序不会出现逆序的情况 

    def backtrack(self, nums, start, subset, res): # 没有返回值 只做操作
        res.append(subset[:]) # 这里要新建副本 否则会导致子集共享
        for i in range(start, len(nums)): # for进行重选元素
            if i > start and nums[i] == nums[i-1]: # 处理重复元素 i>start 也就是同层重选元素 这种情况要跳过
                continue # 跳过重复元素 不放入子集
            subset.append(nums[i]) # 不同层的重复元素正常处理
            self.backtrack(nums, i+1, subset, res)
            subset.pop() # 回溯 弹出当前元素选下一个元素

# 思路和模块化的一样 是枚举法
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            ans.append(path.copy())  # 也可以写 path[:]

            # 在 [i,n-1] 中选一个 nums[j]
            # 注意选 nums[j] 意味着 [i,j-1] 中的数都没有选
            for j in range(i, n):
                # 如果 j>i，说明 nums[j-1] 没有选
                # 同方法一，所有等于 nums[j-1] 的数都不选
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)  # 选下一层
                path.pop()  # 恢复现场

        dfs(0)
        return ans



# 思路不同 是选和不选的回溯二叉树 非模板化 把选和不选体现的非常清晰
class Solution3:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None: # 只有一个参数就是当前要决定选不选的元素 这种方法是对nums的每个元素做一次dfs 比枚举来说要慢
            if i == n: # 边界条件 选到最后一个数了 那么当前这条路径也就确定了需要退栈了 加入结果集
                ans.append(path.copy())  # 也可以写 path[:]
                return # 退栈 可能到dfs（i+1）也可能到dfs（i）

            # 选 x
            x = nums[i]
            path.append(x)
            dfs(i + 1) # 选完一种后 退栈到这里 然后接着往下执行 pop（）
            path.pop()  # 恢复现场 把这层选的元素删除 也就变成了不选这个元素 也就是下面的部分

            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中，这就重复了
            i += 1
            while i < n and nums[i] == x: # 跳过全部相等的数
                i += 1
            dfs(i) # 选同层下一种元素 这个元素就变成了当前的x

        dfs(0) # 递归入口

        # return 会退栈到调用当前 dfs 的地方
        # 只有从 dfs(i + 1) 退栈回来时，才会执行 path.pop()
        # 从 dfs(i) 退栈回来时，会直接结束当前递归层
        return ans

# 二叉树的回溯方法模块化
class Solution4:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 1. self. 定义的变量
        # 这是实例变量（instance variable），属于类的每一个对象（实例）单独拥有。
        # 只要通过 self. 定义（如 self.res），这个变量可以在该对象的所有方法中访问和修改。
        # 不是所有实例共享，而是同一个实例的所有方法共享。

        # 2. 在函数内直接定义的变量（如 res = []）
        # 这是局部变量，只在该函数内部可见和可用。
        # 其他方法/函数无法访问这个变量。

        # 3. 类变量（class variable）
        # 如果你在类体内（不是方法里）直接写 res = []，那是类变量，会被所有实例共享。 也就是对类
        # 但 self.res = [] 是实例变量，每个实例一份。 
        # 类变量在类中所有方法中共享，而实例变量在每个实例中独立存在。 也就是对对象
        self.res = [] 
        self.subset = []
        self.backtrack(0,nums) # 从0开始 入口
        return self.res
    def backtrack(self,i:int,nums:List[int]):
        if i == len(nums):
            self.res.append(self.subset[:])
            return
        # 选
        self.subset.append(nums[i])
        self.backtrack(i+1) # 选完一种后 退栈到这里 然后接着往下执行 pop（）不选
        self.subset.pop() # 回溯 弹出当前元素选同层下一个元素

        # 不选
        # 跳过全部相同元素
        i = i+1
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1  
        self.backtrack(i) # 选同层下一种元素 这个元素就变成了当前的x
        

