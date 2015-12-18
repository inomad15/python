#coding=UTF-8
class HousePark:
    lastname = '박'
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))

class HouseChoi(HousePark):
    lastname = '최'

class HouseKim(HousePark):
    lastname = '김'
    def travel(self, where, day):
        print("%s, %s 여행을 %d일 동안 가다." % (self.fullname, where, day))

a = HousePark('문수')
a.travel('일본')
b = HouseChoi('홍배')
b.travel('스위스')
c = HouseKim('박사')
c.travel('달나라', 10)
d = HouseChoi('민준')
d.travel('USA')
