# 长度为三且字符各不相同的字符串
# 哈希表 计数 滑动窗口 定长

# 计算所有长度为3且字符各不相同的子串的数量
# 是的，from collections import Counter 是从 Python 的 collections 模块一个 模块名.py文件 里面定义了很多类
# 中导入 Counter 类 Counter 类是定义的一个类 所以Counter可以生成一个Counter对象


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        # 特殊情况
        if len(s) < 3:
            return 0
        # 初始化哈希表 记录子串中字符出现的次数
        char_count = Counter(list(s[0:3]))
        if 2 not in char_count.values() and 3 not in char_count.values(): # 长度为3且字符各不相同的子串至少有两个不同的字符
            count += 1
        print(char_count)


        # 遍历字符串

        for right,num in enumerate(s[3:],3): # 窗口大小为3 从3开始切片 从3开始遍历 初始化的窗口是0-2
            left = right - 3 # 左边界
            char_count[s[right]] += 1
            char_count[s[left]] -= 1

            # if (2 or 3) not in char_count.values():  # 长度为3且字符各不相同的子串至少有两个不同的字符 忘记了3 0 0 的情况
            # ****语法错误 这个条件判断是错误的，因为 (2 or 3) 在 Python 中会被解释为 2（因为 2 是第一个非零值），所以这个条件实际上等同于 if 2 not in char_count.values()。
            # 显而易见先算（）里的2 or 3 会产生bool 的true
            if 2 not in char_count.values() and 3 not in char_count.values():
                count += 1



        return count

s ="ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
print(Solution().countGoodSubstrings(s))



# 在模块里定义测试函数 只有直接运动模块时 特殊语句if __name__ == "__main__": 才会成立 定义的该函数才会执行
# 当调入该模块时 import 模块名 则不会执行该函数
# 在 if __name__ == "__main__": 块中定义函数是 Python 中一种常见的做法，让我解释一下：
# 定义测试函数
# 还可以定义测试 类 当单独运行该模块时 该类才会能被执行
# if __name__ == "__main__":
#     class TestSolution: # 测试类
#         def test_case1(self):
#             s = "abc"
#             assert Solution().countGoodSubstrings(s) == 1
#
#         def test_case2(self):
#             s = "aababcabc"
#             assert Solution().countGoodSubstrings(s) == 4
#
#     # 运行测试
#     test = TestSolution()
#     test.test_case1()
#     test.test_case2()

# 这些函数只在直接运行这个文件时才会被定义和执行，当文件被导入时不会执行。这样做的好处是：
# 可以组织测试代码
# 避免污染全局命名空间
# 使测试代码更有条理
# 方便添加新的测试用例



'''
Python 程序入口：
当 Python 运行一个程序时，会有一个主模块（main module）
主模块的 __name__ 属性会被设置为 "__main__"
其他被导入的模块的 __name__ 属性会被设置为它们的模块名


当模块被导入时 该模块不会成为执行入口处不是main（） 该模块的 __name__ 属性会被设置为模块名
'''


class Solution2: # 更简化但是不够快
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        # 使用集合来检查是否有重复字符，比检查Counter.values()更高效
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3: # 因为集合不能有重复元素 所以set的长度为3就直接实现了
                count += 1
        return count


if __name__ == "__main__": # 可以单独执行该模块
    s = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
    print(Solution().countGoodSubstrings(s))

from collections import Counter


class Solution3: # 更快
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        # 直接比较三个字符是否相同，比使用set更快
        for i in range(len(s) - 2):
            a, b, c = s[i], s[i + 1], s[i + 2]
            if a != b and b != c and a != c:
                count += 1
        return count


if __name__ == "__main__":
    s = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
    print(Solution().countGoodSubstrings(s))

# 减少内存分配：
# 移除了 set 的创建，避免每次循环都创建新的集合对象
# 直接使用字符比较，减少内存操作
# 减少函数调用：
# 移除了 len() 和 set() 的调用
# 使用直接的字符比较，减少函数调用开销
# 优化比较逻辑：
# 使用 a != b and b != c and a != c 代替 len(set(...)) == 3
# 这种比较方式更直接，不需要创建临时对象
# 代码简化：
# 移除了不必要的导入
# 代码更简洁，逻辑更清晰
# 这个优化版本应该会运行得更快，因为：
# 减少了内存分配和释放
# 减少了函数调用
# 使用了更直接的比较方式
# 避免了创建临时对象




'''
@staticmethod 是 Python 中的一个装饰器，让我详细解释一下：
基本概念：
@staticmethod 用于定义静态方法
静态方法不需要访问实例或类
可以通过类名直接调用，不需要创建实例

class MyClass:
    # 普通方法
    def normal_method(self):
        print("这是一个普通方法")
    
    # 静态方法
    @staticmethod
    def static_method():
        print("这是一个静态方法")

# 普通方法需要实例
obj = MyClass() # 创建一个对象
obj.normal_method()

# 静态方法可以直接通过类调用 不用self方法()

# 直接 类名.静态方法名()

MyClass.static_method()

用 @staticmethod 的好处：
不用创建实例节省内存
代码更清晰
调用更方便
不需要创建实例
方法之间相互独立
在你的测试代码中，使用 @staticmethod 是一个很好的选择，因为：
测试方法不需要访问实例状态
可以直接通过类名调用
测试方法之间相互独立
代码更简洁清晰
'''