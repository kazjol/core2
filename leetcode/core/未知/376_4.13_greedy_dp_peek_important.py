# 摆动序列
# 贪心 数组 动态规划
# 贪心 每次都是局部最优解
# 例如： 计算数组中的最值 遍历数组每次用当前元素去比较更新全局最值的记录

'''
动态规划 难且重要
基础题目： 斐波那契 爬楼梯
背包问题 打家劫舍问题
股票问题
子序列

****
dp数组的定义及下标的含义
dp数组怎么初始化是0还是1
遍历顺序
打印dp数组可以查错

***递推公式
'''



# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。
# 仅有一个元素或者含两个不等元素的序列也视作摆动序列。
# 例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。
# 相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
# 子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。
# 给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

# 示例：
# 输入：nums = [1,17,5,10,13,15,10,5,16,8]
# 输出：7
# 解释：这个序列包含几个长度为 7 摆动序列。
# 其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
# 1,17,5,10,5,16,8 17后面选降的能选好几个





# 降维处理 转摆动（增减）为单增单减子序列来解决 单增单减序列为常见的dp问题 要多刷几道dp序列问题
# 这种将为的思维非常的好 找波峰波谷的思路
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        核心思想：
        把数组的全部数 按照顺序和大小写出来 然后能观察到
        数组元素不是严格递增或递减的 中间存在单增减子数列
        在这些单增减的子数列中随意选取一个元素 都能形成一个摆动序列 并且是最长子序列

        问题：当增减性连续变化 需要保存两个元素  例如：对1 17 5 10 在17和5这里需要保存17和5
             当增减性不是连续变化的时候此时只需要弹出一个元素 例如对于 1 17 20 5 2在17这里只用保存17
             所以一次按道理只能存一个元素 但是会遇到需要保存两个元素的情况 所以一保存次只清空一个数组
             清空的数组是取决于是上升下降 还是下降上升导致的 如果是上升下降则清空上升队列 否则清空下降队列



              连续变化时会同时产生波峰和波谷所以需要保存两个

        '''
        inc, dec, n = 0, 0, len(nums) # 记录增减性 以及数组长度
        up = []
        down = []
        ans = [] # 记录最长摆动序列
        ans.append(nums[0]) # 第一个元素 一定存在
        tip = 0 # 记录最近一次是上升还是下降
        i  = 1 # 遍历数组的下标
        if n == 2: # 数组长度为2
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        elif n >= 3:
            while i < n:
                if nums[i] > nums[i-1] : # 按道理应该越界但是列表是会逆回去的nums[-1] == nums[n-1]
                    up.append(nums[i]) # 记录上升子数列
                    tip = 1
                    inc = 1

                elif nums[i] < nums[i-1] :
                    down.append(nums[i]) # 记录下降子数列
                    tip = -1
                    dec = 1

                if inc + dec == 2: # 增减性发生变化 单增单减结束

                    if tip == 1: # 最近一次上升 弹出下降的队列的一个元素
                        ans.append(down.pop())  # 下降队列弹出一个
                        dec = 0 # 重置增减性
                        down = []

                    else: # 最近一次是下降 弹出上升队列的一个元素
                        ans.append(up[0])  # 上升队列弹出一个
                        inc = 0 # 重置增减性
                        up = []

                i += 1

            if inc == 1 or dec == 1: # 最后一个元素是上升或下降的 单独记录
                ans.append(nums[n-1])

        print('ans:',ans)
        return len(ans)

nums = [1,17,5,10,13,15,10,5,16,8]
print(Solution().wiggleMaxLength(nums)) # 输出 7






print('\n\nod 解法单增减子序列')

# https://www.algomooc.com
# 作者：程序员吴师兄
# 代码有看不懂的地方一定要私聊咨询吴师兄呀
# 摆动序列(376):https://leetcode-cn.com/problems/wiggle-subsequence/
class Solution2:

    # 这里代码写的易读性和结构很漂亮，值得学习 尤其是像是用beginState来初始化状态 而不是直接用0来初始化
    # 因为beginState不仅易读而且还是个变量

    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 每个元素都有三种状态

        # 1、每个元素的初始状态
        beginState = 0

        # 2、如果当前元素的值大于它之前元素的值
        # 比如 nums[i] > nums[i-1]
        # 那么说明当前元素处于上升阶段，状态设置为 up
        upState = 1

        # 3、如果当前元素的值小于它之前元素的值
        # 比如 nums[i] < nums[i-1]
        # 那么说明当前元素处于下降阶段，状态设置为 down
        downState = 2

        # 如果 nums 长度小于 2
        if len(nums) < 2:
            # 由于仅有一个元素或者含两个不等元素的序列也视作摆动序列
            # 直接返回数组的长度
            return len(nums)

        # 以第一个元素作为初始的摇摆序列，此时，长度为 1
        length = 1

        # 一开始，状态为 begin
        state = beginState

        # 接下来，开始遍历 nums 中的所有元素
        for i in range(1, len(nums)):
            # 每个元素都有三种状态，在这三种状态下去判断这个元素应该怎么操作

            ''' 
                思路和上面的解法一样，只是这里没有用到数组 而是直接根据是否连续变化来输出保存的元素个数
                连续就保存2 不连续就保存1 也就是每次都是保存波峰和波谷的值
                连续变化时会同时产生波峰和波谷所以需要保存两个
                       
            '''

            # 1、如果是在 begin 状态
            if state == beginState:
                # 那么比较 nums[i] 和  nums[i-1] 的大小

                # 此时的元素值为 nums[i]，它前面的元素值为 nums[i-1]
                # 如果 nums[i] > nums[i-1]，代表着现在处于上升过程
                if nums[i] > nums[i - 1]:
                    # 状态修改为 up
                    state = upState
                    # 摆动序列中增加了 nums[i] 这个元素，所以 length 需要加 1
                    length += 1

                # 此时的元素值为 nums[i]，它前面的元素值为 nums[i-1]
                # 如果 nums[i] < nums[i-1]，代表着现在处于下降过程
                elif nums[i] < nums[i - 1]:
                    # 状态修改为 down
                    state = downState
                    # 摆动序列中增加了 nums[i] 这个元素，所以 length 需要加 1
                    length += 1

            # 2、如果是在 up 状态
            # 说明 nums[i] 的前面两个元素 nums[i-2] < nums[i-1]，正在处于上升过程
            elif state == upState:

                # 只有此时 nums[i] < nums[i-1]
                # 那么 nums[i-2]，nums[i-1]，nums[i] 这三者形成一个波峰  ^
                if nums[i] < nums[i - 1]:
                    # 此时，由于 nums[i] < nums[i-1]，开始处于下降状态了
                    # 状态修改为 down
                    state = downState
                    # 摆动序列中增加了 nums[i] 这个元素，所以 length 需要加 1
                    length += 1
            # 3、如果是在 up 状态
            # 说明 nums[i] 的前面两个元素 nums[i-2] > nums[i-1]，正在处于下降过程
            elif state == downState:

                # 只有此时 nums[i] > nums[i-1]
                # 那么 nums[i-2]，nums[i-1]，nums[i] 这三者形成一个波谷 V
                if nums[i] > nums[i - 1]:
                    # 此时，由于 nums[i] > nums[i-1]，开始处于上升状态了
                    # 状态修改为 up
                    state = upState
                    # 摆动序列中增加了 nums[i] 这个元素，所以 length 需要加 1
                    length += 1

        # 返回结果 length
        # 不需要返回具体序列

        return length
# 这个和我刚开始想的 inc和dec的思路完全一样 但是我当时没改出来一些问题
nums = [1,17,5,10,13,15,10,5,16,8]
print(Solution2().wiggleMaxLength(nums)) # 输出 7


# 波峰波谷的判断方法 可以直接套用inc dec 和tip标
print('\n\n最开始的思路 只用inc和dec')
from typing import List
class Solution3:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 还是只保存波峰波谷

        inc, dec,tip, n = 0,0, 0, len(nums) # 记录增减性 以及数组长度
        lenth = 1 # 记录最长摆动序列

        i  = 1 # 遍历数组的下标
        if n == 2: # 数组长度为2
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        elif n >= 3:
            while i < n:
                if nums[i] > nums[i-1] : # 按道理应该越界但是列表是会逆回去的nums[-1] == nums[n-1]
                    inc = 1
                    tip = 1
                elif nums[i] < nums[i-1] :
                    dec = 1
                    tip = -1

                if inc + dec == 2: # 增减性发生变化 单增单减结束

                    # 问题一开始在于不能一次性全部重置inc和dec
                    if tip == 1: # 最近一次上升 下降重置
                        lenth += 1
                        dec = 0 # 重置增减性
                    else: # 最近一次是下降 上升重置
                        lenth += 1
                        inc = 0 # 重置增减性

                i += 1

            if inc == 1 or dec == 1: # 最后一个元素是上升或下降的 单独记录
                lenth += 1


        return lenth

nums = [1,17,5,10,13,15,10,5,16,8]
print(Solution3().wiggleMaxLength(nums)) # 输出 7

