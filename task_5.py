k=str(input())
p=k[::-1]
if "Python" and "python" in k:
    print(p)
elif "Java" and "java" in k:
    print(k.upper())
else:
    print(k)
