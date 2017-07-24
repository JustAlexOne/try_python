import sys

long_string = "some really long string with a lot of text"

print(long_string[0:4])

print(long_string[-4:]) # last 5 chars

print(long_string[:-4]) # everything up to the last 4 chars

print("%c is my %s letter and my number %d number is %.5f" % ('A', "favorite", 1, .25))

print(long_string.capitalize())

print(long_string.find("really"))

print(long_string.isalpha()) # is contains only letters (doesn't ignore spaces)

print(long_string.isalnum()) # is contains only numbers

print(long_string.replace(" ", "").isalpha())

with_spaces = " d "
print(len(with_spaces))
strip = with_spaces.strip()
print(len(strip))

print("Hello {0}!".format("Alex")) # Hello Alex!

print(sys.path)