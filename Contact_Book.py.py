print("Welcome to Your Contact Book!")
# Creating operatioins using numbers(1,2,3,4,5)
add_num = "1"
search_num  = "2"
update_num = "3"
view_num = "4"
delete_num = "5"

# Creating detailed information of contact using dictionary.
contact_info = {"Names" : ['Sumit','Rohit','Shiv','Dev'],
                "P_number" : [8571916506,8570924035,8059232310,9728624055],
                "Email" : ['sumit1234@gmail.com','rohitkmr23@gmail.com','shiv0001@gmail.com','devsh45@gmail.com'],
                }
print("What do you wanna do: ")

#Taking input from user to select the operation.
choose = input("Add number, Search number, Update number, View all number, Delete the contact, \n if wanna add pleaase select 1 \n if wanna search the number please select 2 \n if wanna update the number pleaase select 3 \n " \
"if wanna View numbers please select 4 \n if wanna delete the data please select 5\nHere:So what would you wanna do: ")

# Executing the all operations using if-elif-else statement.

#Operation one = Adding contact.
if choose == "1":
    name = input("Name: ")
    P_num = input("Phone number: ")
    Email = input("Email: ")
    
    contact_info["Names"].append(name)
    contact_info["P_number"].append(P_num)
    contact_info["Email"].append(Email)
# contact_for.append(name)
    print(contact_info)

#Operation two = Search contact.
elif choose == "2":
    srch = input("Search by name: ")
    if srch in contact_info['Names']:
     index = contact_info['Names'].index(srch)
     num = contact_info['P_number'][index]
     email = contact_info['Email'][index]
     print("Name: ",srch,"\n","Number: ",num ,"\n","Email address: ",email)
    else:
        print("Name does'nt exit")

#Operation three = Updating contact information.
elif choose == "3":
    print("if you don't wanna update any column, enter same")
    namee = input("Enter the present name: ")
    if namee in contact_info["Names"]:
        index = contact_info["Names"].index(namee)
        new_name = input("Enter the new name: ")
        new_num = input("Enter the new number: ")
        new_eml = input("Enter the new Email: ")
        if new_name != "same":
            contact_info['Names'][index] = new_name
            if new_num != "same":
                contact_info['P_number'][index] = new_num
                if new_eml != "same":
                    contact_info['Email'][index] = new_eml
        print("Contact Updated!")
        print(contact_info)            
            
            
    else:
        print("You entered the wrong name")

#Opeartion 4 = Viewing all the contact.
elif choose == "4":
    v2 = contact_info['Names']
    view = contact_info["P_number"]
    v3 = contact_info["Email"]
    
    count = 1
    print("  Names |  Numbers   | Emails ")
    for v2,view,v3 in zip(v2,view,v3):
        print(count,v2,"|",view,"|",v3)
        count+=1

#Operation 5 = Deleting the contact.
elif choose == "5":
    dl = input("Delete contact name: ")
    if dl in contact_info['Names']:
    
      index = contact_info["Names"].index(dl)
      contact_info["Names"].pop(index)
      contact_info["P_number"].pop(index)
      contact_info["Email"].pop(index)
      print(contact_info)
      
    else:
        print("Name not found!")




