star=input("Enter a sentence:")
z=0
if len(star)%2==0:
    Y=len(star)//2
else:
    Y=len(star)
for i in range(1,Y+1):
    z+=i
print("The sum:",z)
