class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for num in range(2, int(n ** 0.5) + 1):
            if is_prime[num]:
                is_prime[num * num:n:num] = [False] * len(is_prime[num * num:n:num])
        
        return sum(is_prime)