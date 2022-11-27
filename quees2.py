numbers=[1,2,3,4,5,6,2,8,9]
for i in range(0,len(numbers)-1):
    if numbers[i]==2:
        numbers.pop(i)
        numbers.insert(i,200)
print(numbers)