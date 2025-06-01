# https://og7kl7g6h8.feishu.cn/docx/Fiv6dtHbWo0qDUxE5HwciJnvnNg
from typing import List
# 经典题型
# 单调栈 找第一个比当前元素大的元素
def friend(n:int,height:List[int]) -> str: # 返回字符串
    stack = [] # 单调递减栈 保存索引
    ans = [0]*n
    for i in range(n): # 遍历每个身高
        h = height[i]

        while stack and height[stack[-1]] < h:
            pre_h = stack.pop() # 被比较的小朋友索引
            ans[pre_h] = i

        stack.append(i) # 栈顶大当前身高索引入栈

    # return ans 需要输出带空格的字符串
    return ' '.join(str(i) for i in ans) # join()的参数必须可迭代且元素类型为字符串 join返回的类型也是字符串


n = int(input())
height = list(map(int,input().split()))
print(friend(n,height))
