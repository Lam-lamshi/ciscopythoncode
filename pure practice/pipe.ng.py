age = int(input("enter your age : "))
for x in range(1000):
    if x <= age:
        print(x,age)
class Pig:
    def __init__(self,age,date):
        self.age=age
        self.date=date
    def get_age(self):
        return self.age
    def get_date(self):
        return self.date
    def set_age(self):
        return self.age
d = Pig(34,12)
d.set_age(23)
print(d.get_age())


