'''
5
1 1
2 3
3 4
9 8
5 2
'''

'''
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
'''

t = int(input())

for i in range(t):
    A, B = map(int, input().split())
    print("Case #%s: %s" % (i+1, A+B))
