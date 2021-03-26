''' N번째 줄에는 별 N개를 찍는 문제
5
'''

'''
    *
   **
  ***
 ****
*****
'''
# 모범답안
a = int(input())

for i in range(1, a+1):
    print(" " * (a-i) + "*" * i)

# 내가 제출한 답안
a = int(input())

for i in range(1,a+1):
    print("%5s" % ("*" * i))
