def count_ones(n: int):
    ans = 0
    pow10 = 1
    while pow10 <= n:
      divisor = pow10 * 10
      quotient = n // divisor
      remainder = n % divisor
      if quotient > 0:
        ans += quotient * pow10
      if remainder >= pow10:
        ans += min(remainder - pow10 + 1, pow10)
      pow10 *= 10

    return ans
      

# Example usage:
n = int(input())
result = count_ones(n)
print(f"Số lượng chữ số 1 từ 0 đến {n} là {result}")
print(777%10)