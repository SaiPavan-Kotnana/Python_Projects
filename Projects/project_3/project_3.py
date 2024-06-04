print("Thank you for choosing python pizza deliveries")
size=input("Enter S or M or L ")
add_pepperonion=input("Enter Y or N ")
extra_cheese=input("Enter Y or N ")
bill=0
if size=="S":
    bill +=15
elif size == "M":
    bill+=20
else :
    bill +=25
if add_pepperonion =="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Y" :
    bill += 1
print(f"Your final bill is:{bill}")