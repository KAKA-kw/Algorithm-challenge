from itertools import permutations

one_to_nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
check_list = list(permutations(one_to_nine, 3))

n = int(input())

for i in range(n):
  num, s, b = map(int, input().split())
  num_str = str(num)
  count = 0

  for i in range(len(check_list)):
    strike = 0
    ball = 0
    i -= count
    check = check_list[i]
    for j in range(3):
      if check[j] == num_str[j]:
        strike += 1
      else:
        if check[j] in num_str:
          ball += 1
    if (ball != b) or (strike != s):
      count += 1
      check_list.remove(check)
print(len(check_list))

    

