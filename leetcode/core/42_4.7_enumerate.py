# 接雨水 单调栈经典问题 困难

# 讲解链接：https://www.bilibili.com/video/BV1VN411J7S7/?vd_source=584c3163bb422497e2633945b1038f8b
# 1、压栈一直压到后面元素比栈顶更大的时候停止压栈
# 2、记录三根柱子的高度 中间的柱子是栈顶元素 左边的柱子是栈顶元素的后一个 右边柱子是待入栈元素
# 结束后保留的高度为右边柱子的高度 也就是这个坑填平了 然后就可以弹出栈顶元素了 继续以之前的左边柱子为栈顶元素继续算 如果没有左边柱子了就把当前待入栈元素入栈后继续往后
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        water = 0
        # 要记录索引和高度值来算 待求面积的宽和高
        for i, h in enumerate(height):  # 前面是索引后面是高度
            while st and h>= height[st[-1]]:  # 后面的元素大于栈顶 栈顶存的是索引啊啊啊啊


                # 保存中间柱子的值
                bottom = height[st.pop()]  # 因为栈里存入的是索引

                # 写了st.pop()之后栈顶元素就已经弹出了

                # 存左边柱子 如果没有左边柱子就直接跳出循环 压当前元素入栈 这些都是在while下的
                if not st:
                    break
                else:
                    wid = i - st[-1] - 1
                    h_left = height[st[-1]]
                    heigh = min(h_left, h) - bottom
                    water = water + (heigh * wid)


            st.append(i)


        return water

 # ***如果想栈里保存索引和值 就直接保存索引就好了 因为值可以通过索引访问得到
 # 栈的核心有一点就是栈里保存的是索引

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(heights)) # 6





st=[]
height=[0,1,0,2,1,0,1,3,2,1,2,1]
for i,h in enumerate(height):# 前面是索引 后面是值
    while st and height[i]>=st[-1]:
        bottom = height[st.pop()]

        print(bottom)
        print(i,h)
    if not st:
        st.append(i)




s = [1,2,3,4]
import collections
d = collections.defaultdict()
for i,h in enumerate(s): # 前面的是索引，后面的是值
    d[i] = h
print(d)


