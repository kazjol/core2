# https://og7kl7g6h8.feishu.cn/docx/AlXmdfpQzoOlQvxrhPxch6MKnRh

lst = ['']
# 处理输入中带字符的问题
s =input()# 元素类型为str的列表
for i,ch in enumerate(s):
    if ch.isalpha():
        lst[-1] += ch # 最后一个字符串直接拼接上字符
    else:
        lst.append('') # 不是字母则要开始存下一个字符串了 在末尾插入一个空字符串 准备做处理

lst = sorted(set(lst)) # 对单词去重后排序
# print(lst)
pre = input() # 读取要匹配的前缀
ans = []
n = len(pre)
# 切片找匹配
for ch in lst:
    if ch[:n] == pre: # ***切片也是取不到末尾元素的*** 所以结尾是n不是n-1
        ans.append(ch)
# print(lst)
# 如果ans长度大于0，说明至少存在一个单词的前缀是pre，输出由所有单词组成的字符串
# 如果ans长度等于0，说明不存在任何一个单词的前缀是pre，返回pre
print(" ".join(ans) if len(ans) > 0 else pre)



