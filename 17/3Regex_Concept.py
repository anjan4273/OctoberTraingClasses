import re

line = "bangaloreDELHI Pune 1234 @!# No CHENNAI 56789"

print(re.search("...........................", line).group())
print(re.search("[^A-Za-z0-9_]", line).group())