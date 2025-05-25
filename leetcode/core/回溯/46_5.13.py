# 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


# 和组合不同 这里for 要出现回退选元素而不是之选之后的元素

# 枚举法做全排列就是全试一遍


# 枚举法的树形结构可视化 (对于数组 [1,2,3])

#                    []
#               (可用: [1,2,3])
#                /    |    \
#               /     |     \
#            [1]     [2]    [3]   (第一层选择)
#       (可用:[2,3]) ([1,3]) ([1,2])
#          /  \     /  \     /  \
#         /    \   /    \   /    \
#      [1,2]  [1,3] [2,1] [2,3] [3,1] [3,2]  (第二层选择)
#     (可用:[3]) ([2]) ([3]) ([1]) ([2]) ([1])
#        |     |     |     |     |     |
#        |     |     |     |     |     |
#    [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]  (最终排列)

# 更详细的枚举过程：
# 第一层：选择第一个位置的元素
#   ├── 选择1：当前排列=[1], 剩余可用=[2,3]
#   ├── 选择2：当前排列=[2], 剩余可用=[1,3]  
#   └── 选择3：当前排列=[3], 剩余可用=[1,2]

# 第二层：选择第二个位置的元素
# 对于 [1] 分支：
#   ├── 选择2：当前排列=[1,2], 剩余可用=[3]
#   └── 选择3：当前排列=[1,3], 剩余可用=[2]
# 对于 [2] 分支：
#   ├── 选择1：当前排列=[2,1], 剩余可用=[3]
#   └── 选择3：当前排列=[2,3], 剩余可用=[1]
# 对于 [3] 分支：
#   ├── 选择1：当前排列=[3,1], 剩余可用=[2]
#   └── 选择2：当前排列=[3,2], 剩余可用=[1]

# 第三层：选择最后一个元素，完成排列
#    [1,2,3]  [1,3,2]  [2,1,3]  [2,3,1]  [3,1,2]  [3,2,1]
from typing import List
class Solution:
    def __init__(self): # 生成类的对象时的自动初始化 说明了类里要用到的共享变量
        self.res = None
        self.subset = None
        self.tmp = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.tmp = nums[:]  # 暂存剩余的元素
        self.subset = []
        self.res = []
        self.backtrace(self.tmp)
        return self.res

    def backtrace(self,tmp:List[int]): # 没有返回值
        if len(tmp)==0:
            self.res.append(self.subset[:])  # 使用切片创建副本 一定别忘了存副本
            return
        for i in range(0,len(tmp)): # 任选一个元素加入序列 每次都要选择全部的元素
            val = tmp[i]  # 先保存要移除的值
            self.subset.append(val)
            self.tmp.remove(val) # 更新tmp
            self.backtrace(self.tmp)
            # 回退操作
            self.subset.pop()  # 移除最后添加的元素 这个千万不能忘啊 没有删除当前选的元素 怎么重选呢
            self.tmp.insert(i, val)  # 将移除的元素放回待取数数组 回退的时候要删除tmp在上面的代码中已经清除的元素 所以无法用tmp[i]访问 需要val缓存


# 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

from typing import List

