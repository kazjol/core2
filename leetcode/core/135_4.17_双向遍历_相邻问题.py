# 分发糖果
# 贪心 数组

# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。得分高的只要保证比相邻多就行，而不是高就多得一个
# 例如 ratings = [1,6,5] 可以分发糖果 [1,2,1] 就能保证得分高的孩子比相邻的孩子糖果更多
# 评分相等的孩子的糖果数可以不同
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。


# 找单增单减序列连增减几次 顶端糖果就是几 找到增减性第二次变化的地方然后计算单调序列长度记为顶端值 遇到相同的数值就糖果数置1重新计算单调序列长度
# 单增单减序列大小决定顶峰糖果数目 增减序列从1开始赋值逐个加1


print("mine 改不出来屎山一样")
from typing import List, Tuple


class Solution:
    # 初始化类的函数 初始化的对象
    def __init__(self, ratings: List[int]):

        self.ratings = ratings

    def candy(self, ratings: List[int]) -> Tuple[int,List[int]]: # 能返回两种参数


        n = len(ratings)
        # ratings = [0] + ratings + [0] # 首尾补0 非常重要的方法
        candies = [1]*n
        cur = 0 # 峰值
        inc = 0
        dec = 0
        count = 0 # 记录第一次转折点
        tip = 0 # 记录增减方向
        up = 1 # 记录单增数
        down = 1 # 记录单减数



        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                inc = 1
                up += 1
                tip = 1

            elif ratings[i] < ratings[i-1]:
                dec = 1
                down += 1
                tip = -1


            if dec + inc == 2 and count == 0: # 第一次转折点
                cur = i - 1
                count = 1
                if i == n-1 or ratings[i] == ratings[i+1]: # 如果第一次转折后就是第一个元素最后一个元素

                    if tip == -1:# 先增后减
                        candies[cur] = max(up, down) # 波峰
                        for j in range(1, up):
                            candies[cur-j] = max(up,down)-j
                        for j in range(1, down):
                            candies[cur+j] = max(up,down)-j
                    elif tip == 1: # 先减后增
                        candies[cur] = 1 # 波谷
                        for j in range(1, down):
                            candies[cur-j] = j+1
                        for j in range(1, up):
                            candies[cur+j] = j+1

                    count = 0
                    inc = 0
                    dec = 0
                    up = 1
                    down = 1




            elif dec + inc == 1 and (ratings[i] == ratings[i-1] or i == n-1): # 单调序列
                cur = i-1- up if dec == 1 else i-1 -down
                if inc == 1:
                    candies[cur] = up
                    for j in range(1, up):
                        candies[cur-j] = up-j
                elif dec == 1:
                    candies[cur] = down
                    for j in range(1, down):
                        candies[cur+j] = down-j
                up = 1
                down = 1
                inc = 0
                dec = 0



            elif inc + dec == 2 and count == 1 : # 第二次转折点
                count = 0

                if tip == -1:# 波峰先增后减
                    candies[cur] = max(up, down)
                    for j in range(1, up):
                        candies[cur - j] = max(up, down) - j
                    for j in range(1, down):
                        candies[cur + j] = max(up, down) - j
                elif tip == 1: # 波谷先减后增
                    candies[cur] = 1
                    for j in range(1, down):
                        candies[cur - j] = j + 1
                    for j in range(1, up):
                        candies[cur + j] = j + 1

                up = 1
                down = 1
                inc = 0
                dec = 0



        print(candies)
        return sum(candies),candies # sum函数能求列表元素和


ratings = [1,3,4,5,2]
cand = Solution(ratings) # 设置了初始化函数init函数之后默认的初始化函数就不能为空了 否则会报错 在用该类初始化一个对象的时候就要填参数了
print(Solution(ratings).candy(ratings))


# 双向遍历 贪心
# 从左往右遍历 保证相邻的左边大的比右边多一个（相等的不变） 初始都是一个糖果
# 从右往左遍历 保证相邻的右边大的比左边多一个（相等的不变）
# 从两边开始遍历其实就能包含最大最小的增减序列 最后对两个列表对应位置取max值就解决了波峰波谷 是减序列大还是增序列大的
print("\n\n双向遍历 很好的思路 两边都满足最大就满足相邻最大")
class Solution2:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))] # 另一种初始化列表的方法 甚至没用 for i in range（）遍历
        right = left[:] # 默认开始是第一个元素结束是最后一个元素 步长为一的遍历

        # right = left # 这样用变量初始化 左右两个列表指向同一个内存地址会一起变的 所以要用切片来复制

        # print(right)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        count = left[-1]
        # 初始化顺便包含只有一个小孩的情况 省略一个if判断
        # 并且还包含了最后一个元素的情况 因为下面的循环取max取不到最后一个元素的情况
        # 对于最后一个元素而言没有相邻一说 只需要判断是否比左边的元素大 比左边的元素大则加1


        for i in range(len(ratings) - 2, -1, -1): # 因为是i和i+1比所以要从倒数第二个人开始遍历否则会越界 range函数生成的序列不包括结束的元素
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i]) # max函数还能遍历取最大值 可索引的都可以用

        print(left,'\t',right)
        print(list(max(left[i], right[i]) for i in range(len(ratings)))) # for循环结合max函数每次产生一个数放进list中最后构成一整个列表
        # count = sum(list(max(left[i], right[i]) for i in range(len(ratings))))
        return count



ratings = [1,2,87,87,87,2,1]

print(Solution2().candy(ratings))




