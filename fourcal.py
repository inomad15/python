class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
c = FourCal()

a.setdata(5, 6)
b.setdata(7, 8)
c.setdata(900, 1000)

print(a.sum())
print(b.sum())
print(c.sum())
print(a.mul())
print(b.mul())
print(c.mul())
print(a.sub())
print(b.sub())
print(c.sub())
print(a.div())
print(b.div())
print(c.div())
