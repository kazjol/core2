# 找到一个数字的k美丽值
# 数学 数组 滑动窗口 定长

# 找出长度为k的 能被原字符串整除的子串的数目

# 字符串可索引不可更改
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        k_count = 0
        for right in range(len(num))[k-1:]:
            left = right - k +1
            son = int(num[left:right+1])
            if son != 0 and int(num) % son == 0:
                k_count += 1



        return k_count
num = 1000
k = 3
print(Solution().divisorSubstrings(num, k))
