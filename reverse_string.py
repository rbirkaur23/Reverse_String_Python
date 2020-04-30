def reverse(s):
    rev=""
    for i in range(len(s)-1,-1,-1):
       rev=rev+s[i]
    return(rev)
p=input("Enter string: ")
print("Reversed string: ",reverse(p))
