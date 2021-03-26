'''
5
1 1
2 3
3 4
9 8
5 2
'''

'''
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''

t = int(input())

for i in range(t):
    A, B = map(int, input().split())
    C = A + B
    print("Case #%s: %s + %s = %s" % (i+1, A, B, C))

