filestream = open('input_02.txt')
relt = 0
numlist = filestream.readlines()
for i in numlist:
    relt = relt + int(numlist)

print(relt)
filestream.close()
