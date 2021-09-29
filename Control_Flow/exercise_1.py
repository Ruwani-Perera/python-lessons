count = 0
for number in range(1, 10):
    remainder = number % 2

    if remainder == 0:
        count += 1
        print(number)
print("We have", count, "even numbers")
