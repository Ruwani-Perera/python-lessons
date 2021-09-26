temperature = 27
if temperature > 26:
    print("It's warm")
    print("Drink water")
print("Done")

# Method 1>> if, elif, else
score = 74
if score >= 75:
    print("A")
elif score >= 65:
    print("B")
elif score >= 55:
    print("C")
else:
    print("Fail")
print("Completed 1")

# Method 2
score = 55
if score >= 75:
    massage = "Distinction Pass"
elif score >= 65:
    massage = "Ordinary Pass"
elif score >= 55:
    massage = "Simple Pass"
else:
    massage = "Fail"
print(massage)
print("Completed 2")

# method 3- Ternary Opertor
score = 35
new_massage = "A" if score >= 75 else "Fail"  # Ternary Operator
print(new_massage)
print("Completed 3")
