#Question: if thr bill was 150$,split between 5 people, with 12%tip.
#Each person should pay (150.00/5)*1.12 ==33.6
#Round the result to decimal places = 33.60
print("Welcome to the tip calculator! ")
bill=float(input("What was the total bill ? "))
tip=int(input("How much tip would you like to expect to give ?10 , 12 0r 15 "))
people=int(input("how many people to split bill? "))
bill_with_tip= tip / 100 * bill + bill
total_bill_perhead = bill_with_tip/people
print("total bill perhead is:"" {:.2f}".format(total_bill_perhead))