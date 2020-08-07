# Time：2020/3/420:53
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class link:
    def __init__(self):
        self.__head = None
    def add(self,k):
        node = ListNode(k)
        node.next = self.__head
        self.__head = node
        return node
class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pass
if __name__ == '__main__':
    linked=link()
    node1=linked.add(1)
    node2=linked.add(2)
    print(node1.val)
    print(node2.val)