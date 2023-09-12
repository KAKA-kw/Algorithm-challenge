from itertools import combinations

array = []
for _ in range(9):
  n = int(input())
  array.append(n)

combination = list(combinations(array, 7))

for combi in combination:
  if sum(combi) == 100:
    sort_combi = sorted(combi)
    for i in sort_combi:
      print(i)
    break



