class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length +=1
            
        k = k % length
        
        if k == 0:
            return head
        
        current = head
        for _ in range(length-k-1):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        current = new_head
        while current.next:
            current = current.next
        current.next = head
        return new_head

class Solution1(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Handle special cases
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Calculate the actual rotation amount
        k = k % length

        if k == 0:
            return head  # No rotation needed

        # Find the new tail and break the list
        current = head
        for _ in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None  # Break the list

        # Connect the old tail to the old head
        current = new_head
        while current.next:
            current = current.next
        current.next = head

        return new_head


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Tạo danh sách liên kết ban đầu từ ví dụ 1: [1,2,3,4,5]
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Tạo danh sách liên kết ban đầu từ ví dụ 2: [0,1,2]
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)

# Khởi tạo đối tượng Solution
solution = Solution1()
   
# Test ví dụ 1
k1 = 3
result1 = solution.rotateRight(head1, k1)
print("Ví dụ 1 - Kết quả:")
printLinkedList(result1)  # Kết quả: [4,5,1,2,3]

# Test ví dụ 2
k2 = 4
result2 = solution.rotateRight(head2, k2)
print("Ví dụ 2 - Kết quả:")
printLinkedList(result2)  # Kết quả: [2,0,1]