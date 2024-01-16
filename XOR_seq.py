start = 1
length = 1

'''
Calculate the XORs from start number with the define length,
that get's shorter by one on every iteration.
15 16 17 18/
19 20 21/22
23 24/25 26
27
15^16^17^18^19^20^21^23^24^27
'''
def compute_XOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n+1
    if n % 4 == 3:
        return 0

def solution(start, length):
    ans = 0
    end = start+length-1
    for i in range(length):
        new_start = max(0, start + i*length -1)
        new_end = end + i*(length - 1)
        print(new_start, new_end)
        ans ^= compute_XOR(new_start)
        ans ^= compute_XOR(new_end)
    return ans

print(solution(start, length))
ans = 4^9
#print(ans)