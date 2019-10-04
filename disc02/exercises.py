# 1.2 Write curry2 as a lambda function

curry2 = lambda h: lambda x: lambda y: h(x, y)

#1.5  Write a function that takes in a function cond and 
#     a number n and prints numbers from 1 to n where 
#     calling cond on that number returns True.

def keep_ints(cond, n):
  """Print out all integers 1..i..n where cond(i) is true

  >>> def is_even(x):
  ...   # Even numbers have remainder 0 when divided by 2.
  ...   return x % 2 == 0
  >>> keep_ints(is_even, 5)
  2
  4
  """
  i = 1
  while i <= n:
    if cond(i):
      print(i)
    i += 1