# 枚举法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        生成数组的所有可能排列
        
        Args:
            nums: 输入数组，不包含重复数字
            
        Returns:
            所有可能的排列列表
        """
        self.res = []  # 存储所有排列结果
        self.cur = []  # 当前正在构建的排列
        self.available = nums[:]  # 可用的数字列表
        
        self._backtrack()
        return self.res
    
    def _backtrack(self) -> None:
        """
        回溯函数，用于生成所有可能的排列
        """
        # 当没有可用数字时，说明一个排列完成
        if not self.available:
            self.res.append(self.cur[:])
            return
            
        # 遍历所有可用数字
        for i in range(len(self.available)):
            # 选择当前数字
            num = self.available[i]
            self.cur.append(num)
            self.available.pop(i)
            
            # 继续构建排列
            self._backtrack()
            
            # 回溯：恢复状态
            self.cur.pop()
            self.available.insert(i, num)



# 对于数组 [1,2,3]，交换法的递归树结构大致如下： 回溯树

#                 [1,2,3]
#                 /  |  \
#                /   |   \
#         [1,2,3] [2,1,3] [3,2,1]  (第一层交换)
#          /  \     /  \    /  \
#         /    \   /    \  /    \
#    [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,2,1] [3,1,2] (第二层交换)

# 树的深度固定
# 每次只做两个数的交换
# 交换法模块 核心思路 ：通过交换元素来生成不同的排列
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        使用交换元素的方式生成全排列
        
        Args:
            nums: 输入数组，不包含重复数字
            
        Returns:
            所有可能的排列列表
        """
        self.res = []
        self.swap_permute(nums, 0)
        return self.res
    
    def swap_permute(self, nums: List[int], start: int) -> None:
        """
        通过交换元素生成排列
        
        Args:
            nums: 当前数组
            start: 当前处理的位置
        """
        # 当处理到最后一个元素时，找到一个排列 存入结果 有点像回溯二叉树 找到叶子再返回
        if start == len(nums):
            self.res.append(nums[:])
            return
        
        # 从当前位置开始，尝试将每个元素交换到当前位置
        for i in range(start, len(nums)):
            # 交换元素
            '''
            python的多重赋值 
            但实际上 Python 在内部已经帮我们处理了这个问题。这行代码的执行过程是：
            Python 会先计算等号右边的值，创建一个临时元组 (nums[i], nums[start])
            然后按照顺序将元组中的值赋给等号左边的变量

            # Python 内部的处理过程
            temp = (nums[i], nums[start])  # 创建临时元组
            nums[start] = temp[0]         # 第一个值赋给 nums[start]
            nums[i] = temp[1]            # 第二个值赋给 nums[i]
            '''
            # 每次交换都是在固定当前位置 得到一个分叉（实际每次交换都会产生多个分叉多个结果） 然后对当前的分叉继续做递归
            nums[start], nums[i] = nums[i], nums[start]
            # 递归处理下一个位置
            self.swap_permute(nums, start + 1)
            # 回溯：恢复交换
            '''
                保证每个分支独立 - 每次循环都从相同的初始状态开始
                确保结果正确 - 不会因为前面的交换影响后面的结果
                实现真正的回溯 - 递归返回时，状态完全还原
                这就是回溯算法的精髓：做选择 → 递归 → 撤销选择，确保每个分支的探索都是独立的！
                真正的重选
            '''
            # 恢复父结点那个叉的状态 选出兄弟结点的状态
            nums[start], nums[i] = nums[i], nums[start]


# 第一层递归 (start = 0):
# [1,2,3] -> 尝试把1和后面的数交换
#   ├── 1和1交换: [1,2,3]  (i=0)
#   ├── 1和2交换: [2,1,3]  (i=1)
#   └── 1和3交换: [3,2,1]  (i=2)

# 第二层递归 (start = 1):
# 对于 [1,2,3]:
#   ├── 2和2交换: [1,2,3]  (i=1)
#   └── 2和3交换: [1,3,2]  (i=2)

# 对于 [2,1,3]:
#   ├── 1和1交换: [2,1,3]  (i=1)
#   └── 1和3交换: [2,3,1]  (i=2)

# 对于 [3,2,1]:
#   ├── 2和2交换: [3,2,1]  (i=1)
#   └── 2和1交换: [3,1,2]  (i=2)


'''
为什么这样能生成所有排列：
每次递归都固定了前面的元素 已完成一个路径的前部分
通过交换，让每个元素都有机会出现在当前位置
递归到下一层时，只考虑后面的元素
回溯时恢复状态，确保每个分支都是独立的
'''
# 交换法
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))   # 添加排列方案
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位
                dfs(x + 1)                           # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换
        res = []
        dfs(0)
        return res



nums = [1,2,3]
print(Solution().permute(nums))
print(Solution2().permute(nums))



