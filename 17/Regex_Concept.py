import re
name = "bangaloreDELHI Pune 1234 @!# No CHENNAI 56789"

#2.287.43.56 Invalid IP
#3.44.21.2 Valid IP
#1.255.78.98 Invalid IP

#ip address range should be between 0 - 255

print(re.match("(\w+)\s(\w+)\s(\d+)", name).group())
print("group1 : ",re.match("(\w+)\s(\w+)\s(\d+)", name).group(1))
print("group2 : ",re.match("(\w+)\s(\w+)\s(\d+)", name).group(2))
print("group3 : ",re.match("(\w+)\s(\w+)\s(\d+)", name).group(3))
print(re.search("\w+\s\w+", name).group())
print(re.search("\W+", name).group())
print(re.search("\D+", name).group())

print("a-z small : ",re.search("[a-z]+", name).group())

print(re.findall("[a-z]+", name))
print(re.search("[0-9]+", name).group())
print(re.findall("[0-9]+", name))
print(re.search("[A-Z]+", name).group())
print("range : ",re.search("[A-Z]{2,3}", name).group())
print(re.findall("[A-Z]+", name))
print(re.findall("[A-Z]{4}", name))



