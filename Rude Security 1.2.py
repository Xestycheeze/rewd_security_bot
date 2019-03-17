
known_users={"username":"password"}#This is the storage for registered users, in the form of
                                   #[username]:[password],[username2],[nu_password_repeat],etc


def username_validity(username):#This checks if the username is valid
                                #before user can register with that name
    
    allowed_characters="""ABCDEFGHIJKLMNOPQRSTUVWXYZ           
                        abcdefghijklmnopqrstuvwxyz1234567890""" #Special characters are not allowed                                          
    allowed_character_list=list(allowed_characters)
    username_character_list=list(username)
    username_character_allowed=True
    for character in username_character_list:
        if character not in allowed_character_list:
            username_character_allowed=False #This checks if username has banned characters
    if username=="": #Username cannot be blank
        print("Username cannot be blank! Try again you cheeky alien!")
        return False
    elif len(username)<6:#Username cannot be too short
        print("You gotta make a longer username, lazy alien! At least 6 characters will ya?")
        return False
    elif username_character_allowed==False:#Username cannot contain special characters
        print ("You have alien characters in your username! Only alphanumeric ones are allowed!")
        return False
    elif username in known_users:#Username cannot be already registered
        print ("This name is registered!")
        return False
    else:
        return True

def set_password(username):
    password=False
    while password==False:
        nu_password=input ("Set your password!")
        nu_password_repeat=input ("Give me it again! Making sure you don\'t phatfinger!")
        if nu_password==nu_password_repeat:#Makes sure consistent input
            password_chars=list(nu_password)
            letters_list=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            numbers_list=list("1234567890")
            contains_letters=False
            contains_numbers=False
            
            for char in password_chars:
                if char in letters_list:
                    contains_letters=True
                if char in numbers_list:
                    contains_numbers=True
                
            if len(nu_password)<=7:#Password cannot be too short
                print ("Make a longer password! Like at least 8 characters!")
            elif nu_password==username:#Password cannot be too easy to guess
                print ("Password cannot be the same as username, you dumbo!")
            elif contains_letters==False or contains_numbers==False:#Password must contain both
                                                                    #letters and numbers
                print("You must have at least 1 letter or 1 number in your password!")
            else:
                print ("Password and username stored!")
                password=nu_password
                known_users[username]=password #Verified users and passwords stored in database
        else:
            print ("You phatfingered alien! Make sure you enter the same password twice!")
    print ("Registration complete!")
    input()

def registration(username):#Combines username validity check and password setting,
                           #denying any unusable inputs
    while username_validity(username)==False:
        username=input("Your username won't work! Give me a new username!")
    set_password(username)

def call_police(): #LOL, will come into use later
    while True:
        print ("WEE WOO")
    
while True:
    print ("You are not welcomed to SekuriTee,the world's rudest security system!")
    print ("But if you want to come anyways, then no one will stop you... I guess.")
    username=input ("Enter your username!").strip()#No spaces after the name

    if username not in known_users: 
        print ("Your username is not recognized, alien!")
        intention="Unknown"
        while intention=="Unknown":
             register=input ("Do you want to register? ").strip().capitalize()
             if register=="Yes":
                intention="Yes"
                keep_username="Unknown"
                while keep_username=="Unknown":
                    keep_username=input ("Do you want to keep your previously entered username?").strip().capitalize()
                    if keep_username=="Yes":
                        registration(username)
                    elif keep_username=="No":
                        username=input ("Tell me what do you want your username to be!")
                        registration(username)

                    else:
                        print ("Your reponse is invalid!")#If they do not respond with "Yes" or "No"
                        print ("""The only accepted reponses are "Yes" or "No".""")
                        keep_username="Unknown"
                        
             elif register=="No":
                 intention="No"
                 print ("You will not be registered to the system.")
                 print ("We do not thank you for visiting SekuriTee.")
                 print ("Hope you have a terrible day.")
                 input()
             else:
                 print ("Your reponse is invalid!")
                 print ("""The only accepted reponses are "Yes" or "No".""")
            
                
    else: #If the user has been registered
        password_correct=False
        incorrect_entries=0
        while incorrect_entries<4:#3 attempts to input correct password
            password=input("Enter your password! ")
            if password==known_users[username]:
                print("User Authorized!")
                password_correct=True
                input()
                break
            elif incorrect_entries==2:
                print("Wrong Password!You have 1 attempt left!")
                incorrect_entries+=1 
            elif incorrect_entries in [0,1,]:
                print("Wrong Password!You have "+str(3-int(incorrect_entries))+" attempts left!")
                incorrect_entries+=1
            else:
                print("Wrong password! You have no attempts left! Police will be notified!")
                input()
                call_police()#You have been caught!
                break







