
class ListNode: # 定义结点类型
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Linkedlist: # 定义链表类型
    def __init__(self, head=None):
            self.head = head


class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        # 初始化快慢指针
        slow = fast = head # 核心代码模式head指针是给定的
        while fast and fast.next :# python里不用&&用and
            slow = slow.next # python和c++里访问对象的变量和函数只用.
            fast = fast.next.next
        return slow # python里因为没有{}所以要注意缩进
