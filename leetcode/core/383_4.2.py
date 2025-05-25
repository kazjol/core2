# 给两个字符串ransomNote和magazine，判断ransomNote是否能由magazine里的字符组成。
# 注意：每个字符只能使用一次。
# 也就是完全匹配或magazine的字符多出

# 这里还是用数组存字母用ASCII码
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for i in ransomNote:
            count[ord(i) - 97] = count[ord(i) - 97] + 1

        for i in magazine: # i是字母不是索引
            if count[ord(i) - 97] == 0:# 出现了多余字母
                continue # 跳过开始遍历下一个字母
            else: # else：后面不能直接接代码要换行
                count[ord(i) - 97] = count[ord(i) - 97] - 1
        for i in count: # i是count的索引值不是索引
            if i > 0:
                return False
        return True



ransomNote = "aa"
magazine = "aab" # 保证多余字母的情况
print(Solution().canConstruct(ransomNote, magazine))

