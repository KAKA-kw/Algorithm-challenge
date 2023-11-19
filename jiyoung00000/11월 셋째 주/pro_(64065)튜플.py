import re
from collections import Counter


def solution(s):
    s = re.findall('\d+', s)
    counter = Counter(s)
    return [int(num) for num, _ in counter.most_common()]
