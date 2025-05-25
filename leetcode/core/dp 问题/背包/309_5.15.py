# 最佳买卖股票时机含冷冻期

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。

# 设计一个算法计算出**最大利润。在满足以下约束条件下，你可以尽可能地完成**更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 
from math import inf
from typing import List
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache # 使用@cache装饰器时，只有作为函数参数的对象需要是可哈希的（hashable）
        # 在新的实现中，你的dfs函数没有直接将prices数组作为参数传递。dfs函数只接收两个参数：i（当前处理的天数索引）和hold（是否持有股票的布尔值）。
        # 当你的递归函数通过索引i访问prices[i]时，你是在访问函数外部定义的变量，而不是将整个数组作为参数传递。
        def dfs(i: int, hold: bool) -> int:
            '''
            最重要的边界条件 进入到第一天的情况 
            1、持有 不可能那么这条分支全部无效 返回-inf
            2、不持有 正常返回收益为0

            股票最重要的两个已知条件
            1、第一天不持有股票 收益为0
            2、最后一天不持有股票 收益为最大
            '''
            if i < 0:
                return -inf if hold else 0
            # 两个式子的轻微区别其实就是在 买入需要冷冻期而卖出不需要 
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i]) # 今天持有股票 可能是昨天*持有*股票今天不操作 或者两天前*不持有*股票过了冷冻期今天买入  
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i]) # 今天不持有股票 可能是昨天*不持有*股票今天不操作 或者昨天*持有*股票今天卖出 
        return dfs(n - 1, False) # *股票的两个入口条件*第一天不持有股票和最后一天不持有股票
# 动态规划 优化空间
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 2)]
         # 存储每天持有股票的状态 一项保存有持有股票和未持有股票的最大利润 一共有天数的项数 
         # 相当于保存每天两种状态的最大利润 最后返回最后一天不持有股票的状态

         # 初始化第一天持有股票的状态为-inf 因为第一天不可能持有股票 遍历是从（1，n+1）更好理解
        f[1][1] = -inf
        for i, p in enumerate(prices):
            f[i + 2][0] = max(f[i + 1][0], f[i + 1][1] + p) # 今天不持有股票 可能是昨天*不持有*股票今天不操作 或者昨天*持有*股票今天卖出
            f[i + 2][1] = max(f[i + 1][1], f[i][0] - p) # 今天持有股票 可能是昨天*持有*股票今天不操作 或者两天前*不持有*股票过了冷冻期今天买入 *买入股票具有一天的冷冻期* 所以要两天前不持有股票今天才能买入
            '''
            其实也就是对于 一天前不持有股票 有两种情况 
            1、之前卖出的  对于这种今天不能操作不做判断
            2、一天前卖出的 对于这种其实结果继承了两天前不持有股票的状态(不操作)也就是f[i+1][0]=f[i][0] 所以直接用f[i][0]来做判断就好

            '''
            
            # f[i][0]表示"第i天不持有股票"的最大利润，但这个状态已经包含了所有可能的历史情况，包括：
            # 从未持有过股票
            # 之前持有过但已经卖出
            # 刚刚卖出

            # 动态规划会自动选择最优路径。如果"一天前不持有股票"是因为两天前就卖出了，那么f[i+1][0]已经包含了这种情况下的最大利润。
            # 但是，我们不能直接使用f[i+1][0]（一天前不持有股票的状态）来更新f[i+2][1]（今天持有股票的状态），因为：
            # 1、如果第i+1天不持有股票是因为第i+1天卖出了，那么第i+2天是冷冻期，不能买入
            # 2、如果第i+1天不持有股票是因为更早之前就卖出了，那么第i+2天可以买入
            # 动态规划无法区分这两种情况，所以我们需要使用f[i][0]（两天前不持有股票的状态）来确保我们在考虑买入股票时，已经过了冷冻期。
            # 这就是为什么状态转移方程中使用f[i][0]而不是f[i+1][0]。它确保了我们在考虑买入股票时，已经过了冷冻期，而不需要显式地判断"一天前不持有"是因为什么原因。
            # 简单来说，动态规划会自动选择最优路径，我们只需要确保状态转移方程正确地表示了问题的约束条件。
        
        return f[-1][0]
    
