# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_string = '';
        second_string = '';
        
        while l1:
            first_string += str(l1.val)
            l1 = l1.next
        while l2:
            second_string += str(l2.val)
            l2 = l2.next
            
        first_integer = int(first_string[::-1])
        
        second_integer = int(second_string[::-1])
        
        final_integer = first_integer + second_integer
        
        final_string = str(final_integer)[::-1]
        
        l3 = ListNode()
        l4 = None
        for i in final_string:
            
            if l3.val == 0 and l4 is None:
                
                l3.val = int(i)
                l4 = l3
            else:
                
                l4.next = ListNode(int(i))
                l4 = l4.next
            
        return l3