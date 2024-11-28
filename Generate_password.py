#import string module
#store all the characters in list
#take number of characters from user
#make sure number is not less than 6
#shuffle all lists
#calculate 30% and 20% of number of characters
#create password 60% letters and 40% digits and punctuation


import string
import random
def generate_password():
    s1 = list (string.ascii_lowercase)
    s2 = list (string.ascii_uppercase)
    s3 = list (string.digits)
    s4= list (string.punctuation)
 
    characters_numbers = input("How many characters you want in your password?:")


    while True:
        try:
            characters_numbers=int(characters_numbers)
            if characters_numbers<6:
                print ("You need at least 6 characters")
                characters_numbers = input("Please enter the number again:")
            else:
                 break
        except:
            print("Please enter numbers only")
            characters_numbers = input("Please enter the number again:")


    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round (characters_numbers*30/100)
    part2 = round (characters_numbers*20/100)

    password = []

    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])
    for i in range(part2):
        password.append(s3[i])
        password.append(s4[i])

    random.shuffle(password)

    password = "".join(password[0:])

    print( "Your password is:",password )
    

while True:
    generate_password()
    user_choice = input("Do you want to generate another password? (yes/no): ")
    if user_choice.lower() != 'yes':
        print ( " Thanks you to for use my program")
        print ( " Made by Ahmed Ghallab")
        break
input("---")