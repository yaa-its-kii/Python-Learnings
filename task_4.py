star=str(input("Enter a word:"))
Length=len(star)
if Length%2==0:
    print(star.upper())
elif Length%3==0:
    Slice=star[::-1]
    print(Slice)
else:
    print(star.lower())
