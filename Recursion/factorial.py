def factorial(n):
  # Base step
  if n == 0 or n == 1:
    return 1

  # Recursive step
  return n * factorial(n-1)

for i in range(10):
  print(f"{i}! = {factorial(i)}")

# 0! = 1
# 1! = 1   
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
