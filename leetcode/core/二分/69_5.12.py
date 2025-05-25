# x的平方根
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

            if mid*mid < x < (mid + 1)*(mid + 1):
                return mid


x = 8
print(Solution().mySqrt(x)) # Output: 2
print(int(4.7)) # 强制类型转换向下取整

# pow() 函数是 Python 内置的幂运算函数，它有两种使用方式：
# 基本用法：pow(x, y)
# 计算 x 的 y 次方
# 例如：pow(2, 3) 返回 8，表示 2 的 3 次方
# 带模运算的用法：pow(x, y, z)
# 计算 (x 的 y 次方) 对 z 取模
# 例如：pow(2, 3, 5) 返回 3，表示 (2 的 3 次方) 对 5 取余

# sqrt（x）对x开根号