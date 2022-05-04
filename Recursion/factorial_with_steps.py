def factorial(n, init_value, steps=False):
  # Print steps
  if steps: 
    print((init_value-n)*"\t" + f"Call factorial({n})")
  
  # Base step
  if n == 0 or n == 1:
    # Print steps
    if steps: 
      print((init_value-n+1)*"\t" +"Return 1")
    return 1

  # Print steps
  if steps: 
    print((init_value-n+1)*"\t" + f"{n}*Return({n-1})")
  
  # Recursive step
  fact = factorial(n-1, init_value, steps)
  result = n*fact

  # Print steps
  if steps: 
    print((init_value-n+1)*"\t" + f"Return {n}*{fact}={n*fact}")
  return result

print(f"Result = {factorial(5,5,True)}")

# Call factorial(5)
#         5*Return(4)
#         Call factorial(4)
#                 4*Return(3)
#                 Call factorial(3)
#                         3*Return(2)        
#                         Call factorial(2)  
#                                 2*Return(1)
#                                 Call factorial(1)
#                                         Return 1
#                                 Return 2*1=2
#                         Return 3*2=6
#                 Return 4*6=24
#         Return 5*24=120
# Result = 120