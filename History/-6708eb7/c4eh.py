import re

# Target String one
str1 = "Emma's luck numbers are 251 761 231 451"

# pattern to find three consecutive digits
string_pattern = r"\d{3}"
# compile string pattern to re.Pattern object
regex_pattern = re.compile(string_pattern)

# print the type of compiled pattern
print(type(regex_pattern))
# Output <class 're.Pattern'>

# find all the matches in string one
result = regex_pattern.findall(str1)
print(result)
# Output ['251', '761', '231', '451']

# Target String two
str2 = "Kelly's luck numbers are 111 212 415"
# find all the matches in second string by reusing the same pattern
result = regex_pattern.findall(str2)
print(result)
# Output ['111', '212', '415']