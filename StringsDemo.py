str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str3 = "RahulShetty"

print(str[1]) #grabs a

print(str[0:5]) #grabs first five characters

print(str+str1) #concatenates two strings

#extracting data from a string, comparing it to another string

print(str3 in str) #substring check

#splitting strings

var = str.split(".") #breaks string into two strings
print(var)
print(var[0])

#trim removes white spaces

str4 = " great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
