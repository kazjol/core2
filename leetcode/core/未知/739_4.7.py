# 给定一个整数数组temperatures ，表示每天的温度，返回一个数组answer ，
# 其中answer[i]是指对于第i天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用0来代替。



# 输出的answer长度和输入数组同样长度
# 遍历temperature从前到后压栈压入温度和索引，遇到大的则索引相减存入answer 然后弹出栈顶元素 继续往后比
# 如果比栈顶元素小则压栈


# 可以通过索引访问temperatures数组来得到用于比较的数值 所以实际不用保存两个数值压栈
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        answer = [0] * n
        stack = []

        # for循环遍历温度 正序遍历
        for i in range(n):

            # if not stack or temperatures[i] > temperatures[stack[-1]]:
            #     stack.append(i)

            # while循环判断何时出栈压栈的条件
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # 索引相减得到answer
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        # 因为初始化的answer数组全为0，所以温度不升高的天不用单独处理 直接保留0就行
        return answer

temperatures =  [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))


print(list(range(0,4,1)))
print(list(range(5)))
# range的用法是（起始，终止，步长）终止是不包含在内的是总长度

