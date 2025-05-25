# 1456. 定长子串中元音的最大数目
# 字符串 滑动窗口 定长
# 给你一个字符串 s 和整数 k 。请返回 s 中长度为 k 的单个子串中可能包含的最大元音字母的数目。
# 元音字母包括 'a', 'e', 'i', 'o', 'u' 。
# 注意：子串的长度为 k 时，如果字符串 s 中存在长度大于 k 的子串，那么答案只统计长度为 k 的子串。
# 定长窗口为k

# 示例 1：
# 输入：s = "abciiidef", k = 3
# 输出：3
# 解释：子串 "iii" 中包含 3 个元音字母。




# 定长滑动窗口思路：
# 优化 ： 固定滑动窗口 只用考虑进和出的元素是不是元音 出不是元音 进元音则加1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0 # 统计元音字母数量
        maxn = 0 # 记录最大元音字母数量
        vowels = ['a', 'e', 'i', 'o', 'u'] # 定义元音列表 用来匹配
        # 直接用字符串也能匹配
        left, right = 0, k-1 # 左右指针

        count = sum(1 for i in range(k) if s[i] in vowels) # 统计窗口内元音字母数量
        while right < len(s):
            if s[right] in vowels and s[left] not in vowels:

                count += 1
                maxn = max(maxn, count)


            elif s[right] not in vowels and s[left] in vowels:
                count -= 1
                count = max(count, maxn)

            if s[left:right+1] == 'aeiou':
                maxn = k
                return maxn

            right += 1
            left += 1
        return maxn














# 怎么优化
class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):
            # 1. 进入窗口
            if c in "aeiou": # 进窗口的元素是元音
                vowel += 1
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            ans = max(ans, vowel)
            # 3. 离开窗口
            if s[i - k + 1] in "aeiou": # 出窗口的元素是元音 因为一开始就判过进的是不是元音了 所以这里如果出的是元音直接减就好了
                vowel -= 1
        return ans


# 题目：LC1456. 定长子串中元音的最大数目
# 难度：中等
# 作者：许老师-闭着眼睛学数理化
# 算法：固定滑窗
# 代码看不懂的地方，请直接在群上提问


class Solution3:
    def maxVowels(self, s: str, k: int) -> int:
        # 初始化包含所有5种元音字母的哈希集合
        vowels = {'a', 'e', 'i', 'o', 'u'}

        win_num = 0
        # 初始化第一个窗口的情况
        for ch in s[:k]:
            if ch in vowels:
                win_num += 1

        ans = win_num

        for right, ch in enumerate(s[k:], k): # 遍历从k开始的字符串 对s的索引从k开始
            # A1
            if ch in vowels:
                win_num += 1
            # A2
            left_ch = s[right - k]
            if left_ch in vowels:
                win_num -= 1
            # A3
            ans = max(ans, win_num)

        return ans

s = "abciiidef"
k = 3
print('超时',Solution().maxVowels(s, k))
print('\n\n优化',Solution2().maxVowels(s,k))
print('\n\n优化 od',Solution3().maxVowels(s,k))




def test():
    print('\n\n','test')
    # 字符串可索引不可修改
    s = "leetcode"

    print(s.index('e')) # index只会输出第一个匹配项
    print(s.count('e')) # count会输出所有匹配项的个数

    s=list(s)
    s.append('f')
    print(s)


    k=3
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s=['a', 'b', 'c', 'i', 'd', 'e', 'f']
    count = sum(1 for i in range(k) if s[i] in vowels) # 统计窗口内元音字母数量
    print(count,'\n\n')

    # 遍历字符串 索引从2开始
    for i,num in enumerate(s[2:],2):
        print(i,num)
print(test())