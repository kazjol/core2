# 跳跃游戏
# 贪心 数组 动态规划

# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

# 示例
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#       nums[0] = 2 最多可以跳两步 nums[1] = 3最多可以跳三步
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


# 显而易见的动态问题且涉及最大最小也可以用贪心 但是如何用贪心来解决 动态问题解决一般都是降维找波峰波谷 找子序列
# 思路：并且这种一般都是从后往前推并且取最值->贪心

# 从后往前遍历取能到达当前位置的跳跃数最大的

print("mine 递归dp+贪心 慢了")
from functools import cache
from typing import List


@cache
class Solution:
    def jump(self, nums: List[int]) -> int:
       # 初始位置
        jump_count = 0  # 记录最小跳跃次数
        cur = len(nums) - 1
        # 递归
        # 函数里面写函数就行了

        def max_jump(cur: int, jump_count:int) -> int: # 函数内函数就不用在指明对象self了
            tmp = []

            if cur > 0:  # 循环执行
                for i in range(cur - 1, -1, -1):  # 从后往前遍历 且结束位置取不到
                    if cur - i <= nums[i]:  # 能跳到
                        tmp.append(i)  # 加到数组里
                        i -= 1  # 继续往前
                cur = min(tmp)  # 下一个跳的位置
                jump_count += 1  # 跳一次
                return max_jump(cur, jump_count) # 函数内函数调用自身不用slef.
            else:
                return jump_count  # 到达最后一个位置

        return max_jump(cur, jump_count)

nums = [2,3,1,1,4]
print(Solution().jump(nums))  # 2



# 递归函数的设计：递归外层函数不会主动进入内部的递归函数 会直接执行内部语段 要用return进入递归函数
# 递归函数内部调用自己不用加self.   self.是同一个类里的不同成员函数之间的互相调用才要用到的
# 且内层为递归函数本身该函数就是在类的成员函数里的 所以函数声明的时候不用写self

# 报错是报错行行下一行执行失败


print('\n\nod解法纯贪心 很快')

# 贪心：每次都选择下一步能跳到最远的位置 然后更新当前位置 直到到达最后一个位置
# 因为遍历是每次跳都选的最远 所以一定是最优解
# 因为题目保证一定能跳到所以每次跳最远就行

class Solution2:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0  # 记录最小跳跃次数
        now_pos = 0  # 当前位置

        while now_pos < len(nums) - 1:  # 继续跳

            max_pos = nums[now_pos] + now_pos # 记录能跳到的最远位置

            if max_pos >= len(nums) - 1:  # 到达最后一个位置
                jump_count += 1
                return jump_count


            for i in range(now_pos + 1, max_pos + 1):  # 遍历当前和边界中的所有位置
                # 对比能跳到的位置哪一个下一步能跳最远 由于是每次跳完一个位置都循环遍历
                # 所以有很多不同的解但是 每次一定选的是最优
                # 其实每个题目的最优跳法都有多种
                if i + nums[i] > max_pos:  # 能跳到更远的位置
                    max_pos = i + nums[i]  # 更新能跳到的最远位置
                    now_pos = i  # 更新当前位置

            jump_count += 1  # 跳一次
            print(f'{jump_count}step nowpos:{now_pos}->{nums[now_pos]}')
        return jump_count



nums = [2,4,2,1,4,1,1,1,1]
print(Solution2().jump(nums))




# 两层while和一层for 一次while绝对不行执行速度太慢 一定会超时



















