# 回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。



# 取mid值 从头到尾和从尾到头比较 相同则是回文数
# 不用取mid值 直接判low heigh指针大小就行
class Solution:
     def isPalindrome(self, x: int) -> bool:
         ch = str(x)
         len(ch)
         low = 0
         heigh = len(ch) - 1
         while low < heigh:
             if ch[low]!= ch[heigh]:
                 return False
             low += 1
             heigh -= 1

         return True
x = 1211
print(Solution().isPalindrome(x))



# od解法
class Solution2:
    def isPalindrome(self, x: int) -> bool:

        # 转换为字符串数组的形式
        xArray = list(str(x))

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



# 相向双指针从两边往中间移 也就是low和heigh 首尾指针
# 降复杂度从O(n^2)降到O(n)

# 双指针 同向->快慢指针  相向->low和heigh指针 背向考察少

