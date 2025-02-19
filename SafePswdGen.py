import random # Import the random module
import string # Import the string module

chars = string.ascii_letters + string.digits + string.punctuation # Define the characters to be used

while True:
    
    userRange = input("Enter the length of the password: ") # Ask the user for the length of the password
    
    if userRange == "":
        print("Please enter a number") #
    
    else:
        userRange = int(userRange) # Convert the user input to an integer
        
        if userRange < 8:
            print("The password must be at least 8 characters long") # Check if the password is long enough
        else:
            break

        

while True:    
    userRangePunc = input("Enter the amount of symbols that you deserve in your password: ") # Ask the user for the amount of special characters in the password
    
    if userRangePunc == "":
        print("Please enter a number")
    else:
        userRangePunc = int(userRangePunc)
        if userRangePunc > userRange:
            print("The amount of special characters must be less than the length of the password") 
        else:
            break

    
SecurePswd = "" 
PswdChecker = 0
while True:
    SecurePswd = ""  # Reset password each iteration
    PswdChecker = 0  # Reset special character count

    for i in range(userRange):
        charChossed = random.choice(chars)
        SecurePswd += charChossed

        if charChossed in string.punctuation:
            PswdChecker += 1

    if PswdChecker == userRangePunc and len(SecurePswd) == userRange:
        break

print("This is your new password: " + SecurePswd)

