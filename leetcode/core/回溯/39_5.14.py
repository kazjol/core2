# 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。

# 核心还是组合问题，但是这里元素可以重复选择 ps：做回溯这种问题直接就先排序就好了 因为排列和组合都没有说有固定顺序的问题
# 还是要按组合来做
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtrack(subset, start):
            if sum(subset) == target:
                res.append(subset[:])
                return
            # 重复组合：没有start参数，会产生[2,3]和[3,2]这种重复
            # 提前return：找到解后直接return，导致无法继续探索其他组合
            # 递归调用位置错误：for循环外的backtrack(subset)没有意义 不会因为for循环而重复调用函数而形成递归

            # 递归的核心是for循环的重复调用函数
            for i in range(start, len(candidates)):
                # 剪枝
                if sum(subset) + candidates[i] > target:
                    continue
                subset.append(candidates[i])
                # 剪枝
                if sum(subset) > target:
                    continue    
                if sum(subset) == target:
                    res.append(subset[:])
                else:
                    backtrack(subset, i)
                subset.pop()  # 必须！每次append都要pop

        backtrack(subset, 0)
        return res
'''
    很重要的一点啊 我在想为什么不用判断这层选不到元素满足条件的情况 为什么不用做判断然后return

    但是最重要的一点 ： 当for循环执行完之后还是没有执行到return的语句是会自动返回到上一层的啊
    
    
'''


from typing import List
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtrack(start,subset): # 传start避免重复组合

            for i in range(start, len(candidates)): # for i in range() i自动加1
                if candidates[i] > target:
                    continue
                '''
                  一直都是因为剪枝的错误 导致超限
                '''
                if sum(subset) + candidates[i] > target:
                    continue

                # 没有在每次append后都做pop：
                # 问题在于：没找到解时，你直接递归了，没有pop恢复subset状态。
                # 没有在每次append后都做pop会造成深度超限
                subset.append(candidates[i])
                if sum(subset) == target:
                    res.append(subset[:])
                    # 回溯 pop()后i会自动减1因为退到上一层for循环了
                    subset.pop()
                    return
                else:
                    # 避免重复组合：因为每次只能往后选，所以不会出现[2,3]和[3,2]
                    # 允许重复数字：因为传i而不是i+1，所以可以重复选择当前数字***
                    # 不是完全遍历：每一层的for循环都是从当前i开始，而不是从头开始
                    # 所以传i的设计很巧妙：
                    # 既保证了可以重复选择当前数字
                    # 又避免了重复组合
                    # 还减少了搜索空间
                    backtrack(i,subset) # start的位置传i能保证不回退查找组合 因为一次for i会自动加1 并且向后传到更深的for里
                # backtrack(subset)
                
                '''
                    每次append后都要pop要保证退栈后能正常撤销
                    if 后面的这个pop只有当不执行else也就是找到解后才执行
                '''
                subset.pop()
            # subset.pop() # for循环结束没找到也要重选元素
            # return # 回溯到上一层
        
        backtrack(0,subset)
        return res

class Solution3:
    def __init__(self):
        self.res = []
        self.candidates = []
        self.target = 0

     # 对于传进另一个函数的参数不能直接访问 要先声明

    def backtrack3(self, subset, start): # 这里for循环里加return
        for i in range(start, len(self.candidates)):
            if self.candidates[i] > self.target:
                continue
                
            subset.append(self.candidates[i])
            if sum(subset) == self.target:
                self.res.append(subset[:])
                subset.pop()
                return
            elif sum(subset) < self.target:
                self.backtrack3(subset, i)  # i允许重复使用
            subset.pop()
            


    def backtrack4(self, subset, start):
        for i in range(start, len(self.candidates)):
            if self.candidates[i] > self.target:  # 剪枝
                continue
            if sum(subset) + self.candidates[i] > self.target:  # 剪枝
                continue
            
            subset.append(self.candidates[i])
            if sum(subset) == self.target:
                self.res.append(subset[:])
                subset.pop()
                return
            self.backtrack4(subset, i)
            subset.pop()

    def backtrack5(self, subset, start): # for外加return
        if sum(subset) == self.target:  # 先检查
            self.res.append(subset[:])
            return
        
        for i in range(start, len(self.candidates)):
            subset.append(self.candidates[i])
            self.backtrack5(subset, i)
            subset.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.res = []
        self.subset = []
        # self.backtrack3([], 0)
        self.backtrack4([], 0)
        # self.backtrack5([], 0)
        return self.res
   
    
'''
    根本是因为不剪枝 造成的超限
'''

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))
print(Solution2().combinationSum(candidates, target))
print(Solution3().combinationSum(candidates, target))



