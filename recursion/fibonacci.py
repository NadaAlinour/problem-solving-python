# fibonacci
# conditions: fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
# where n > 1

def fibonacci(n):
  if not isinstance(n, int):
    print('fibonacci is only defined for integers')
    return None
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)


n = input('Enter the integer whose fibonacci value you want to calculate\n')
print(fibonacci(int(n)))