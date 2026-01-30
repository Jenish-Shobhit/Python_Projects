#Split Calculator - Jenish Version
total_bill = float(input("enter the total amount of the bill to pay :"))
no_of_people = int(input("enter the number of people :"))
tip_amount = float(input("enter the  percent tip amount :"))
new_amount = total_bill *(1 + tip_amount/100)
each_person_split = new_amount/no_of_people
print(f"Each person should pay {each_person_split} ")


