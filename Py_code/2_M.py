# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = None
        s = 0
        count = 0
        digit = 0
        while (l1 or l2):
            if l2:
                s += l2.val*(10**count)
                l2 = l2.next
            if l1:
                s += l1.val*(10**count)
                l1 = l1.next
            count += 1
        s= str(s)
        for i in s:
            t = ListNode(int(i))
            t.next = r
            r = t
        return r
