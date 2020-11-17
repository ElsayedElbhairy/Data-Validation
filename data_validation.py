# Author Name: Elsayed Elbhairy
# Creation Date: 11/15/2020
# Description: Python program to validate data from a Json file


import json 
# for regular expressions 
import re 
  
# Make a regular expression for validating an Email 
emailAddress_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# Make a regular expression for validating an phone number 
phoneNumber_reqex ='^\d([0-9 -]{0,10}\d)?$'

# Define a function for validating an Email and phone numbers
def check(email, phone):  
    if(re.search(emailAddress_regex,email) and re.search(phoneNumber_reqex,phone)):  
        return "Valid"  
          
    elif(not re.search(emailAddress_regex,email) and re.search(phoneNumber_reqex,phone)):  
        return "Email is invalid" 

    elif(not re.search(phoneNumber_reqex,phone) and re.search(emailAddress_regex,email)):  
        return "Phone is invalid" 
    else:
        return "Email and Phone are invalid"


def sort_names(info):
    sorted_data= sorted(info, key=lambda k: k['fullName'])
    return sorted_data
    
def print_cities(info):
    dict = {}
    for file_data in info:
        if check(file_data["emailAddress"], file_data["phoneNumber"]) != "Valid":
            if file_data['cityName'] not in dict.keys():
                dict[file_data['cityName']] = 1
            else:
                dict[file_data['cityName']] += 1
    dict = sorted(dict.items(), key=lambda x: x[1],  reverse=True)
    for entry in dict:
        city = entry[0]
        city += ' ==> ' + str(entry[1])
        print(city)
 
def print_contacts(info):
   
    sorted_data_dict = sort_names(info)
    for file_data in sorted_data_dict:
        contact = (file_data["fullName"])
        contact += ' ==> ' + check(file_data["emailAddress"], file_data["phoneNumber"])
        print(contact)

if __name__ == '__main__':
    with open('Contact.json') as f:
        data_dict = json.load(f)
    print("Contact List: \n")
    print_contacts(data_dict)
    print("\n\nCity List with numbers of validation errors:")
    print_cities(data_dict)


