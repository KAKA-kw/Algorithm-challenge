def splitNumberSum(n):
  sum = 0
  for s in str(n):
    sum += int(s)
  return sum

n = int(input())
count = 0
for i in range(n+1):
  if (i + splitNumberSum(i) == n):
    print(i)
    count += 1
    break

if (count == 0):
  print(0)