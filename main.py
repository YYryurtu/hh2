import random
class Human:
    HP=30
    money=30
    def __init__(self,name,age,profesion):
        self.age = age
        self.name = name
        self.profesion = profesion
    def isalive(self):
        if(self.HP <= 0 or self.money <=0):
            print("You die")
    def work(self):
        self.HP-=2
        self.money+=35
    def rest(self):
        self.HP+=4
        self.money-=10
    def shop(self):
        self.HP+=10
        self.money-=15
    def sport(self):
        self.HP-=4
        self.money-=5
    def sleep(self):
        self.HP+=10
        self.money+=0

class_1 = Human("Yaroslav",24,"doctor")
print(class_1.name,class_1.age,class_1.profesion)

user = input("Print + to start live")
if user=="+":
    people = Human("Yaroslav", 24, "doctor", )
    for i in range(365):
        rand_action = random.randint(1, 5)
        if (rand_action == 1):
            people.work()
        elif (rand_action == 2):
            people.rest()
        elif (rand_action == 3):
            people.shop()
        elif (rand_action == 4):
            people.sport()
        elif (rand_action == 5):
            people.sleep()
else:
    print("No print +")



