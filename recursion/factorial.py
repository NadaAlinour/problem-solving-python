# factorial function (recursion)
# conditions: 0! -> 1, n! -> n(n - 1)!, where n > 0
# 3! -> 3 * 2! -> 2! = 2 * 1! -> 1! = 1 * 0!

def factorial(n):
  if not isinstance(n, int):
    print('factorial is only defined for integers')
    return None
  if n == 0:
    return 1
  
  return n * factorial(n - 1)


n = input('Enter the integer whose factorial value you want to calculate\n')
print(factorial(int(n)))


