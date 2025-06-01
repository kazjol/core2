# 考试的最大困扰度
# 字符串 二分查找 前缀和 滑动窗口 可变长度
from collections import defaultdict


# 操作规定次数使得 连续相等的字符串最长
# 操作次数小于等于k 除非出现全为T或F否则操作次数一定要用满

# 示例：
# 输入：answerkey = 'TTTFTFF' k=1
# 输出：5 修改第四个字符‘TTTTTFF’


class Solution:
    # def multiply(self, num1: str)->str:
    #     if num1 == 'T':
    #         return 'F'
    #     else:
    #         return 'T'

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ch_len = 0
        left,right = 0,0
        cur = answerKey[0]
        multi = int(k)
        diff = 0 # 记录第一个不同的字符的位置

        if len(answerKey) == 1:
            return 1

        while right in range(len(answerKey)):


            if answerKey[right] != cur and multi >0:

                if multi == int(k):
                     diff = right # 记录第一个不同的字符的位置

                # 遇到不同的就循环操作right+1直到k为0或right == n-1
                while multi > 0 and right < len(answerKey) and answerKey[right] != cur:
                    # modify_ch = self.multiply(answerKey[right]) # 取反操作  *类里面的函数间调用self.function()
                    multi -= 1 # 减少操作次数
                    right += 1



            # 如果没有操作步数了并且当前字符不同 就更新窗口大小
            elif answerKey[right] != cur and multi == 0:
                ch_len = max(ch_len, right-left)
                right = diff
                multi = int(k)
                cur = answerKey[right]
                left = right

            else:
                right += 1

        while left >= 1 and answerKey[left-1] == cur:
            left -= 1


        while multi > 0 and left >= 0 and answerKey[left-1] != cur:
            multi -= 1
            left -= 1




        # 边界情况
        ch_len = max(ch_len, right-left)


        return ch_len


class Solution2:
    # 哈希表 同时统计 T 和 F 的数量只要一个满足出现次数小于等于操作次数k 就说明可以操作保留该窗口长度 否则就更新窗口大小 直到再次满足条件

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # 用哈希表 保存‘T’和‘F’的次数
        # dict = {'T':0, 'F':0} # 初始化
        dict = defaultdict(int) # 防止key不存在报错
        max_len = 0 # 记录最大窗口长度
        left, right = 0, 0 # 窗口左右边界
        # 滑动窗口一般都是枚举

        for right, ch in enumerate(answerKey):
            dict[ch] += 1 # 统计当前字符出现次数

            while dict['T'] > k and dict['F'] > k: # 如果两个字符都满足操作次数k 就更新窗口大小
                # max_len = max(max_len, right-left+1) # 更新窗口大小
                dict[answerKey[left]] -= 1 # 左边界字符出现次数减1
                left += 1 # 左边界右移

            # 每次遍历都记录最大窗口 因为此时是满足条件的 不满足的时候会进入while然后调整直到满足条件
            max_len = max(max_len, right-left+1) # 处理最后一个窗口大小

        return max_len



answerKey = "TTTTTFTFFT"
k = 2
print(Solution().maxConsecutiveAnswers(answerKey, k))
print('\n\n哈希 滑动窗口',Solution2().maxConsecutiveAnswers(answerKey, k))