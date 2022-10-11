numbers=[]
x=0
for i in range (5):
    numbers.append(int(input("input?")))
total=sum(numbers)
avg=total/5
while x<5:
    if numbers[x]>avg:
        print(numbers[x])
    x=x+1
# Make your Code******************************
