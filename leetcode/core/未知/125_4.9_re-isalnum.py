# 验证回文串
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
# 则可以认为该短语是一个 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回true ；否则，返回false 。

# 示例 1：
# 输入：s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。


print('Solution1:正则表达式')

# 1、要用到lower方法将所有大写字符转换为小写字符，用正则表达式去除所有非字母数字字符。 之后再用逆置判断是否相等
# 正则表达式：[^a-zA-Z0-9] 匹配除了字母和数字以外的字符。 调用re.sub()s = re.sub(r'[^a-z0-9]', '', s)的意思是从字符串s中移除所有非字母和非数字的字符。

import re # re模块用于正则表达式的处理 regex
class Solution1:
    def isPalindrome(self, s: str) -> bool:


        s2 = re.sub(r'[^a-z0-9]', '', s.lower())[::-1] == re.sub(r'[^a-z0-9]', '', s.lower())
        return s2
s = "A man, a plan9, a canal: Panama"
print(Solution1().isPalindrome(s)) # True
# re.sub()返回修改后的字符串
# pattern：是匹配模式 这里是[^a-z0-9]，即匹配字母和数字的字符。 repl即replace：是替换模式，把要去除的字符替换为''里的东西
# lower()：将字符串全部转换为小写。 [::-1]：逆置字符串

print(re.sub(r'[^a-z0-9]', '', s)) # 把字符串s中除小写字母和数字以外的字符替换为空，并打印
print(re.sub(r'[^a-z0-9]', '*', s)) # 因为字符串里面有空格空格 空格不属于小写字母和数字也要替换掉


print('\n\n\n')
print('Solution2:双指针   这个解有问题')
# 2、开始还是先转换为小写字母用lower()
# 用到ASCII码 字符1-9的ASCII码是49-57 字符a-z的ASCII码是97-122
# 用range（）生成序列来对比是否是小写字母和数字如果不是就跳过
# 然后还是用双指针
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a_cnt = -1
        a_l = list()
        b_cnt = -1
        b_l = list()
        # 字符串是可索引的
        i = 0
        j = len(s) - 1
        # 因为字符串出现奇数情况 所以条件带=
        while i < j-1: # 小于等于<= 而不是=<
            if ord(str(s[i])) not in range(49,58) and ord(str(s[i])) not in range(97,123):

                i += 1
            else:
                a_l.append(s[a_cnt+1])
                i += 1
                a_cnt += 1



            if ord(str(s[j])) not in range(49,58) and ord(str(s[j])) not in range(97,123):

                j -= 1
            else:
                b_l.append(s[b_cnt+1])
                j -= 1
                b_cnt += 1

        if a_l != b_l:
            return False




        return True



# if 里可以继续嵌套的
# 哪些动作是if哪些动作是else也要想好逻辑顺序

s = "A man, a plan, a canal: Panama"
# 输出a 字符串是可索引的
print(Solution2().isPalindrome(s)) # True


print('\n\n\n')
print('Solution3:双指针 od')


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        # is alpha number
        # isalnum() 方法检测字符串是否由大小写字母或数字组成 不接受参数直接用待求可索引数据调用
        # 转换为字符串数组的形式
        xArray = ",".join(ch.lower() for ch in s if ch.isalnum())
        xArray2 = "".join(ch.lower() for ch in s if ch.isalnum())

        print(xArray)
        print(xArray2)
        # .join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        #''里放分割来的元素间的分隔符最后生成的字符串元素之间会有， ‘’里默认为空
        # 遍历ch里的元素如果是字母或数字则保留并调用ch.lower（）将其转换为小写字母

        # 左边索引的位置在 0
        left = 0

        # 右边索引的位置在 len(xArray) - 1
        right = len(xArray) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while left <= right:
            # 判断这两个元素值是否相同
            if xArray[left] != xArray[right]:
                # 如果不同，直接返回 False
                return False

            # 否则，left 向右移动
            left += 1

            # right 向左移动
            right -= 1

        return True

s = "A man, a plan, a canal: Panama"
print(Solution3().isPalindrome(s)) # True
