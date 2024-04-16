A=int(input("Enter the number of elements:"))
B=0
print("Enter the",A, "Values:")
for i in range(1,A+1):
    C=int(input())
    B+=C
    z=C/A
operation=input("Enter the 'sum' or 'average' to be compute :")
if  operation=='sum':
    print ("The sum is:",B)
elif operation=='average':
    print("The average is:",int(z))
else:
    print("Choose sum or average to be computed: ")