# 它通过状态机的思想，将问题转化为三个状态的转移，避免了使用二维数组或递归调用，同时保持了代码的可读性和正确性。
# 这个解法也很好地处理了冷冻期的约束：当股票被卖出后，必须经过一个冷却期才能再次买入，这个约束通过状态转移 cd = max(cd, sold) 来保证。
class Solution3:
    
    def maxProfit(self, prices: List[int]) -> int:
        # 因为最后一天要么是刚卖出，要么是在冷却期。
        held = sold = -float("inf") # 强制转字符串为float类型   hold：持有股票的最大利润 sold：卖出股票的最大利润
        cd = 0 # 冷却期的最大利润
        # 设立三种状态 持有股票 卖出股票 冷却期 状态机的思想 状态间转移
            
        # 让我们详细分析每个状态转移：
        # 持有状态 (held)：
        # 可以保持持有状态不变 (held)
        # 或者从冷却期买入 (cd - p)
        # 取两者中的最大值
        # 冷却期状态 (cd)：
        # 可以保持冷却期状态不变 (cd)
        # 或者从卖出状态进入冷却期 (sold)
        # 取两者中的最大值
        # 卖出状态 (sold)：
        # 只能从持有状态卖出 (held + p) 
        # 
        #          
        
        for p in prices:  # 遍历每一天的股票价格
            # 1. 计算持有股票状态的最大利润
            tmp = max(held, cd - p)  
            # held: 保持持有状态不变
            # cd - p: 从冷却期买入股票（需要减去当前价格）
            # 取两者中的最大值作为新的持有状态

            # 2. 更新冷却期状态
            cd = max(cd, sold)  
            # cd: 保持冷却期状态不变
            # sold: 从卖出状态进入冷却期
            # 取两者中的最大值作为新的冷却期状态

            # 3. 计算卖出股票状态的最大利润
            sold = held + p  
            # 只能从持有状态卖出
            # held + p: 持有状态卖出股票（加上当前价格）
            # 注意：不能从冷却期卖出，因为冷却期没有股票

            # 4. 更新持有状态
            held = tmp  
            # 使用之前计算好的tmp更新持有状态
        
        return max(sold, cd)
class Solution4:
    
    def maxProfit(self, prices: List[int]) -> int:
        rest = 0                # 未持有股票且不在冷冻期（可以买入） 冷冻期结束 
        sold = 0                # 未持有股票刚卖出股票（冷冻期）
        hold = -float("inf")    # 持有股票
        for price in prices:
            preSold = sold
            preHold = hold
            preRest = rest

            # 三个状态都只能由另一个状态转化或是继承自身 但是对于sold不能继承 如果sold继承则变成rest状态了
            '''
                画出状态机 然后直接列式子就行了 
                注意状态的更新一定要用之前的状态tmp暂存 不能用更新后的状态（因为是多状态转换）
            '''

            hold = max(preHold, preRest - price)   # 继续持有 or 休息后买入
            sold =  preHold + price                # 在一天的循环中，sold 只能由昨天持有股票并且今天卖出得到 sold的定义是刚刚卖出 如果继承则不是sold状态而是rest状态了
            rest = max(preRest, preSold)           # 继续休息 or 冷冻期结束
        return max(rest, sold)
prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))
print(Solution2().maxProfit(prices))
print(Solution3().maxProfit(prices))
print(Solution4().maxProfit(prices))
            
'''
状态机思想：
设置全部可能状态 分析状态间的转化方式 列出所有可能的状态更新方式 取最优

示例：自动售货机
[等待投币]  [已投币]  [出货中] 三种状态
            
            状态转移 都是单向的 
                   投币
[等待投币] -----> [已投币] -----> [出货中]
     ^                |              |
     |                | 选择商品      | 出货完成
     |                v              v
     +----------------[等待投币]------+

初始化状态
waiting = True    # 等待投币状态
paid = False      # 已投币状态
dispensing = False # 出货中状态

1、正常购买
1. 初始状态：
[等待投币] --投币--> [已投币] --选择商品--> [出货中] --出货完成--> [等待投币]

2. 状态转换：
- 投币：waiting -> paid
- 选择商品：paid -> dispensing
- 出货完成：dispensing -> waiting

2、取消购买
1. 状态转换：
[等待投币] --投币--> [已投币] --取消--> [等待投币]

2. 状态转换：
- 投币：waiting -> paid
- 取消：paid -> waiting

3、缺货
1. 状态转换：
[等待投币] --投币--> [已投币] --选择缺货商品--> [等待投币]

2. 状态转换：
- 投币：waiting -> paid
- 选择缺货商品：paid -> waiting（退回硬币）

class VendingMachine:
    def __init__(self): # 对象初始化函数初始化状态
        self.waiting = True
        self.paid = False
        self.dispensing = False
        self.balance = 0

    def insert_coin(self, amount):
        if self.waiting:
            self.waiting = False
            self.paid = True
            self.balance += amount
            return "已投币"
        return "机器正在工作中"

    def select_product(self, product):
        if self.paid:
            if self.check_stock(product):
                self.paid = False
                self.dispensing = True
                return "正在出货"
            else:
                self.paid = False
                self.waiting = True
                return "商品缺货，退回硬币"
        return "请先投币"

    def complete_dispensing(self):
        if self.dispensing:
            self.dispensing = False
            self.waiting = True
            return "出货完成"
        return "机器未在出货中"

    def cancel(self):
        if self.paid:
            self.paid = False
            self.waiting = True
            return "已取消，退回硬币"
        return "无法取消"

状态定义：
    等待投币：初始状态，可以接受投币
    已投币：可以选择商品或取消
    出货中：正在处理出货
状态转换规则：
    只能从等待投币状态投币
    只能从已投币状态选择商品
    只能从出货中状态完成出货
    可以从已投币状态取消
状态转换的约束：
    必须按顺序进行状态转换
    每个状态只能执行特定的操作
    状态转换需要考虑各种异常情况
状态转换的触发条件：
    投币：需要等待投币状态
    选择商品：需要已投币状态
    出货完成：需要出货中状态
    取消：需要已投币状态
'''


