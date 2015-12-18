# coding=UTF-8
# memo.py

import sys
import time

def usage():
    print("""
사용방법
======
python3 %s -v : 메모를 본다.
python3 %s -a : 메모를 추가한다.
""" % (sys.argv[0], sys.argv[0]))

if not sys.argv[1:] or sys.argv[1] not in ['-v', '-a']:
    usage()
elif sys.argv[1] == '-v':
    try: print(open('memo.txt').read())
    except IOError: print("메모가 없습니다.")
elif sys.argv[1] == '-a':
    word = input("메모를 적으세요: ")
    f = open("memo.txt", 'a')
    f.write(time.ctime() + ': ' + word + '\n')
    f.close()
    print("메모가 추가되었습니다.")
