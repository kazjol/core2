# 子集
# 位运算 数组 回溯

# 给你一个整数数组 nums (元素各不相同)，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 子集不能重复

'''
https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/

回溯 基于递归 因为递归会出现退栈的情况 退栈后再选择是否从该点继续递归 尝试和回退（尝试失败后回退）  这就是回溯

回溯法就是暴力搜索对每个点都做尝试，并不是什么高效的算法，最多再剪枝一下。

回溯算法能解决如下问题：

组合问题：N个数里面按一定规则找出k个数的集合
排列问题：N个数按一定规则全排列，有几种排列方式
切割问题：一个字符串按一定规则有几种切割方式
子集问题：一个N个数的集合里有多少符合条件的子集
棋盘问题：N皇后，解数独等等



回溯的关键点：
每次递归都代表一个决策点
在决策点，我们可以选择当前数字或不选择
选择后继续递归，不选择则回溯到上一个状态
回溯时，我们会尝试其他可能的选择


溯的核心思想是：
尝试一个选择
递归处理后续选择
回溯到上一个状态
尝试其他可能的选择
这种"尝试-回溯-再尝试"的过程，就像是在走迷宫：
当你走到一个岔路口时，先选择一条路走下去
如果这条路走不通，就回到岔路口
然后尝试另一条路
直到尝试完所有可能的路径
这就是为什么回溯算法能够系统地"枚举"所有可能的解。
'''
import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp) # 每次进递归先保存结果
            # 退栈时会退到for循环这里 然后j开始用下一个数
            for j in range(i, n): # 这里也是边界条件 因为i<n才能range 遍历结束后开始退栈 回退到for这里
                helper(j + 1, tmp + [nums[j]]) # 入栈位置 所以最后退也退到for 然后继续等到j不满足条件再退栈  [1]+[2] = [1,2] 

        helper(0, []) # 入口
        return res
    

# helper(0, [])
#     ↓
#     helper(1, [1])
#         ↓
#         helper(2, [1,2])
#             ↓
#             helper(3, [1,2,3])
#             ↓
#             res = [[], [1], [1,2], [1,2,3]]

# helper(0, [])
#     ↓
#     helper(1, [1])
#         ↓
#         helper(2, [1,2])  ← 回溯到这里 是i=1 的for 循环这里j在range（1，n）里该选2了 调用的上个helpler
#             ↓
#             helper(3, [1,2,3])
#             ↑
#             退栈

# 1. helper(0, [])
#    res = [[]]  # 添加空集
#    ↓
# 2. helper(1, [1])
#    res = [[], [1]]  # 添加[1]
#    ↓
# 3. helper(2, [1,2])
#    res = [[], [1], [1,2]]  # 添加[1,2]
#    ↓
# 4. helper(3, [1,2,3])
#    res = [[], [1], [1,2], [1,2,3]]  # 添加[1,2,3]
#    ↑
#    退栈到 helper(2, [1,2])
#    ↓
#    继续循环，j=3
#    ↓
# 5. helper(3, [1,3])  # 这里选择3，生成[1,3]
#    res = [[], [1], [1,2], [1,2,3], [1,3]]  # 添加[1,3]
#    ↑
#    退栈到 helper(2, [1,2])
#    ↓
#    继续循环，j=4，循环结束
#    ↑
#    退栈到 helper(1, [1])
#    ↓
#    继续循环，j=2
#    ↓
# 6. helper(3, [1,3])  # 这里会重复添加[1,3]，但不会影响结果
#    ↑
#    退栈到 helper(1, [1])
#    ↓
#    继续循环，j=3，循环结束
#    ↑
#    退栈到 helper(0, [])
#    ↓
#    继续循环，j=1
#    ↓
# 7. helper(2, [2])
#    res = [[], [1], [1,2], [1,2,3], [1,3], [2]]  # 添加[2]
#    ↓
# 8. helper(3, [2,3])
#    res = [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]  # 添加[2,3]
#    ↑
#    退栈到 helper(2, [2])
#    ↓
#    继续循环，j=3，循环结束
#    ↑
#    退栈到 helper(0, [])
#    ↓
#    继续循环，j=2
#    ↓
# 9. helper(3, [3])
#    res = [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]  # 添加[3]

# 每次递归都会把当前子集加入结果
# 当递归到最深处时，开始回溯
# 回溯时退到上一层的 for 循环
# 继续尝试下一个可能的数字
# 通过 j + 1 确保不会重复选择同一个数字
# 回溯的特点：
# 深度优先：先尝试一条路径到最深处
# 回溯：当一条路径走完后，退回到上一个决策点
# 尝试：在决策点尝试其他可能的路径
# 剪枝：通过 range(i, n) 避免重复选择

