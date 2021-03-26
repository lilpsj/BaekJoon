'''
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
    print("*" * i)

# 내가 제출한 답안 : 오답
# 입력 부분을 빼먹고, 파이썬 문자열 곱셈의 특징을 못살림
star = "*"
for line in range(1, 6):
    print(star * line)
