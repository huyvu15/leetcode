class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    Node = ListNode()
    currrent = Node
    temp = 0
    while l1 or l2 or temp:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        temp = sum // 10
        digit = sum % 10
        
        currrent.next = ListNode(digit)
        currrent = currrent.next
    return Node.next
            
def create_linked_list(digits):
    dummy_head = ListNode()
    current = dummy_head
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy_head.next

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
