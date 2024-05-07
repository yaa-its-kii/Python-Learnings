##1 Given a number say N, get all numbers from -N to N and store it in a list and print this list.
##N=int(input("Enter the number:"))
##K=[]
##for i in range(-N,N+1):
##    K.append(i)
##print("The numbers from -N to +N:",K)


###2 Get a string as an input and return true if that string is a valid vehicle registration number or not.
##p=str(input())
##if len(p)==12 or len(p)==13:
##    if p[0:2].isalpha() and p[3:5].isdigit() and (p[6:7] or p[6:8]).isalpha and p[9:13].isdigit():
##        print("Valid")
##    else:
##        print("Not valid")
##else:
##    print("Not Valid")

###3 Get a letter as an input and print the Indian state name starts with that letter, if more names exists print all in ascending order. 
##a=['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala','Madhya Pradesh', 'Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland', 'Odisha', 'Punjab','Rajasthan', 'Sikkim','Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh']
##o=input("Enter the character:").upper()
##for i in a:
##        if i[0]==o:
##            print(i)


####4 Using the above list, print all the states in descending order along with its total length count.
##b=['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala','Madhya Pradesh', 'Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland', 'Odisha', 'Punjab','Rajasthan', 'Sikkim','Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh']
##l=[]
##for i in range(17,0,-1):
##        for j in b:
##                if i==len(j):
##                        l.append(j)
##for i in l:
##        print(i,len(i),sep="=>")

#5 Write a program to find if a number is an armstrong number or not.
a=input("Enter the number:")
k=0
for i in a:
    k+=int(i)**3
if int(a)==k:
    print(k,"is a armstrong number.")
