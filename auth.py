from config import *
from storage import *
import getpass

def create_newuser():
    record=[]
    user=input("Username:")
    record.append(user)
    psw=getpass.getpass("Password:")
    record.append(psw)
    role=input("Role:").lower()
    if role=="admin":
        print("\nThis role contains strong authority over data, are you sure?")
        x=input("\n(y/n):").lower()
        if x=="y" or x=="ye" or x=="yes" or x=="yes.":
            record.append("admin")
        else:
            y=input("\n\nCHOOSE ANOTHER ROLE:")
            record.append(y)
    else:
        record.append(role)
    append_record(USER_FILE,record)

def delete_user():
##1.  Read all the user records from the file into list(memory)
#2.  From the list  find and delete the user record
#3. Overwrite the file , with the updated records list from step2
    x=input("Please Enter the user you wish to delete:")
    users=read_file(USER_FILE)
    record=[]
    for user in users:
        if user[0]==x:
            if user[2]=="admin":
                input("--------!!!_WARNING:_ USER IS ADMIN!!!--------")
            y=getpass.getpass("Password required:")
            if user[1]==y:
                cd=(input("Are you sure you want to delete this user from system?(y/n):")).lower()
                if cd=="yes" or cd=="y" or cd=="yes.":
                    pass #MAKE FUNCTION WORK!!!
                else:
                    record.append(user)
            else:
                record.append(user)
        else:
            record.append(user)
    write_records(USER_FILE,USER_HEADER,record)


def login(user_name,password):
    users=read_file(USER_FILE)
    for user in users:
        if user[0]==user_name and user[1]==password:
            return True, user[2]
    return False,"INVALID"


# Write a function check_login() in auth.py that inputs username and password and  
# then calls login function to check if it s correct or not and return true or false

def check_login():
    max_attempts=3
    current_attempt=0
    while current_attempt<max_attempts:
        username = input("Please Provide your USERNAME:")
        password = getpass.getpass()
        login_success,roles=login(username,password)
        current_attempt+=1
        if login_success==False:
            if max_attempts-current_attempt==0:
                print("ACCESS PERMISSION DENIED.")
            else:    
                print("You have",max_attempts-current_attempt,"tries left.")
        elif login_success==True:
            break
    return login_success,roles
    

















