""" 
1.1 Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
Write a function that takes in the current temperature and a boolean value telling
if it is raining and returns True if Alfonso will wear a jacket and False otherwise
"""

def wears_jacket_with_if(temp, raining):
  """
  >>> wears_jacket_with_if(90, False)
  False
  >>> wears_jacket_with_if(40, False)
  True
  >>> wears_jacket_with_if(100, True)
  True
  """
  if raining == True:
    return True
  elif temp < 60:
    return True
  else:
    return False

# with one line

def wears_jacket(temp, raining):
  """
  >>> wears_jacket(90, False)
  False
  >>> wears_jacket(40, False)
  True
  >>> wears_jacket(100, True)
  True
  """
  return raining or temp < 60

"""
1.2 What is the result of evaluating the following code?
"""

def square(x):
  print("here!")
  return x * x

def so_slow(num):
  x = num
  while x > 0:
    x = x + 1
  return x / 0

# square(so_slow(5)) #Infinite Loop 

"""
1.3 Write a function that returns True if a positive integer n is a prime number and False otherwise.
"""

def is_prime(n):
  """
  >>> is_prime(10)
  False
  >>> is_prime(7)
  True
  """
  if n == 1:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    i = 3
    while i <= (n // 2):
      if n % i == 0:
        return False
      i += 2
    return True


