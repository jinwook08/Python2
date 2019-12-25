import os
a = os.getcwd()
print(a)

# filestream = open('lap11.txt')
# contents = filestream.read()

# print(contents)


# filestream.close()
# ------------------------------------
# print(type(contents))


# filestream = open('lap11.txt')
# contents = filestream.readline()

# print(contents)


# filestream.close()


# --------------------------------

filestream = open('lap11.txt')
contents = filestream.readlines()

print(contents[0].strip())


filestream.close()