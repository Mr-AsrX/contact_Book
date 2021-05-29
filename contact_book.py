import time
import json
print(40*"-")
print(f"{5*'-'}CONTACT BOOK!{5*'-'}. ")
print(40*"-")


print("1. create contact\n2.view contact \n3. edit contact \n4. delete contact ")
user = input("Enter your contact name: ")
time.sleep(2)
selction = input("input your selection; ")

files = open("contact.json","r+")

contact_list = {}
contact_list = json.load(files)



def verification(contact_name):
    
    verify_value = 0
    for data in contact_list[contact_name]:
        
            if data.count("%?") == 1:
                password_check = input("please enter your password :")
                if data == "%?"+password_check:
                    verify_value = 1
                    return verify_value 
                else:
                    retype = 0
                    print("please enter correct password ")
                    while retype < 2:
                        password_check = input("please enter your password :")
                        if data == "%?"+password_check:
                            
                            verify_value = 1
                            return verify_value
                        else:

                            print(f"please enter correct password ")
                            if retype == 1:
                                exit()
                        retype += 1

def create_contact(contact_name):
    
    print(f"hello {contact_name} create your contact : ")
    time.sleep(4)
    try:

        phone_no = str(input("enter your phone no: "))
        email = input("enter your email id: ")
        address = input("enter your Adress: ")
        privacy_agree = input("do you want to setup pasword y/n: ")
        if privacy_agree =="y":
            password  = input("Create password : ")
            password = "%?"+password
            data =[phone_no,email,address,password]

        else:
            data =[phone_no,email,address]
        
    except ValueError:
        print("please enter correct value type ")
        exit()
    
    contact_list[contact_name]=data
    
    
        
def view_contact(contact_name):
    print(f"hello welcome back {contact_name}")
    if contact_name in contact_list:
        if verification(contact_name) == 1:

            if contact_name == "admin":
                for user,data in contact_list.items():
                    print("\n"+user)
                    for data1 in data:
                        print(data1)
                
            else:
                print("your data: \n")
                view_data = contact_list[contact_name]
                for no,data in enumerate(view_data):
                    if data.count("%?"):
                        print(no, data[2:])
                    else:
                        print(no, data)
                
                
            
        else:
            print("Add password for more security")
            view_data = contact_list[contact_name]
            for no,data in enumerate(view_data):
                
                print(no, data)
            
        
    else:
        print("INVALID NAME! ")
        exit()
def edit_contact(contact_name):
    view_contact(contact_name)
    if contact_name == "admin":
        select_user = input("Enter user for edit :")
        edit_data = contact_list[select_user]
        for no, change_data in enumerate(edit_data):
            print(no, change_data)
        select_data = int(input("enter No to change that: "))
        if edit_data[select_data].count("%?")== 1:
            update_password= str(input("change password: "))
            edit_data[select_data]= "%?"+update_password
        else:

            edit_data[select_data]= str(input("edit this data: "))
        print("edit successful!")
    else:
        edit_data = contact_list[contact_name]
        select_data = int(input("enter No to change that: "))
        if edit_data[select_data].count("%?")== 1:
            update_password= str(input("change password: "))
            edit_data[select_data]= "%?"+update_password
        else:

            edit_data[select_data]= str(input("edit this data: "))
        print("edit successful!")    

def delete_data(contact_name):
  
    all =    input("want to Delete your All contact y/n :")
    if all =="y":
        print(f"deleted {contact_list.pop(contact_name)}")
    else:
        view_contact(contact_name)
        delete_data = contact_list[contact_name]
        select_data = int(input("enter No to delete that: "))
        del delete_data[select_data]
        print("delete successful!")  

if selction == "1":
    try:
        if contact_list[user]:
            print("already this name avilable try different one : ")
    except KeyError:
        create_contact(user)
if selction == "2":
    view_contact(user)
if selction == "3":
    edit_contact(user)
    
if selction == "4":
    delete_data(user)

files.seek(0)
json.dump(contact_list,files)
files.close()