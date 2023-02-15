# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

while int(age) >= 90:
    print("Sure you are.")
    age = input("What is your current age? ")

yearsLeft = 90-int(age)
print("You have %s days, %s weeks, and %s months left." % (365*yearsLeft, 52*yearsLeft, 12*yearsLeft))