'''
状态机 多向状态转移 
    红绿灯：
    [红灯] <----> [绿灯] <----> [黄灯]
    状态转移规则：
    红灯 -> 绿灯 -> 黄灯 -> 红灯（正常循环）
    紧急情况下可以：红灯 -> 黄灯（闪烁）
    故障时可以：任意状态 -> 黄灯（闪烁）

    游戏角色状态：
      [站立] <----> [行走] <----> [奔跑]
        ^            ^  ^          ^
        |            |  |          |
        |            |  |          |
        +------------+--+----------+
            [跳跃]          [攻击]
    状态转移规则：
    站立 -> 行走/奔跑/跳跃/攻击
    行走 -> 站立/奔跑/跳跃/攻击
    奔跑 -> 站立/行走/跳跃/攻击
    跳跃 -> 站立/行走/奔跑
    攻击 -> 站立/行走/奔跑

游戏角色状态机:
class CharacterState:
    def __init__(self):
        self.state = "standing" # 初始化为站立状态
        self.stamina = 100 # 初始化体力值

    def change_state(self, new_state):
        # 定义状态转移规则
        # 字典 键值对 状态转移规则 匹配上键值之后可以转移到对应的值
        transitions = {
            "standing": ["walking", "running", "jumping", "attacking"],
            "walking": ["standing", "running", "jumping", "attacking"],
            "running": ["standing", "walking", "jumping", "attacking"],
            "jumping": ["standing", "walking", "running"],
            "attacking": ["standing", "walking", "running"]
        }

        # 检查状态转移是否合法
        if new_state in transitions[self.state]: # 用当前状态在transitions字典中匹配 如果匹配到则可以转移
            # 检查特殊条件
            if new_state == "running" and self.stamina < 20:
                return "体力不足，无法奔跑"
            
            # 执行状态转移
            self.state = new_state
            return f"状态已更改为: {new_state}" # 在字符串里接变量
        
        return "非法的状态转移"

    def update(self):
        # 状态更新逻辑
        if self.state == "running":
            self.stamina -= 1
        elif self.state == "standing":
            self.stamina = min(100, self.stamina + 1) # 体力值在100和当前体力值+1之间取最小值 回血

状态转移的条件和约束：
条件转移：
def can_transition(self, from_state, to_state):
    # 检查基本条件
    if to_state not in self.transitions[from_state]:
        return False
    
    # 检查特殊条件
    if to_state == "running" and self.stamina < 20:
        return False
    
    return True

状态转移的副作用：
def transition_effects(self, from_state, to_state):
    if from_state == "running" and to_state == "standing":
        self.stamina += 5 # 回血
    elif to_state == "running": # 奔跑状态消耗体力
        self.stamina -= 10



'''



'''
1.状态机的核心概念
    基本组成：
        状态（States）：系统可能处于的有限个状态
        转换（Transitions）：状态之间的转换规则
        事件（Events）：触发状态转换的输入
        动作（Actions）：状态转换时执行的操作
    状态转移方式：
        单向转移：A -> B -> C
        双向转移：A <-> B
        多向转移：A -> B/C/D
        循环转移：A -> B -> C -> A

2. 判断是否使用状态机的特征
    适合使用状态机的情况：
        系统有明确的状态划分
        状态数量有限且可枚举
        状态转换规则清晰
        不同状态下行为不同
        需要跟踪系统状态
    不适合使用状态机的情况：
        状态数量过多
        状态转换规则复杂
        状态之间关系不明确
        系统行为不依赖状态

'''