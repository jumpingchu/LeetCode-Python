# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def calc_gcd(n1, n2):
        if n2 == 0:  # 整除的情況=找到公約數
            return n1
        else:        # 沒有整除，將餘數繼續往下除
            return calc_gcd(n2, n1 % n2)  
    
    n1, n2 = head, head.next
    while n2:
        # calculate insert node
        gcd_result = calc_gcd(n1.val, n2.val)
        center_node = ListNode(gcd_result)
        
        # assign three nodes 
        # old: [n1 -> n2]
        # new: [n1 -> center -> n2]
        n1.next = center_node
        center_node.next = n2

        # move to next node
        n1 = n2
        n2 = n2.next
    
    return head
