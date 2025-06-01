# 找到字符串中的所有字母异位词
# 哈希表 字符串 滑动窗口

# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 是指由相同字母组成，但排列不同的字符串。

# 异位词->哈希表 匹配来做 关键字字符 值索引

from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        index = []

        count = len(p) # 窗口大小方便返回首字母索引
        p_count = Counter(p) # 统计 p 中每个字符出现的次数 做匹配

        intermedia = Counter() # 记录当前滑动窗口中每个字符出现的次数
        if len(p) > len(s): # 窗口大小大于字符串长度 则无匹配
            return []
        # 初始化第一个窗口
        for i in range(count):
            intermedia[s[i]] += 1
        if intermedia == p_count:
            index.append(0)

        for right,ch in enumerate(s[count:],count): # 滑动窗口都用枚举 第一个窗口是1 ~ count-1
            left = right - count # 左边界
            intermedia[s[left]] -= 1 # 左边界字符出窗口
            intermedia[ch] += 1 # 右边界字符进窗口

            if intermedia == p_count: # 窗口内字符出现次数与 p 相同 则为异位词
                index.append(left+1) # 记录首字母索引 left进一个的位置是匹配索引



        return index


class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans




if __name__ == '__main__':
    s ="aaaaaaaaaa"
    p = "aaaaaaaaaaaaa"
    print(Solution().findAnagrams(s,p)) #[0, 6]
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution2().findAnagrams(s, p)) #[0, 6]