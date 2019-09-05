import string
import random

def password(userInput):
    specialCharacter=[random.choice(string.punctuation)for character in range(userInput)]
    lowercase=[random.choice(string.ascii_lowercase)for lower in range(userInput)]
    uppercase=[random.choice(string.ascii_uppercase)for upper in range(userInput)]
    numbers=[random.choice(string.digits)for number in range(userInput)]
    generatedPassword=''.join(specialCharacter+lowercase+uppercase+numbers)
    print(generatedPassword)
    print(len(generatedPassword))
    generatedPassword=''.join(random.choice(generatedPassword)for value in range(userInput))
    print(generatedPassword)

userInput=int(input("Enter the length of password:"))
password(userInput)

