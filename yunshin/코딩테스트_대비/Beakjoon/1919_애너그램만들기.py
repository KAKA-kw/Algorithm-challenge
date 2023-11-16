import sys

input = sys.stdin.readline

a = list(input())[:-1]
b = list(input())[:-1]

a_set = set(a)
b_set = set(b)

# 공통의 키를 찾는다.
commonList = []
for a_key in a_set:
    if(a_key in b_set):
        commonList.append(a_key)
a_spell_cnt = {key:0 for key in commonList}
b_spell_cnt = {key:0 for key in commonList}

for spell in a:
    if(spell in a_spell_cnt.keys()):
        a_spell_cnt[spell]+=1
for spell in b:
    if(spell in b_spell_cnt.keys()):
        b_spell_cnt[spell]+=1

essential_cnt = 0
for key in commonList:
    essential_cnt += min(a_spell_cnt[key],b_spell_cnt[key])

print(len(a)+len(b)-essential_cnt*2)