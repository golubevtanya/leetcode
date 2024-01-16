from collections import deque
from typing import List
def max_roll(arr: List[int], m: int):
    maxlen = m
    de_in = ([])
    de_out = ([])
    max_in = 0
    max_out = 0
    el = 0
    for n in arr:
        if not de_out and len(de_in)<m:
            max_in = max(max_in, n)
            de_in.append([n, max_in])
        if len(de_in)==maxlen:
            while de_in:
                el, _ = de_in.pop()
                max_out = max(max_out, el)
                de_out.append([el, max_out])
            max_in = 0
            max_out = 0
            print(de_out.pop()[1], end=" ")
            continue
        if len(de_out)>0:
            max_in = max(max_in, n)
            de_in.append([n, max_in])
            print(max(de_out.pop()[1], max_in), end=" ")
m = 4
arr = [2, 7, 3, 1, 5, 2, 6, 2]

max_roll(arr,m)