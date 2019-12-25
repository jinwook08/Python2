# filestream = open('input_01.txt')
# contents = filestream.read()

# result = int(contents) + 1

# filestream.close()



# filestream = open('input_01.txt')
# contents = filestream.read()

# result = int(contents) + 1

# print(result)

# filestream.close()



# filestream = open('input_01.txt')
# contents = filestream.read()

# result = contents + str(1)

# print(result)

# filestream.close()



fiestream = open('input_02.txt')
rlt = 0
cont = fiestream.read()


for i in cont :
    rlt = rlt + int(i)

print(rlt)
fiestream.close()

# fstream = open('input_02.txt')
# rlt = 0
# numlist = fstream.readlines()
# for i in numlist:
#     rlt = rlt + int(i)

# print(rlt)
# fstream.close()
