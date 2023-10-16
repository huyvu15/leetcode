# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = []
        while head.next != None:
            temp.append(head.val)
            head = head.next
        else:
            temp.append(head.val)
        print(temp)
        save = []
        for i in range(len(temp)):
            if temp.count(temp[i]) == 1:
                save.append(temp[i])
        print(save)
        result = ListNode()
        current = result
        current_val = head.val
        for val in save:
            current.next = ListNode(val)
            current = current.next
        # current.next = ListNode(current_val)
        return result.next  

# Hàm để in danh sách liên kết
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Tạo danh sách liên kết từ danh sách Python
input_list= [1,1,1,2,3]
head = ListNode(input_list[0])
current = head
for val in input_list[1:]:
    current.next = ListNode(val)
    current = current.next

# Tạo một đối tượng của lớp Solution
solution = Solution()

# Gọi phương thức deleteDuplicates để loại bỏ các phần tử trùng lặp
new_head = solution.deleteDuplicates(head)

# In danh sách liên kết sau khi xử lý
printLinkedList(new_head)
