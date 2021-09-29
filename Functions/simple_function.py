def name():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")

    print(f"Hi {first_name} {last_name} ")


def selection():
    age = input("Age:")
    gender = input("Gender (F/M)>")
    if int(age) > 18 and gender.lower() == "f":
        print("Congratualtions")
        print("You have selected")


name()
selection()
