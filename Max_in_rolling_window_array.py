from collections import deque
from typing import List
def max_roll(arr: List[int], m: int):
    de = deque([0])
    for i,n in enumerate(arr):
        if i>=m and de[0]==arr[i-m]:
            de.popleft()
        while de and de[-1]<n:
            de.pop()
        de.append(n)
        if i>=(m-1):
            print(de[0], end=' ')
arr = [2, 7, 3, 1, 5, 2, 6, 2]

max_roll(arr,m)