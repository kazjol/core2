# 给定两个字符串s和t ，判断它们是否是同构的。
# 如果s中的字符可以按某种映射关系替换得到t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
# 也就是两字符串结构相同像是egg和add e映射到a g映射到d 但是abc和add不相同因为映射必须一一对应

class Solution:
#
    def isIsomorphic2(self, s: str, t: str) -> bool:
            return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))

    def isIsomorphic(self, s: str, t: str) -> bool:
# 先拆分字符串形成两个字典 然后判断关键字的出现次数是否能完全匹配
# 先判断字符串长度是否相同 不同则一定无法映射
        if len(s)!= len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] != t[i]:# 先判断是否有重复项 再判断是否映射正确
                return False
            elif t[i] in dict2 and dict2[t[i]] != s[i]:# elif后面不加： 只有else后面紧跟：
                return False
            else:
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]


        print("dict",dict1,dict2)
        return True
# 最后两个映射没有放入字典
s = "bbbaaaba"
t = "aaabbbba"
print(Solution().isIsomorphic(s,t))
print(list(s.index(s[i]) == t.index(t[i]) for i in range(len(s))))
print(list(s.index(s[i]) for i in range(len(s))))
print(list(t.index(t[i]) for i in range(len(s))))

# all（）函数的用法是判断一个列表中的所有元素是否都为真 如果有一个元素为假 则返回假 否则返回真
# t.index(t[i])查找字符串t中第i个字符 在字符串中第一次出现的位置
# range(len(s)) 用法是生成一个从 0 到 len(s) - 1 的整数序列该序列是有序的  可以用来遍历字符串 像是c的用法 for(i=0; i<len(s); i++)
'''
s = "egg"
for num,idx in enumerate(s):
    print(num,idx)
    enumerate()也可以直接用于字符串
'''



