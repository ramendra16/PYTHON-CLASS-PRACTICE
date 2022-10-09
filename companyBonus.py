#COMPANY WILL GIVE BONUS ON THE FOLLOWING CRITERIA

#TIME SPENT IN COMPANY                      BONUS
#GREATER THAN 10 YEARS                       10%
#MORE THAN 6 AND LESS THAN 10                8%
#LESS THAN 6                                 5%


#ASK THE SALARY AND TIME SPENT FROM THE USER
#PRINT THE NET BONUS AMOUNT ACCORDINGLY




years=float(input("enter your working years"))
salary=float(input("enter your current salary"))

if years>10:
    print("your salary after bonus",salary+ salary*0.1)

elif years>6 and years<10:
    print("your salary after bonus", salary+ salary*0.08)

elif years<6:
    print("your salary after bonus", salary+salary*0.05)

else:
    print("no bonus")