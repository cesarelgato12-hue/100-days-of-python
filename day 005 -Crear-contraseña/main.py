letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]

print("welcome to the PyPassword Generator! ")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many simbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))


#password = ""

#for char in range(0,nr_letters ):

#    password += random.choise(letters)
#    print(password)

#for char in range (0,nr_symbols):
#    password += random.choise(symbols)
#for char in range (0 , nr_numbers):
 #   password += random.choise(numbers)    

#print (password) //


password_list = []

for char in range(0,nr_letters ):

    password_list.append(random.choise(letters))

for char in range (0,nr_symbols):
    password_list.append(random.choise(symbols))
for char in range (0 , nr_numbers):
    password_list.append(random.choise(numbers))

print (password_list)

random.shuffle(password_list)

print(password_list)

password = ""

for char in password_list:
    password += char 
print(f"Your password is : {password}")
