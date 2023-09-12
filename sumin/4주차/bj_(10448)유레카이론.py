from itertools import combinations_with_replacement

def triangleSum(n):
  sum = 0
  for i in range(n+1):
    sum += i
  return sum

def checkTriangleSum(n):
  array = []
  for i in range(1, n):
    if triangleSum(i) < n:
      array.append(triangleSum(i))
    else:
      break
  combination = list(combinations_with_replacement(array, 3))
  count = 0
  for combi in combination:
    x, y, z = combi
    if (x + y + z == n):
      count += 1
      print(1)
      break
  if (count == 0):
    print(0)



t = int(input())
test_array = []

for _ in range(t):
  n = int(input())
  test_array.append(n)

for t in test_array:
  checkTriangleSum(t)

  