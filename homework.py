n = int(input("Please enter a number: "))

count = 0
i = n

while i > 0:
    i = i // 10
    count = count + 1

print("The total number of digits is", count)
