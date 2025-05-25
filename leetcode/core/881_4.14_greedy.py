# 救生艇
# 贪心 数组 双指针 排序
# 看到求最值基本就是要用贪心了 要不然先排序 要不然就是直接局部最优

# 给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回 承载所有人所需的最小船数 。


# 体重最小的配体重最大的
# 如果体重最小的都配不上当前这个的大体重那后面的体重更大的也不用配了
# 先排序然后找出limit体重的人 重划数组然后用双指针
print('mine 贪心 双指针 慢了')
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        boat=0

        for heavy in people:
            if heavy >= limit:
                boat = len(people)-people.index(heavy)

                right = people.index(heavy)-1 # 返回索引数组的下一个数组
                break

        # 一个船最多两个人 贪心算法就是最大体重配最小体重
        # for i in range(left,right+1): 毫无必要的循环 最后决定是否跳出循环的是while的判断 而且left和right在动作结束后会变根本不用生成序列 # ***n遍了range的序列不包含结束
            while left <= right:
                if people[right] + people[left] <= limit:
                    boat+=1
                    left += 1
                    right -= 1
                elif people[left] + people[right] > limit: # 这个重的人配最轻的人也不行 单独一条船

                    right -= 1
                    boat+=1

        return boat
peoples = [7,8]
limit = 8
s = Solution()
print(s.numRescueBoats(peoples, limit))
print(list(range(0,1))) # range(起始，结束)生成的序列不包含结束


print('\n\nod 要快一点我原来多套了一个循环')


class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # 先排序
        people.sort()

        # 获取数组长度
        n = len(people)

        # 寻找两人组

        # 最左边的位置
        left = 0

        # 最右边的位置
        right = n - 1

        # 船的数量
        ans = 0

        while left <= right:

            # 1、如果 people[left] + people[right] <= limit
            # 说明 people[left] 和 people[right] 可以同船

            if people[left] + people[right] <= limit:

                #  此时船的数量加一
                ans += 1

                # 两个指针分别往中间靠拢

                left += 1

                right -= 1


            # 如果 people[left] + people[right] > limit
            # 说明 people[left] 和 people[right] 不可以同船
            else:

                # 由于题目说明了人的重量不会超过 limit
                # people[right] 需要独自坐船，船的数量加一
                ans += 1

                # people[right] 坐船后
                # right 需要向内移动，寻找新的组合
                right -= 1

        # 返回结果
        return ans
people = [1,2,3,1,1,2]
limit = 3
print(Solution2().numRescueBoats(people, limit)) # 3


