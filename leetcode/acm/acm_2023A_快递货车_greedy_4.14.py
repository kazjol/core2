# 快递货车
#一辆具有最大载重量的运送快递的货车正在运送若干重量不一的快递中，试计算出该货车最多能运载的快递数目。快递数量最多为1000个，货车的最大载重最为50000。
# 注：不考虑快递的体积。
# 输入
# 第一行输入每个快递的重量，用英文逗号隔开，如 5,10,2,11
# 第二行输入货车的最大载重量，如 20
# 输出
# 输出最多能装多少个快递，如 3

# 匹配问题
# 先sort排序然后直接遍历往货车塞就行了 塞到最接近max_weight的位置 因为如果连小的都放不进后面一定没意义
from typing import List
class Solution:
    def maxnum_packages(self, weights: List[int], max_weight: int) -> int:
        # 先将重量从小到大排序
        weights.sort()
        # 定义一个变量记录当前载重
        total_weight = 0
        for weight in weights: # 遍历
            if total_weight + weight <= max_weight: # 如果当前载重加上当前快递的重量小于等于最大载重
                total_weight += weight # 则加上当前快递的重量
            else:
                return weights.index(weight)# 否则返回当前快递的索引 因为是先weight往后走了一个再返回的索引所以不用+1

        return len(weights) # 全部能塞下
weights = list(map(int, input().split(',')))
max_weight = int(input())
print(Solution().maxnum_packages(weights, max_weight))