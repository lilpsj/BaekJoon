no1 = int(input())
no2 = int(input())

no3 = no1*((no2%100)%10)
no4 = no1*((no2%100)//10)
no5 = no1*(no2//100)
result = no1*no2

print(no3, no4, no5, result, sep="\n")
