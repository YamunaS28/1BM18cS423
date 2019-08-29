def reve(str):
    lis=str.split(" ")
    lis.reverse()
    print(lis)
    a=" "
    s2=a.join(lis)
    print(s2)
def reverse_string(str):
    lis=str .split(" ")
    lis2=" "
    for i in lis:
        lis2 +=i[::-1]
        lis2 +=" "
    print(lis2)
str1=input("enter the string")
reve(str1)
reverse_string(str1)
