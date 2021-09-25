course = " python programming "
# convert to upper case
print(course.upper())

# convert to lewer case
print(course.lower())

# convert as a title
print(course.title())

# remove space
print(course.strip())
print(course.lstrip())  # remove space in the left
print(course.rstrip())  # remove space in the right

# find something
# after running, the location of the "pro" will give, in this case it's 8
print(course.find("pro"))
# in here "Pro" is not available, (p- capital), then give -1 as the result
print(course.find("Pro"))

# repalce one thing with another
print(course.replace("p", "j"))  # p will replace by j >> jython jrogramming

print("pro" in course)  # gives boolean value, pro is available, so gives True
# Pro is not avaible, give False (python is case sensitive)
print("Pro" in course)