# 库函数 这里其实就是二项式
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i): # 二项式 n选m个
                res.append(tmp)
        return res

print('test1:',list(itertools.combinations([1,2,3,4], 2))) # 二项式 n选m个并把结果返回成列表


# 迭代 这个思路太绝了
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res] # 这里res是元素为列表的列表 所以[i]+num是列表相加 并把推到的结果都加到列表里
        return res

print('test2:',[[1] + i for i in [[2],[3],[4]]])

# 回溯模板
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        # 结果集合
        sets = []

        # 每次的子集
        subset = []

        # 执行回溯算法
        self.backtrack(0, nums, subset, sets) # 入口 self.成员函数 同类里的访问

        # 返回结果
        return sets
    
    # 回溯算法模块
    def backtrack(self, i, nums, subset, sets):
        """
        :param i: int
        :param nums: List[int]
        :param subset: List[int]
        :param sets: List[List[int]]
        """
        # 每次确定好一个子集，都把它加入到结果集合中 每次都先加进去再入栈
        # 这是因为 Python 中列表是可变对象（mutable object），当你直接使用 sets.append(subset) 时，你实际上是在 sets 中添加了对 subset 列表的引用，而不是 subset 的副本。这意味着：
        # 当你后续修改 subset 时（比如通过 subset.pop() 或 subset.append()），所有通过引用指向这个列表的地方都会受到影响
        # 在回溯算法中，subset 会被反复修改（添加和删除元素），如果直接添加引用，那么 sets 中存储的所有子集都会指向同一个列表，最终它们都会变成相同的状态


        # subset[:] - 使用切片语法创建浅拷贝
        # subset.copy() - 使用 copy() 方法创建浅拷贝
        # copy.copy(subset) - 使用 copy 模块的 copy() 函数创建浅拷贝
        # copy.deepcopy(subset) - 使用 copy 模块的 deepcopy() 函数创建深拷贝

        sets.append(subset[:]) # 这种写法是复制了一份


        # 1、画递归树
        # 2、寻找结束条件，由于回溯算法是借助递归实现，所以也就是去寻找递归终止条件
        # 本题中可以不加这个判断，大家可以思考一下为什么可以不加，结合 for 循环的边界来思考
        if i >= len(nums):
            return

        for j in range(i, len(nums)): # 递归边界 每层的选择 每层入栈时的实参i都是上一层入栈时的实参i+1也是j+1 后续退栈再选的时候j会取下一个数
            # 把本次递归访问的元素加入到 subset 数组中  subset子集
            subset.append(nums[j])

            # 4、判断是否需要剪枝，去判断此时存储的数据是否之前已经被存储过
            # 本题不需要剪枝

            # 5、做出选择，递归调用该函数，进入下一层继续搜索
            # 递归
            self.backtrack(j + 1, nums, subset, sets) # 递归退栈位置

            # 6、撤销选择，回到上一层的状态  更新j的值 重选然后生成新子集 退栈时才会执行pop 
            # 取消对 nums[i] 的选择
            # 在for 循环里 当退栈时执行pop（）然后要选下一个数也就是j+1所以在for内
            subset.pop() 
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):  # 枚举全集 U 的所有子集 i
            subset = [x for j, x in enumerate(nums) if i >> j & 1] # 根据j决定这个i子集里面的元素是选和不选
            # 例如 对于对i=4来说 100 通过j遍历全部的nums的元素 然后通过二进制与来决定当前遍历的这个元素是否会被选到这个子集里
            # 100&001 10&01 1&1 0&1  0 0 1 0 取nums[2] 结果为1的那个是j=2时的结果nums[2]选 从100从低到高也可以看出nums[2]选
            ans.append(subset)
        return ans


    # 对于输入的 nums，考虑每个 nums[i] 是选还是不选，
    # 由此组合出 2^n个不同的子集。
    
    # dfs 中的 i 表示当前考虑到 nums[i] 选或不选。


    # 递归深度最大三层 所以有2^3的叶子
    #                       []
    #                      /  \
    #                 选1 /    \ 不选1
    #                    /      \
    #                 [1]        []
    #                /  \       /  \
    #           选2 /    \不选2选2/   \不选2
    #              /      \    /      \
    #           [1,2]   [1] [2]      []
    #          /   \   /   \ /  \    /  \
    #     选3 / \不选3选3\不选3选3\不选3选3\不选3
    #        /     \  /    \ /   \  /    \
    #   [1,2,3] [1,2][1,3][1][2,3][2][3]  []
    #    return  return return return return return return return