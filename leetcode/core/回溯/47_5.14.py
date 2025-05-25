# 全排列II
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 区别在于nums里会出现重复元素 所以只需要加上一个去重复的步骤即可

# 枚举
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # sorted(nums) 会返回一个结果 不会改变nums
        nums.sort() # 无返回结果但是会改变nums
        self.res = []
        self.backtrack(nums, [], [False] * len(nums))  # 修改：添加used数组
        return self.res

    def backtrack(self, nums, sub, used):  # 修改：参数列表 nums作为实参传进来 自然可以直接在函数内部调用 不用先访问对象再访问成员self.成员 nums不只是传到permute函数里
        if len(sub) == len(nums):  # 边界条件
            self.res.append(sub[:])  # 存副本
            return

        for i in range(len(nums)):  # 修改：遍历所有元素 我之前昏头了 这是全排列不是组合 所以是遍历所有元素而不是遍历之后的元素
            if used[i]:  # 已使用的跳过
                continue
            # 修改：去重逻辑 - 同一层避免选择相同元素 也就是剪枝操作
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            used[i] = True  # 修改：标记使用
            sub.append(nums[i])
            self.backtrack(nums, sub, used)
            # 回溯 最关键的步骤 删除当前层级的选择选其他的元素
            sub.pop()
            used[i] = False  # 修改：取消标记

# 交换 直接在nums上进行交换 不需要额外空间
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(x): # 单参数只有当前位置 嵌套式写法所以不用写出self不用说明在哪个对象里
            if x == len(nums) - 1: # 边界条件确定全部元素的位置
                res.append(list(nums))   # 添加排列方案
                return
            dic = set() # 去重
            for i in range(x, len(nums)): # 遍历当前位置之后的元素依次做交换形成多个结点 和枚举遍历全部元素不同
                if nums[i] in dic: continue # 重复，因此剪枝 重复的元素不做交换 直接跳过当前位置
                dic.add(nums[i]) # 记录当前位置的元素
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位 一次交换确定一个元素 把i位置的元素固定在x位置（交换）
                dfs(x + 1)                           # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换 恢复父节点状态 继续做其他元素的交换
        res = []
        dfs(0) # 从第一个位置开始 递归入口
        return res

"""
    
    组合：
    枚举法：for i in range(start, len(nums))（避免重复）
    或用选/不选二叉树
    排列：
    枚举法：for i in range(len(nums))（遍历全部）
    交换法：for i in range(x, len(nums))（交换固定位置）
        
    组合和排列的区别：
    - 组合：遍历当前位置之后的元素（避免重复），或用选/不选构造二叉树
    - 排列：可用枚举法（遍历全部元素）或交换法（依次交换后面元素到当前位置）


    """


nums = [1,1,2,2]
print(Solution().permuteUnique(nums)) #[[1,1,2],[1,2,1],[2,1,1]]