num = int(input("enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"Is an armstrongnumber")
else:
    print(num,"Is not a armstrongnumber")