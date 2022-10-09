year=float(input("for how many years you are working in this company?"))
salary=float(input("what is your current salary?"))

if year>5:
    print("you will get a bonus amount of 1000rs")
    print("your salary after bonus", salary+1000)

else:
    print("sorry, you are not eligible for any bonus")
