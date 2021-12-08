str="hello world"
str1=""
for i in range(len(str)):
    str1=str1+str[len(str)-1-i]
str1=str1.title()
print(str1)