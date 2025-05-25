# 用两个栈实现队列先入先出 一般队列支持的操作（push，pop，peek，empty）
# 一个用来进 stack_in 一个实现出 stack_out 两个栈互相倒实现先入先出
class MyQueue:

    def __init__(self):
        # self就是该类的对象 python里这样写可以说明调用
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if  not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() # pop函数的返回值是int


    def peek(self) -> int: # 返回栈顶元素而不是删除栈顶元素所以不能只用pop（） pop（）一出来就会删除栈顶
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        x=self.stack_out.pop()
        self.stack_out.append(x)
        return x

    def empty(self) -> bool: # 判断stack_in 和 stack_out是否都为空
        if not self.stack_in and not self.stack_in:
            return True
        return False
        # 直接 return not self.stack_in and not self.stack_in 本身这个判断结果就是bool型


# 定义了一个MyQueue类 定义一个该类对象可以调用内部函数直接用
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()