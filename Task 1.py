a=str(input("Enter a word :"))
b=len(a)
c=1
if(b%2==0):
    z=b//2
    for i in a:
        print(c*z)
        c+=1
else:
    for i in a:
        print(c*b)
        c+=1
        
    
