def uniquePaths( m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def calculate_factorial(x):
            factorial = 1
            for i in range(1, x + 1):
                factorial *= i
            return factorial

        a = n - 1
        b = m + n - 2

        return calculate_factorial(b) / (calculate_factorial(b - a) * calculate_factorial(a))


# Sử dụng
a = 3
b = 7
result = uniquePaths(a, b)
print(f"C({a}!, {b}) = {result}")
