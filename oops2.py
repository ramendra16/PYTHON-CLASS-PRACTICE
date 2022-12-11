class person:
    def __init__(self):
        self.name="Ramendra"
        self.age=18

    # def updateNum(self,name):
    #     self.name= name


    def compareAge(self,other):
        if(self.age==other.age):
            return True
        else:
            return False



person1=person()
person2=person()


person1.age=22

#person2.compareAge(person1)
#person1.updateNum("Ramendra")





if person1.compareAge(person2):
    print("They are of same age")

else:
    print("They are of not same age")

# print(person1.name, person1.age)
# print(person2.name, person2.age)