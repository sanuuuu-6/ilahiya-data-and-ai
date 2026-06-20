def average(numbers):
    return numbers/a


a = int(input("Enter a number: "))
sum =0
for i in range(a):
   i = int(input(f"Enter {i+1} value: "))
   sum = sum+ i

avg = average(sum)
print(f"average is {avg}")