# Write your MySQL query statement below

# group by requester_id đếm count()
# ra 1 bảng có id, có count

# tiếp tục

# group by accepter_id (đếm count)
# ra 1 bảng có id, có count


# cộng 2 giá trị 2 bảng trên vào ứng với mỗi id vào

# sau đó lấy max
WITH FriendsCount AS (
    SELECT id, COUNT(DISTINCT friend_id) AS num
    FROM (
        SELECT requester_id AS id, accepter_id AS friend_id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS id, requester_id AS friend_id FROM RequestAccepted
    ) AS Combined
    GROUP BY id
)

SELECT id, num
FROM FriendsCount
WHERE num = (SELECT MAX(num) FROM FriendsCount);




