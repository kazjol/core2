from collections import Counter
from my_python_lib import memory_monitor

class Solution:
    @memory_monitor
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


class TestSolution:
    @staticmethod
    def test_case1():
        """测试基本用例"""
        s = "abc"
        result = Solution().countGoodSubstrings(s)
        print(f"测试用例1: 输入={s}, 期望=1, 实际={result}")
        return result == 1

    @staticmethod
    def test_case2():
        """测试多个符合条件的子串"""
        s = "aababcabc"
        result = Solution().countGoodSubstrings(s)
        print(f"测试用例2: 输入={s}, 期望=4, 实际={result}")
        return result == 4

    @staticmethod
    def test_case3():
        """测试空字符串"""
        s = ""
        result = Solution().countGoodSubstrings(s)
        print(f"测试用例3: 输入={s}, 期望=0, 实际={result}")
        return result == 0

    @staticmethod
    def test_case4():
        """测试长字符串"""
        s = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
        result = Solution().countGoodSubstrings(s)
        print(f"测试用例4: 输入={s}, 期望=?, 实际={result}")
        return True  # 因为期望值未知，只打印结果

    @staticmethod
    def run_all_tests():
        """运行所有测试"""
        print("开始运行所有测试...")
        TestSolution.test_case1()
        TestSolution.test_case2()
        TestSolution.test_case3()
        TestSolution.test_case4()
        print("所有测试完成")


if __name__ == "__main__":
    import sys

    # 如果没有命令行参数，运行所有测试
    if len(sys.argv) == 1:
        TestSolution.run_all_tests()
    else:
        # 根据命令行参数运行特定测试
        test_case = sys.argv[1]
        if test_case == "test_case1":
            TestSolution.test_case1()
        elif test_case == "test_case2":
            TestSolution.test_case2()
        elif test_case == "test_case3":
            TestSolution.test_case3()
        elif test_case == "test_case4":
            TestSolution.test_case4()
        else:
            print(f"未知的测试用例: {test_case}")