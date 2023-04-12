class Pet:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def show(self):
        print(f"i am {self.name}  and i am {self.age} years old ")
    def speak(self):
        print("i dont know what to say ")
class Dog(Pet):
    def speak(self):
        print("Bark")
class Cat(Pet):
     def speak(self):
        print("meow")

p=Pet("Tim",29)
p.show()
c=Cat("Bill", 34)
c.speak()
d=Dog("Timmy", 23)
d.speak()
