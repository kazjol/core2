# https://ahym1n4sq5.feishu.cn/docx/IqcjdzdIaoMpncx0cFscBM7HnIc

class Solution:
    def simplifyPath(self, path: str) -> str:

        # 分割字符串为列表形式
        names = path.split("/") # 这个方法也能解决多//问题 例如/// 会保存''空  /两端为空   split()函数返回元素类型为字符串的列表
        # / / /

        # 利用栈来处理
        stack = list()

        # 访问列表里面的元素
        for name in names:
            # 1、如果是 ..
            if name == "..":
                # 在栈不为空的情况下
                if stack:
                    # 弹出栈顶元素
                    stack.pop()
                # 栈为空则不操作 直接跳过 最后返回/开头
            # 2、如果是有效值 不是空字符串 因为split（'/'）会得到空字符串
            # 字母
            elif name and name != ".": # 如果是'.'则说明就是当前目录实际也不用做操作
                stack.append(name)
        # stack = ['Python', 'World', 'Hello']
        # new_string = '/ '.join(stack)
        # print(new_string)
        # 输出结果 Python/ World/ Hello
        # 我们使用/ 作为分隔符，将栈stack中的元素连接成一个新的字符串。
        # 每个元素之间使用/ 进行分隔，因此输出结果中每个元素都以/ 结尾（除了最后一个元素）。
        return "/" + "/".join(stack)



# 字符串直接转列表
a = 'abc'
b = '////a//a'
b = b.split('/')
print(list(a))
print(b)
