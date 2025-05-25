# 斐波那契数列
# 递归 记忆化搜索 dp



# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 计算 F(n)

class Solution:
    def fib(self, n: int) -> int:

        fn = 1
        fn1 = 0

        def FN(n: int, fn1:int, fn:int) -> int:
            if n == 0:
                return fn1 # 出递归 逐层执行return fn因为n恒为0 直接return
            t = fn
            fn =fn + fn1
            fn1 = t
            n=n-1
            return FN(n, fn1, fn)

        return FN(n, fn1, fn)
n = 4
print(Solution().fib(n))

from functools import cache
@cache # 装饰器 缓存函数的返回值 自动记忆化搜索了 把计算过的结果保存起来 避免重复计算
class Solution2:
    def fib(self, n: int) -> int:

        return  n if n < 2 else  self.fib(n-1) + self.fib(n-2) # 类内部函数间的调用要指明对象 这里就是self

n = 4
print(Solution2().fib(n))


class Solution3: # 迭代 动态规划
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q

        return r


n = 4
print(Solution3().fib(n))

'''
普通实例方法调用必须使用 self 否则会视为调用全局函数
静态方法（@staticmethod）和类方法（@classmethod）不需要 self
使用 self 可以明确表示这是一个实例方法的调用
'''