# 爱生气的书店老板
# 数组 滑动窗口

# 在customers数组中找到满足条件的最大值
# 当grumpy[i]为1时，customers[i]不被计入最大值之中
# 当grumpy[i]为0时，customers[i]被计入最大值之中
# 窗口大小为minutes
# 窗口内的所有customers[i]的和都被计入最大值之中



# 思想：从全部满意客人最多转成了 挽留客人最多******
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        unsatisfied = [c * g for c, g in zip(customers, grumpy)] # zip 函数合并成元组 for c,g 遍历元组并生成c*g列表值
        # 当grumpy[i]为0 时也就是不生气时客人一定是满意的 当grumpy[i]为1时客人不满意 不满意人数乘1 得到的还是不满意人数
        # 所以unsatisfied列表中存放的是 正常情况下的不满意人数 这部分可以由滑动窗口减少
        # 且列表里保存的还是原始的客人的顺序
        # 现在只需遍历列表使得定长滑动窗口中原来不满意的人数达到最大值即可

        win_sum = sum(unsatisfied[:minutes]) # 初始化第一个窗口
        # print(unsatisfied)
        # print(win_sum)

        max_win_sum = win_sum


        

        for right, num in enumerate(unsatisfied[minutes:], minutes): # 遍历第一个窗口后元素
            # A1
            win_sum += num
            # A2
            left = right - minutes # 这种移左边界更方便
            win_sum -= unsatisfied[left]
            # A3
            # 还是统计窗口内不满意的最多人数是多少 让这部分人满意就得到最大值
            max_win_sum = max(max_win_sum, win_sum)



        # 总人数 - 原本总不满意人数 + 克制住没生气挽回的不满意人数 = 最终满意人数
        return sum(customers) - sum(unsatisfied) + max_win_sum


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print('od',Solution().maxSatisfied(customers,grumpy,minutes)) # 16