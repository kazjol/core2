# 有效的完全平方数
# 数学 二分
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
#
# 不能使用任何内置的库函数，如  sqrt（开根函数） 。

class Solution:
    def isPerfectSquare(self, num: int) -> bool: # 这个命名很有意思 因为能开根的函数意味着是个完美的正方形
        if num < 2:
            return True
        # 二分从 2 到 num // 2 找一个整数 x 用x^2和num比较 这里用二分法更新x的值
        left, right = 2, num // 2 # 闭区间
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > num:
                right = mid - 1
            elif mid*mid == num:
                return True
            else :
                left = mid + 1

        return  False
num = 16
print(Solution().isPerfectSquare(num)) # True

#在Python中，mid^2 不是表示平方的运算符。^ 在Python中是按位异或（bitwise XOR）运算符，而不是幂运算。
# 例如：
# 2^2 的结果是 0，因为这是二进制 10 和 10 的按位异或运算
# 3^2 的结果是 1，因为这是二进制 11 和 10 的按位异或运算

# 可以搜一下异或的实际应用很有意思
print('\n\n',2**3) # **幂运算符 2的3次方 
