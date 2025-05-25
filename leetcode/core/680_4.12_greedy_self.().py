# 验证回文字符串
# 贪心 双指针 字符串

# 给你一个字符串 s，最多 可以从中删除一个字符。
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false

# 实例：
# 输入：s = "abca"
# 输出：true 可以删除 'c' 得到 "ab"，这是回文字符串
# abccbca
# 遇到不相等的字符，可以尝试删除一个字符 再对剩下部分验证回文串 删除一个字符指针要移动

# reverse（）函数是列表的内置函数，可以将字符串转换为列表，然后反转列表，再转换回字符串，判断是否相等。

print('mine')
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        count = 0
        f = 0 # 记录删除一边元素的次数
        # 特殊情况
        if len(s) == 3:

            if s != s[::-1]: # 分片做逆序

                return False
        # 一个或两个字符的字符串 一定是回文串
        if len(s) < 3:
            return True


        while left < right:
            if s[left]!= s[right]:
                # 假装删除一个字符 指针移动
                # 有两种情况可以试着删除两次 一次的结果满足就满足


                count += 1  # 记录删除了一个字符

                if count > 1: # 已经删除了两个字符 直接返回 false
                    f += 1

                    break
                left += 1  # 删除左边的字符


            # 验证删除的字符后的部分是否为回文串

            else:
                left += 1
                right -= 1

        left = 0
        right = len(s) - 1
        count = 0

        while left < right:
            if s[left] != s[right]:
                # 假装删除一个字符 指针移动
                # 有两种情况可以试着删除两次 一次的结果满足就满足

                count += 1  # 记录删除了一个字符
                if count > 1:  # 已经删除了两个字符 直接返回 false
                    f += 1
                    break
                right -= 1  # 删除右边的字符
                # 验证删除的字符后的部分是否为回文串
            # 不用说明是else 因为是接着if的且无其他 自动执行else
            else:
                left += 1
                right -= 1

        if f == 2:
            return False
        return True
s = "yd"
print(Solution().validPalindrome(s)) # True

print('\n\n贪心')
# 贪心算法

class Solution2:

    # 类内部的函数的自己调用自己
    # 在删除一个字符后，直接调用内部函数判断是否为回文串
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 # 连续初始化
        while left < right:
            if s[left] != s[right]:
                # 删除 s[left] 或者 s[right]
                return self.isPalindrome(s[left + 1: right + 1]) or self.isPalindrome(s[left: right]) # 因为切片不包含切片结尾元素
                # or 一个满足有就返回True 否则返回False
            left += 1
            right -= 1
        return True  # s 本身就是回文串

# s[left + 1: right + 1] 代表从s的left+1位置开始截取，到right+1位置结束的子字符串。

s = "aebcbbbea"
print(s[1:4]) # "ebc"切片不包含切片结束元素
print(Solution2().validPalindrome(s)) # True

# input()函数返回输入的字符串，strip()函数用于去除字符串头尾指定的字符（默认为空格或换行符）
# 字符串的切片操作可以用[头下标:尾下标]来表示，其中下标从0开始，可以省略头下标或尾下标，省略时表示取到字符串末尾或开头。
# 字符串的反转操作可以用[:: -1]来表示，即步长为-1，即从尾部开始取元素。
# 字符串的比较操作可以用==来表示，即比较两个字符串是否相等。
# 字符串的拼接操作可以用+来表示，即将两个字符串连接起来。
# 字符串的索引操作可以用[]来表示，即通过下标访问字符串中的元素。






