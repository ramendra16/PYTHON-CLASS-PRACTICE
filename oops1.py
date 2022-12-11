# class laptop:
#     def __init__(self, name, processor):
#         self.name = name
#         self.processor = processor

#     def printOutput(self):
#         print("My laptop name is: ",self.name, "and the processor is: ", self.processor)

# laptop1=laptop("asus", "i7")
# laptop2=laptop("hp", "i9")

# laptop1.printOutput()
# laptop2.printOutput()

class person:
    def __init__(self, name, rollNum):
        self.name=name
        self.rollNum=rollNum

    def printOutput(self):
        print("My name is: ",self.name, "and my rollNum is: ", self.rollNum)

person1=person("Ramendra", "50")
person2= person("Ram","49")

person1.printOutput()
person2.printOutput()

print(id(person1))
print(id(person2))
#names that changes with diffrent instances with diffrent variable is called instance variable


        
        