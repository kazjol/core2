class ListNode:
    def __init__(self, val=0, next=None): # 初始为空
        self.val = val
        self.next = next


class LinkedList: # 链表类定义
    def __init__(self, head=None): # 构造函数初始为空
        self.head = head

    def __str__(self):
        nodes = [] # 初始化空列表
        current = self.head # 当前current结点指针
        while current:
            nodes.append(str(current.val)) # 把当前结点的数据部分转成字符串放进列表
            current = current.next
        return "->".join(nodes) + "->None" # join()方法用于将列表中的所有字符串元素连接成一个单独的字符串，连接的元素之间用箭头->分隔。


def create_linked_list_from_input(): # 从输入创建链表
    input_str = input("请输入数字，用空格分隔：")
    values = list(map(int, input_str.split())) # input()输入返回的是字符串要转成int然后生成列表

    if not values: # 如果输入为空返回空列表
        return LinkedList()

# 这里用的头插法创建链表
    head = None # 初始化头结点为空
    for val in reversed(values): # 遍历values列表
        head = ListNode(val, head) # 每次遍历生成一个新结点，并将新结点的next指针指向旧头结点 next指针部分放的是旧head 这样就产生了一个有关系的链表

    return LinkedList(head) # 返回头结点的链表


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# 主程序
if __name__ == "__main__": # 这行代码用于检查当前模块是否是程序的入口点。换句话说，如果这段代码作为一个独立的程序被运行，__name__的值将是"__main__"。
# 如果这段代码被作为模块导入到其他程序中，__name__的值将是该模块的名称，__name__=='__main__'就为false了
# 这种结构可以确保某些代码只有在模块被直接运行时才会被执行，而在被导入时不执行。这对于测试代码、调试或提供一些功能而不希望它们在导入时被调用非常有用。

    # 创建链表
    print("创建链表:")
    linked_list = create_linked_list_from_input() # 自定义的函数
    print("创建的链表:", linked_list)

    # 查找中间节点
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    print("中间节点值:", middle_node.val if middle_node else None)
