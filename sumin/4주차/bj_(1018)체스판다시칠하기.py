def getPaintCount (graph):
  check = ['W','B', 'W', 'B', 'W', 'B', 'W', 'B']
  count_one = 0
  count_two = 0
  for i in range(len(graph)):
    if i % 2 == 0:
      for ai, bi in zip(graph[i], check):
        if ai != bi:
          count_one += 1
        else:
          count_two += 1
    else:
      for ai, bi in zip(graph[i], check):
        if ai == bi:
          count_one += 1
        else:
          count_two += 1
  return min(count_one, count_two);


n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

result = n*m
for i in range(n-8+1):
  for j in range(m-8+1):
    sub_array = [row[j:j+8] for row in graph[i:i+8]]
    if result > getPaintCount(sub_array):
      result = getPaintCount(sub_array)
print(result)
