# AND
print("and operator")
score = 55
age = 18
if score >= 50 and age >= 18:
    print("Eligible")
else:
    print("Not eligible")
print("end of and opeator")

# OR
print("or operator")
score = 55
age = False
if score >= 50 or age:
    print("Eligible")
else:
    print("Not eligible")
print("end of or operator")

# NOT
print("not operator")
score = 55
age = 10
student = True
if (score >= 50 or age >= 18) and not student:
    print("Eligible")
else:
    print("Not eligible")
print("end of not operator")
