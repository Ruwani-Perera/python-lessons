for number in range(3):
    print("Attempt", number)


for number in range(3):
    print("Attempt", number+1, (number+1)*".")

# series statrt from 1 and will end before 4
for number in range(1, 4):
    print("Attempt", number, number*"#")

# series start from 1 and will end before 10, final no represent the steps
for number in range(1, 10, 2):
    print("Attempt", number, number*"@")
