from random import randint
small = "abcdefghijklmnopqrstuvwyxz"
large = small.upper()
numbers = "1234567890"
special = "!!@#$%^&*()_"

print("If anything other than 'hard', 'medium' or 'low' is entered then the difficulty will automatically be hard")

crack_difficulty = input("How difficult would you like this password to be to crack (hard, medium, low) ? ")
if crack_difficulty.lower() == "hard":
    password_stuff = small + numbers + special + large
elif crack_difficulty.lower() == "medium":
    password_stuff = small + numbers + large
elif crack_difficulty.lower() == "low":
    password_stuff = small + numbers
else:
    password_stuff = small + numbers + special + large

password_length = int(input("Enter the length of the password >> "))
#password = ""
#length = 0

if password_length < 5 or password_length > 80:
    print("Minimum password length must be at least 5 and no more than 80 ")
else:
    def redo(times):
        password = ""
        length = 0
        if times == 0:
            print("\nFeeling insecure about your new password? Test it!\nhttps://www.expressvpn.com/password-generator/\nhttps://www.my1login.com/resources/password-strength-test/")
            exit()
        while length<password_length:
            if crack_difficulty.lower() == "medium":
                password = password + password_stuff[randint(0, len(password_stuff)-1)]
                if length == password_length - 1:
                    password = password + "*!$"[randint(0, 2)]
            else:
                password = password + password_stuff[randint(0, len(password_stuff)-1)]
            length += 1
        print(f"Generated password: {password}")
        redo(times - 1)
    
    generate_amt = int(input("How many passwords would you like to generate >> "))
    if generate_amt > 5 or generate_amt < 1:
        print("You must generate 1-5 passwords")
    else:
        print("\tGENERATED PASSWORDS\t\n-------------------------------------")
        redo(generate_amt)