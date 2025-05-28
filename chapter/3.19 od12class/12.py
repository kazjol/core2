from collections import deque


class ParkingSystem:

    def __init__(self,big, medium, small):# python里形参不用指明数据类型像是int small

        self.park=[0,big,medium,small]# 初始化列表空车位数量
    def add_car(self, carType):# car type有123分别是大车，中车，小车
       if self.park[carType] == 0:# 没有空车位
        return False
       self.park[carType]-=1# 减少车位数量 自动else而且层级非常严格
       return True

# 获取用户输入的大中小车位数量
input_str = input("请输入大中小车位的数量，用空格分隔：")# 如果不加空格将会识别为一个数字这个是固定的
big, medium, small = map(int, input_str.split())# input（）.split(",")这里用，分隔形成的列表用，分隔 ***map的映射希望分隔的结果是纯int类型不能带标点

# 创建ParkingSystem对象
parking_system = ParkingSystem(big, medium, small)

car_type_input = int(input("请输入要添加的车辆类型（1: 大车, 2: 中车, 3: 小车）："))
car_names = {1: "大车", 2: "中车", 3: "小车"}#字典
if parking_system.add_car(car_type_input):
    print(f"成功添加了{car_names[car_type_input]}类型的车辆")# 把int强制转换成字典类型
else:
    print(f"没有{car_names[car_type_input]}类型的空车位")


# stack
# s="()[]{}"就是匹配的 而"([)]"则是不匹配的 （{[]})也是匹配的
class Solution:
    def isValid(self, s: str) -> bool:# ***->bool 定义返 回值类型为bool s：str 是类型注解的用法，表示输入参数为字符串类型
        # 当字符串长度为奇数的时候，属于无效情况，直接返回 False
        if len(s) % 2 == 1:
            # 无效情况，返回 False
            return False

        # 构建一个栈，用来存储括号
        stack = list()# 用列表来作栈使用

        # 遍历字符串数组中的所有元素
        for c in s:

            # 如果字符为左括号 ( ，那么就在栈中添加对左括号 （
            if c == '(':

                # 添加对左括号 （ 压栈
                stack.append('(')

            # 如果字符为左括号 [ ，那么就在栈中添加对左括号 [
            elif c == '[':

                # 添加对应的右括号 ]
                stack.append('[')

            # 如果字符为左括号 { ，那么就在栈中添加对左括号 {
            elif c == '{':

                # 添加对应的右括号 }
                stack.append('{')

                # 否则的话，说明此时 c 是 ）] } 这三种符号中的一种
                # if elif elif 然后才开始else

            '''
            先把碰到的左括号压栈后面紧接碰到右括号则匹配把栈里的左括号弹出
            '''
        else:

                # 如果栈已经为空，而现在遍历的字符 c 是 ）] } 这三种符号中的一种，这是输入的部分，要用栈里已有的来匹配
                # 找不到可以匹配的括号，返回 False
                # 比如这种情况  }{，直接从右括号开始，此时栈为空
                if not stack:# stack为空则农田stack为true
                    return False

                # 如果栈不为空，获取栈顶元素
                top = stack[-1]# -1索引是栈顶元素

                # 将栈顶元素和此时的元素 c 进行比较，如果相同，则将栈顶元素移除
                if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
                    # 移除栈顶元素
                    stack.pop()
                else:
                    # 如果不相同，说明不匹配，返回 False
                    return False

        # 遍历完整个字符数组，判断栈是否为空
        # 如果栈为空，说明字符数组中的所有括号都是闭合的
        # 如果栈不为空，说明有未闭合的括号
        return not stack# not stack是bool类型stack为空返回True，stack不为空返回False


# 题目：2023A-括号检查
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：栈
# 代码看不懂的地方，请直接在群上提问

s = input()
# 初始化用于判断异常的变量isError，初始化为False表示没有异常
isError = False
# 初始化答案变量ans和记录当前深度的变量cur_depth
ans, cur_depth = 0, 0
# 构建三种括号的两两配对关系
pairs = [('(', ')'), ('{', '}'), ('[', ']')]

# 若字符串长度为奇数，必定无法配对，isError设置为True
if len(s) % 2 == 1:
    isError = True
else:
    # 使用列表list初始化一个空栈
    stack = list()
    # 一次遍历字符串s中的每一个字符ch
    for ch in s:
        # 若ch为某种左括号
        if ch == '(' or ch == '{' or ch == '[':
            # 则将ch加入栈顶，同时括号深度+1，更新最大括号深度
            stack.append(ch)
            cur_depth += 1
            ans = max(ans, cur_depth)# 比较ans和cur_depth的大小，更新ans
        # 若ch为某种右括号
        else:
            # 若此时栈为空
            if len(stack) == 0:
                # 该右括号无法与左括号配对，出现异常，isError设置为True，同时退出循环
                isError = True
                break
            # 若栈不为空，则弹出栈顶字符，同时括号深度-1
            ch_stack_top = stack.pop()
            cur_depth -= 1
            # 若栈顶左括号字符ch_stack_top和当前右括号字符ch不配对，
            # 出现异常，isError设置为True，同时退出循环
            if (ch_stack_top, ch) not in pairs:# 不匹配的括号 因为pairs列表里的元素只有三对匹配的括号
                isError = True
                break
    # 经过一次遍历后，若仍存在元素，说明存在括号未配对，出现异常，isError设置为True
    if len(stack) > 0:
        isError = True

# 如果isError标志为True，说明前面某一步出现异常，输出0，否则输出最大深度ans
print('no complete' if isError else ans)



# queue

class MovingAverage:
    def __init__(self, size: int):# 构造函数名固定为__init__
        # 1、记录当前窗口的大小
        self.size = size
        # 2、记录当前窗口里面所有元素的和
        self.sum = 0
        # 3、由于数字进入滑动窗口和移出滑动窗口的规则符合先进先出，因此可以使用队列存储滑动窗口中的数字
        self.q = deque()# dequeue是双端队列，可以从两端添加和删除元素，类似于队列

    def next(self, val: int) -> float:
        # 4、在添加 val 之前，先判断滑动窗口的长度是否已经达到了最大容量 size
        if len(self.q) == self.size:
            # 5、如果达到了，此时先将窗口最左边的元素移除去，即 popleft
            # 那么当前 滑动窗口 里面的元素和就发生了变化，也需要减去
            self.sum -= self.q.popleft()# poplesft（）是双端队列的封装（内置）函数
        # 6、再把 val 累加到 sum.txt 上面去
        self.sum += val
        # 7、同时 val 也加入到了队列里面
        self.q.append(val)
        # 8、最后，计算平均值就行
        return self.sum / len(self.q)
