# 遍历字符串 s ，使用哈希表统计 “各字符数量是否 >1 ”。
# 再遍历字符串 s ，在哈希表中找到首个 “数量为 1 的字符”，并返回。
# 字符统计： 遍历字符串 s 中的每个字符 c 。
# 若 dic 中 不包含 键(key) c ：则向 dic 中添加键值对 (c, True) ，代表字符 c 的数量为 1 。
# 若 dic 中 包含 键(key) c ：则修改键 c 的键值对为 (c, False) ，代表字符 c 的数量 >1 。
# 查找数量为 1 的字符： 遍历字符串 s 中的每个字符 c 。
# 若 dic中键 c 对应的值为 True ：，则返回其索引。
# 否则，返回 -1 ，代表不存在数量为 1 的字符。

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {} # 初始化字典
        for c in s:
            dic[c] = not c in dic # 为不在字典里的字符赋值 True
        for i, c in enumerate(s): # enumerate 同时返回索引和值
            if dic[c]:
                return i
        return -1
s = "aaabbbbccsab"
print(Solution().firstUniqChar(s))



# 字符串中的第一个唯一字符
# 遍历字符串还是用ASCII码来存字母和出现次数
# 取索引值为1的字母与字符串做匹配 并记录匹配次数 匹配次数最小的输出
# 因为最后不仅要取到出现一次的 还要输出元素 既要匹配还要输出元素
class Solution:
    def firstUniqChar2(self, s: str) -> int:  # 返回类型是int

        from collections import Counter
        cnt = Counter(s)
        count = 0
        for key, nums in cnt.items():  # i是字符串元素
            count += 1
            if nums == 1:
                return count # 因为返回类型是int所以直接用return就行了
                break


        return -1


s = "aaabbbbccsaber"
print(Solution().firstUniqChar2(s))

