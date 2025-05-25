# 目标和
# 给你一个非负整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

#  两个状态-+ 还是01背包 遍历所有可能的排列 也是回溯
import collections
from functools import cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.res = 0  # 使用实例变量存储结果 保证该变量在dfs函数中可以被修改存在于整个对象中
        
        def dfs(index, curr_sum):  # 使用curr_sum避免与内置sum函数冲突
            if index == len(nums):
                if curr_sum == target:
                    self.res += 1
                return
            
            dfs(index + 1, curr_sum + nums[index])
            dfs(index + 1, curr_sum - nums[index])
        
        dfs(0, 0)
        return self.res

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            return dfs(index + 1, curr_sum + nums[index]) + dfs(index + 1, curr_sum - nums[index])
        
        return dfs(0, 0)

# 0-1背包动态规划   0-1是一个参数的状态种类  背包容量是要保存几个参数
class Solution3: # 0-1背包 背包容量是要计算状态的个数
        # 背包容量是 (total + target) // 2，其中 total 是数组总和
        # dp[i] 表示装满容量为 i 的背包的方法数
        # 对于每个数字，我们有两种选择：选或不选
        # 状态转移方程：dp[j] += dp[j - num]，表示当前容量 j 的方法数等于不选当前数字的方法数加上选当前数字的方法数
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or total < abs(target): # 有余数不能整除
            return 0
            
        # 背包容量为 (total + target) // 2
        capacity = (total + target) // 2
        
        # dp[i] 表示装满容量i的背包的方法数
        dp = [0] * (capacity + 1)
        dp[0] = 1  # 空集也是一种方案
        
        for num in nums:
            for j in range(capacity, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[capacity]

# 0-1背包递归做法
class Solution4:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(index, curr_sum): # 边界
            if index == n:
                return 1 if curr_sum == target else 0
            
            return dfs(index + 1, curr_sum + nums[index]) + dfs(index + 1, curr_sum - nums[index]) # 计算两种状态的方案数和
        return dfs(0,0)
            
# 二进制+枚举+折半   
# 把原集合拆成两个子集 求每个子集的所有子集和记录 最后对子集和求和和target匹配
class Solution5: 
    def subsets(self, nums: List[int]) -> dict[int, int]: # 求子集和
        cnt = collections.defaultdict(int)
        for i in range(1 << len(nums)): # 生成所有可能的子集数量(不同的元素个数的子集) 1左移n位 也就是range(2^n) 对于长度为 n 的数组，每个元素都有"选"或"不选"两种可能，所以总共有 2^n 种不同的子集
            '''
                如，对于 nums = [1, 2, 3]：
                数组长度是 3
                1 << 3 等于 8（2^3）
                所以 range(1 << len(nums)) 会生成 0 到 7 的数字
                这些数字的二进制表示正好对应所有可能的子集

                0: 000 → []
                1: 001 → [1]
                2: 010 → [2]  010&001 01&01 1&1  0 1 0 取nums[1] 
                3: 011 → [1,2] 011&001 01&01 0&1  1 1 0 取nums[0] nums[1]
                4: 100 → [3]  100&001 10&01 1&1  0 0 1 取nums[2] 结果为1代表当前元素选 当前j=2 nums[2]选
                5: 101 → [1,3]
                6: 110 → [2,3]
                7: 111 → [1,2,3]

                通过 i >> j & 1 可以检查每个位置是否选中
            '''
           
            s = sum(x for j, x in enumerate(nums) if i >> j & 1) # 通过i>>j&1判断得到结果为1则说明当前的元素x nums[j]被选到这个i子集里
            
            '''
                i>>j&1 自动选择i个元素子集的可能的结果 一种元素的选或不选的搭配
                一个i对应一个子集结果 所以是2^n的range（）n个数每个数选或不选有2^n种可能
            '''
            # 在 Python 中，当进行 & 运算时，如果两个数的位数不同，会自动将较短的数用 0 补齐到相同位数。所以：
            # 5 的二进制是 101
            # 1 的二进制是 1，补齐后是 001
            # 然后进行按位与运算：
            # 最右边：1 & 1 = 1
            # 中间：0 & 0 = 0
            # 最左边：1 & 0 = 0
            # 所以 101 & 1 的结果是 001，也就是十进制的 1。
            # 实现了选择第j位

            '''
                对i（2^n）的遍历刚好能满足 每个位置选与不选的结果 其实组合和子集也就是选一些元素和不选一些元素 
                每次都对所有元素做选与不选的搭配
            '''
            # 对于 nums = [1, 2, 3]：
            # i = 0: 000 → 空集 [] 不选012
            # i = 1: 001 → [1] 选0不选12
            # i = 2: 010 → [2] 选1不选02
            # i = 3: 011 → [1, 2] 选01不选2  # 从右到左是低位到高位啊
            # i = 4: 100 → [3] 选2不选01
            # i = 5: 101 → [1, 3] 
            # i = 6: 110 → [2, 3] 
            # i = 7: 111 → [1, 2, 3] 
            cnt[s] += 1
        return cnt

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0
        m = s // 2 #  选正或是选负的个数 缩小了样本搜索空间 后面的子集求结果的部分只用找和为满足该正数或负数的部分
        '''
        首先，s = sum(nums) - abs(target)，这是经过数学推导得到的：
        假设正数集合的和为 pos
        负数集合的和为 neg
        数组总和为 sum
        目标值为 target

        根据题意：
        pos - neg = target
        pos + neg = sum

        通过这两个等式，我们可以得到：
        pos = (sum + target) / 2
        neg = (sum - target) / 2

        所以 m = s // 2 实际上就是：
        我们需要在数组中找到和为 m 的子集
        这个子集就是我们要选为正数的数
        剩下的数就是我们要选为负数的数
        '''

        k = len(nums) // 2 # 分成两段 去选择目标的正负个数
        cnt1 = self.subsets(nums[:k]) # 前半段所有子集求和并记录
        cnt2 = self.subsets(nums[k:]) # 后半段所有子集求和并记录

        return sum(c1 * cnt2[m - x] for x, c1 in cnt1.items())  # 遍历所有关键字（x）和对应的出现次数
    # cnt2[m-x]是关键字m-x的出现次数 也就是和为m-x的子集数量  c1同理
    # cnt2[m-x] c1[x]能对应一种搭配得到目标值  

    # 如果前半段选和=2，后半段需要选和=0
    # 前半段有3种方案（选任意两个1） 任选一个
    # 后半段有1种方案（空集）
    # 总共有 3 * 1 = 3 种组合方案

    # 这就是为什么 c1 * cnt2[m - x] 能表示这种组合的方案数。
    # 它遵循了乘法原理：如果一个事件有 m 种可能，另一个事件有 n 种可能，
    # 那么这两个事件组合起来就有 m * n 种可能。
nums = [1,1,1,1,1]
target = 3
print(Solution().findTargetSumWays(nums,target))
print(Solution2().findTargetSumWays(nums,target))
print(Solution3().findTargetSumWays(nums,target))


'''
其实海明码用的也是这种思路
让我用一个简单的例子来解释为什么遍历 2^n 能实现所有选和不选的可能：

假设 nums = [1, 2, 3]，n = 3，所以 2^3 = 8 种可能：
    每个位置（0,1,2）都有两种选择：选(1)或不选(0)

这就像是一个三位的二进制数，每一位代表一个位置的选择：
   位置:  2  1  0
          ↓  ↓  ↓
   000 = 0  0  0  → 不选3 不选2 不选1
   001 = 0  0  1  → 不选3 不选2  选1
   010 = 0  1  0  → 不选3  选2 不选1
   011 = 0  1  1  → 不选3  选2  选1
   100 = 1  0  0  →  选3 不选2 不选1
   101 = 1  0  1  →  选3 不选2  选1
   110 = 1  1  0  →  选3  选2 不选1
   111 = 1  1  1  →  选3  选2  选1

当我们遍历 0 到 7 时，每个数字的二进制表示正好对应一种选择方案：
    0 (000) → 空集 []
    1 (001) → [1]
    2 (010) → [2]
    3 (011) → [1,2]
    4 (100) → [3]
    5 (101) → [1,3]
    6 (110) → [2,3]
    7 (111) → [1,2,3]

通过 i >> j & 1 可以检查第 j 位是 0 还是 1，从而决定是否选中对应的数

这就是为什么遍历 2^n 能实现所有选和不选的可能：
每个位置有 2 种选择（选或不选）
n 个位置总共有 2^n 种组合
0 到 2^n-1 的二进制表示正好覆盖了所有可能的组合
这就像是一个 n 位的二进制计数器，从 0 数到 2^n-1，每个数字都代表一种不同的选择方案。


'''