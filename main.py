import random
class human:
    HP=100
    def __init__(self,money,profesion,name,age):
        self.age = age
        self.name = name
        self.money = money
        self.profesion = profesion
    def isalive(self):
        if(self.HP <= 0 or self.money <=0):
            return
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
people = human()

for i in range(5):
    rand_action = random.randint(1,5)
    if(rand_action == 1):
        people.work()
    elif (rand_action == 2):
        people.rest()
    elif(rand_action == 3):
        people.shop()
    elif (rand_action == 4):
        people.sport()
    elif (rand_action == 5):
        people.sleep()