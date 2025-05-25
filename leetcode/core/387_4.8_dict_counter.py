# 字符串第一个唯一字符
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 遍历然后存储每个字符为字典 最后遍历字典找到第一个值为一的key
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.defaultdict()
        for i,num in enumerate(s): # i为索引，num为字符 字符串是可以索引的
            if num in dic.keys():
                dic[num] += 1 # +=是一个完整的赋值操作
            else:
                dic[num] = 1 # dic[num]num直接作为关键字 不用加''  加了''关键字就变成'num'了
        for i,num in enumerate(s):
            if dic[num] == 1: # 找到第一个值为一的key
                return i

        return -1

string = "loveleetcode"
print(Solution().firstUniqChar(string)) # 0


# od解法
# 本题涉及到 Python 的一些语法知识
# Python常用内置函数、方法、技巧汇总
# https://og7kl7g6h8.feishu.cn/docx/AbbMdd4YHoGeQRxRGKJcJZs6nDb
from collections import Counter
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        # Counter 可以直接统计字符串、列表等可迭代对象的元素频率 可索引就可以用Counter 且Counter对象是一个字典类型
        # s = "leetcode"
        # cnt = Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
        cnt = Counter(s)
        print(cnt)

        # 如果想在for循环中同时获得列表的索引 i 和元素值 v
        # 可以使用枚举内置函数 enumerate()
        for i, v in enumerate(s):
            # 如果找到了某个字符出现的频率为 1
            if cnt[v] == 1:
                # 返回它的下标即可
                return i

        # 如果不存在，则返回 -1
        return -1



print("*************************************************************************************")
# 对于字典而言就是根据关键字搜索修改值 进行对比的只需要是关键字
dic = {'a':1,'b':2,'c':1}
dic['a']+= 1
print(dic)