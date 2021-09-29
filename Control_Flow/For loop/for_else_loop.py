eligibility = False
for number in range(1, 10, 2):
    print("Attempt", number+1)
    if eligibility:
        print("succesful")
        # using this break, whole if (line 4,5,6) will exempt from execution.
        break
    # if the break in line here, this means for loop will break
else:
    print("Attempt", number+1, "times and failed")
