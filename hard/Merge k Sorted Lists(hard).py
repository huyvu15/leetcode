class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        a = []
        for i in lists:
            while i is not None:
                a.append(i.val)
                i = i.next
        a.sort()

        result = ListNode() 
        current = result
        for val in a:
            current.next = ListNode(val)
            current = current.next
        
        return result.next
        
        

def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

test_lists = [[1,4,5],[1,3,4],[2,6]]

list_nodes = [list_to_linked_list(lst) for lst in test_lists]

solution = Solution()

merged_result = solution.mergeKLists(list_nodes)
while merged_result:
    print(merged_result.val, end=" -> ")
    merged_result = merged_result.next