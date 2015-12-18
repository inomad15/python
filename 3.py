#_*_coding:utf-8_*_
def sum_and_mul(a, b):
    return a+b, a*b

r = sum_and_mul(3, 4)
print(r)

def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s입니다.' % nick)

say_nick('천재')
say_nick('바보')
say_nick('땅콩')
