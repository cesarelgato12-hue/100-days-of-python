print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ : "))

tip = int(input("how much tip would you like to give? 10 ,12 por 15 : "))

people = int(input("How many people to spit the bill?"))

bill_with_tip = (tip / 100 * bill + bill ) / people

print(f"Each person should pay :$ {bill_with_tip}")