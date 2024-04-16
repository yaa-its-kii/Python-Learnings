a=int(input("Num 1:"))
b=int(input("Num 2:"))
c=int(input("Num 3:"))
for i in range(1,c+1):
    if i==1:
        print(1)
    if i%b==0 and i%a==0:
        print(i)
