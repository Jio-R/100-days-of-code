#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What's the bill? $"))
tip = float(input("And how much will you be tipping today?\n(%): "))/100 + 1 #Tip saved as a multiplier, i.e. 1.2 for 20%
people = int(input("Lastly, how many people will split the bill?\n"))

print("Each person should pay: $%s" % (bill*tip/people))
