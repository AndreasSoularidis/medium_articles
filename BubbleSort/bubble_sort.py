import random 
def bubble_sort(data, print_steps = False):
  n = len(data)
  for i in range(n-1):
    for j in range(n-1, i, -1):
      if data[j] < data[j-1]:
        data[j], data[j-1] = data[j-1], data[j]
    if print_steps:
      print(f"i = {i}", end="")
      print(f"\t{data}")


data = [5, 2, 9, 3, 4, 1, 8, 6]

print("Initial data: ", end = " ")
print(f"  {data}")

bubble_sort(data, True)

print("Sorted data: ", end="")
print(f"\t{data}")


# Initial data:    [5, 2, 9, 3, 4, 1, 8, 6]
# i = 0   [1, 5, 2, 9, 3, 4, 6, 8]        
# i = 1   [1, 2, 5, 3, 9, 4, 6, 8]        
# i = 2   [1, 2, 3, 5, 4, 9, 6, 8]        
# i = 3   [1, 2, 3, 4, 5, 6, 9, 8]        
# i = 4   [1, 2, 3, 4, 5, 6, 8, 9]        
# i = 5   [1, 2, 3, 4, 5, 6, 8, 9]        
# i = 6   [1, 2, 3, 4, 5, 6, 8, 9]        
# Sorted data:    [1, 2, 3, 4, 5, 6, 8, 9]


# Stress Test with 5000 experiments
# for i in range(5000):
#   # Create data
#   data = [random.randrange(0, 100) for _ in range(random.randrange(2, 100))]
#   # Copy data
#   copy_data = data[:]
#   assert bubble_sort(data) == copy_data.sort(), "Error: Both list sgould be the same"
