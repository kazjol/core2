# https://og7kl7g6h8.feishu.cn/docx/YxcWdNjDCo0bSaxxwnhcOol0nzf


# 保证最前面的数字保留顺序位中更小的 因为这道题有顺序 左边的是高位

NUM1 = input()
n = int(input())
# rest_n 表示剩余的删除次数
rest_n = n




# 构建一个单调栈，
# 单调栈从栈底至栈顶单调递增
# 即大的数字放在栈顶
stack = list()

# 遍历数字字符串NUM1中的每一个字符ch
for ch in NUM1:
    # 出栈的情况：
    # 1. 栈不为空
    # 2. ch小于栈顶元素
    # 3. 剩余的删除次数大于0
    # 即可以弹出栈顶元素，这样才能使得栈顶元素尽可能小
    while len(stack) and ch < stack[-1] and rest_n > 0:
        stack.pop()
        rest_n -= 1
    # 对于每一个ch，都应该入栈 最后输出剩下的元素
    stack.append(ch)

# 删除了n次后的数字长度一定为len(NUM1)-n
# 但是结束循环时，栈中元素不一定恰好为len(NUM1)-n
# 即n次删除机会不一定全部用完，rest_n没有降为0
# 所以取较小的数前 len(NUM1)-n 个数组合成字符串
print("".join(stack[:len(NUM1)-n]))
