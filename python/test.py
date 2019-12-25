fstream = open('input_02.txt')
rlt = 0
numlist = fstream.readlines()
for i in numlist:
    rlt = rlt + int(i)

print(rlt)
fstream.close()
