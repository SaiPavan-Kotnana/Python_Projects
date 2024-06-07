import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z']
numbers =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
'-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']

print("welcome to password generator")
ps_letters=int(input("How many letters would you like to add in your password? \n"))
ps_numbers=int(input("How many numbers would you like to add in your password?\n"))
ps_symbols=int(input("How many symbols would you like to add in your password?\n"))

#Easy level password
# password =""
# for char in range (1,ps_letters+1):
#     password += random.choice(letters)
# for char in range(1, ps_numbers+1):
#     password += random.choice(numbers)
# for char in range(1, ps_symbols + 1):
#     password += random.choice(symbols)
# print(password)

#Hard level
Password_list=[]

for char in range(1,ps_letters+1):
    Password_list.append(random.choice(letters))
for char in range(1,ps_numbers+1):
    Password_list += random.choice(numbers)
for char in range(1,ps_symbols+1):
    Password_list +=random.choice(symbols)


print(Password_list)
random.shuffle(Password_list)
print(Password_list)

password =""
for char in Password_list:
    password += char
print(password)