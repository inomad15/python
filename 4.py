#_*_coding:utf-8_*_
f = open("new.txt", 'w')

for i in range(1, 11):
    data = "%d 번째 줄입니다. \n" % i
    f.write(data)

f.close()
