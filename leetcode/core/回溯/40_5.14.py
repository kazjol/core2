# 组合综合II
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。 选完后跳过 只遍历后续元素
# 
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def backtrack(start, target,sub): # 超时
            
            if sum(sub) == target:
                res.append(sub[:])
                return


            for i in range(start,len(candidates)):
                # 剪枝
                if candidates[i] > target: # 同层选后续的元素
                    continue
                elif candidates[i] + sum(sub) > target: # 同层选后续的元素
                    continue
                # 跳过重复元素的选择避免重复组合 要加在for循环里 保证是选同层元素的时候跳过该元素实现i+1 而不是进入更深层的递归
                # 如果进入下层递归 相同的元素不受影响正常选择 只有同层选其他元素的时候需要跳过同元素
                # 下层还是要保存这个选项 因为下层可选同元素

                # if candidates[i] == candidates[i - 1]:

                #     continue

                sub.append(candidates[i])
                backtrack(i+1,target,sub)
                sub.pop()
        # 去重 单独去重
        # 使用set去重
        # res = list(set(tuple(t) for t in res))
        # 元组可哈希 列表不可哈希 要用set去重只能先转成可哈希的数据类型
        # 元组(tuple)是可哈希的(hashable)，但有一个重要前提：元组中的所有元素也必须是可哈希的。
        # 元组包含不可哈希的元素（如列表）
        # t4 = (1, [2, 3], 4)  # 列表是不可哈希的

        # # 会报错
        # s = {t4}  # TypeError: unhashable type: 'list'
        # d = {t4: 'value'}  # TypeError: unhashable type: 'list'
        # {}是字典类型

        # 可哈希的类型：
        # - 数字（int, float, decimal）
        # - 字符串（str）
        # - 元组（tuple，但要求元素都是可哈希的）
        # - frozenset
        # - None
        # - bool

        # 不可哈希的类型：
        # - 列表（list）[]
        # - 字典（dict）{}
        # - 集合（set） ()

        # 列表(list)是不可哈希的(unhashable)，因为列表的内容可以随时变化所以没办法用匹配的方法来查找 而可哈希的类型则没有索引的概念无法通过索引查找




        #                                []
        #                             sum.txt = 0
        #                         (可用:[1,1,2,3])
        #                        /    ~~|~~   |   \
        #                       /       |     |    \
        #                      1       1      2     3
        #                   sum.txt=1    (跳过)  sum.txt=2  sum.txt=3
        #             (可用:[1,2,3])        /    \  
        #            /     |     \         2      3  *只能选后面的元素（前面的元素都做剪枝） 因为前面的元素已经作为同层分支结点做递归了 如果不选后面的元素 就会重复
        #           /      |      \     sum.txt=4   sum.txt=5
        #          1       2       3      ✓     (剪枝)
        #       sum.txt=2    sum.txt=3    sum.txt=4
        #      /    \        \      ✓
        #     2      3        3
        #   sum.txt=4 sum.txt=5     sum.txt=5
        #     ✓   (剪)       (剪)

        # 注释说明：
        # ~~1~~ : 同层重复的1被跳过
        # ✓     : 找到有效解(和为4)
        # (剪)  : 和超过4，剪枝
        # (跳过): 同层重复元素跳过

        # 找到的组合：
        # [1,3]
        # [2,2]

        # 同层重复元素的处理（第一层的第二个1被跳过）
        # 向后选择的原则（每个节点只能选择后面的数）
        # 剪枝时机（sum.txt > target时停止）
        # 找到有效解的情况（sum.txt == target）

        def backtrack2(start, curr_sum, sub):
            # 使用curr_sum替代sum(sub)，提高效率
            if curr_sum == target:
                res.append(sub[:])
                return
            
            for i in range(start, len(candidates)):
                # 优化剪枝条件
                if curr_sum + candidates[i] > target:
                    break  # 因为数组已排序，后面的数更大，一定也会超过target 而且不用单独判是否超过target这个式子可以满足
                
                # 跳过同层的重复元素
                '''
                    i > start: 这个条件确保我们只在同一层级比较，而不是和上一层的选择比较 最重要的
                    start 算是进入该层递归的开始 也就是层级 start后面是在该层选择不同的元素 也就是i的遍历实现的部分
                    无论进入哪层递归 都是从start开始 
                    分清楚start和i的关系
                
                '''
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                sub.append(candidates[i])
                '''
                    从i+1而不是start是因为不能重复组合 而且i+1能避免重复选择元素
                    i之前的元素 会作为同层的不同选择产生分支结点继续往后递归 没必要折返到头去重复遍历 而且这样还会导致重复组合
                '''
                backtrack2(i + 1, curr_sum + candidates[i], sub)
                sub.pop()
        
        # 使用backtrack2
        backtrack2(0, 0, sub)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))



