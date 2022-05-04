def fib(n):
  # Base step
  if n == 0:
    return 0
  # Base step
  if n == 1:
    return 1
  # Recursive step
  if n >=2: 
    return (fib(n - 1) + fib(n - 2))


for i in range(5+1):
  print(f"fibonacci({i}) = {fib(i)}")

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(3) = 2
# fibonacci(4) = 3
# fibonacci(5) = 5