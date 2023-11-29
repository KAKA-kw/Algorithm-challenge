test = int(input())
for _ in range(test):
  n, m = map(int, input())
  array = []
  input_data = list(map(int, input().split()))
  for i in range(0, n, m):
    array.append(input_data[i, i+m-1])
  data = [[0 * m] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if (i+1 < n):
        data[i+1][j] = max(data[i+1][j], data[i][j] + array[i+1][j])
      if (j+1 < m):
        data[i][j+1] = max(data[i][j+1], data[i][j] + array[i][j+1])
      if (i+1 < n and j+1 < m):
        data[i+1][j+1] = max(data[i+1][j+1], data[i][j] + array[i+1][j+1])
  result = 0
  result = max(result, max(result[n-1]))
  print(result)
