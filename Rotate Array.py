def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    length = len(nums)
    
    k = k % length
    
    # Tạo một bản sao của danh sách nums để không làm mất dữ liệu ban đầu
    nums_copy = nums[:]
    
    for i in range(length):
        # Sử dụng công thức để tính vị trí mới cho phần tử
        new_idx = (i + k) % length
        nums[new_idx] = nums_copy[i]
    
    print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
