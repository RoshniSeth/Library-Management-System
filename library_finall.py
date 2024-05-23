import random as r                                      
from datetime import datetime,date,time                 
import json                                     
import os                                               
from tabulate import tabulate                           
import time                                             


print()
print("\t\t\t","Welcome To Harmony Library")
print()
print("-"*70)
print("Read carefully the rules of Harmony Library before issuing a book.")
rules=["1. Select your desired book.","2. You have to return the earlier issued book for issuing a new book.","3. You can issue atmost 3 books."]
for i in rules:
    print(i)
print("-"*70)
print()
print()

books={"computer basics":{"Book Id":1001,"Author":"Anshuman Sharma","Number Of Books":5},"c":{"Book Id":1002,"Author":"Anshuman Sharma","Number Of Books":5},"c++":{"Book Id":1003,"Author":"Satish Marwaha","Number Of Books":5},"data structures":{"Book Id":1004,"Author":"Ravinder Singh","Number Of Books":5},"numerical methods":{"Book Id":1005,"Author":"Anmol Rana","Number Of Books":5},"dbms":{"Book Id":1006,"Author":"Dr.Harpreet Sethi","Number Of Books":5},"information technology":{"Book Id":1007,"Author":"Shivam Maini","Number Of Books":5},
        "python":{"Book Id":1008,"Author":"Pankaj Sharma","Number Of Books":5},"html":{"Book Id":1009,"Author":"Manpreet Singh","Number Of Books":5},"java":{"Book Id":1010,"Author":"Anjali Pathak","Number Of Books":5}}
print()

options_1=["i).   SIGN UP","ii).  Already a user? LOGIN","iii). LOGOUT"]

issued_books={}                                                   
customer_details={}                                               
main_dict={"customers":customer_details,"ibooks":issued_books,"books":books}    

options=["1. Issue Book","2. Book Return","3. Book Information","4. User Information","5. Quit"]


cwd=os.getcwd()                                     
file_name="book_records.txt"                        
file_path=os.path.join(cwd,file_name)               


def file_data():
    global file_name,file_path
    if os.path.exists(file_path)==True:     
        f=open(file_path,"r")                         
        data=f.read()                                 
        consumer_details=json.loads(data)             
    else:
        f=open(file_path,"w+")
        consumer_details={"customers":{},"ibooks":{},"books":books}
        f.close()
    return consumer_details


def registration():
    global customer_details
    name=input("Enter Your Full Name: ")
    for i in name:
      while not (i.isalpha() or i.isspace()):
         print("Invalid Name Entered")
         print()
         name=input("Enter Your Full Name: ")
        
    mobile_number=input("Enter Your Mobile Number(10-digit): ")
    while len(mobile_number)!=10 or not(mobile_number.isdigit()):
        print("Invalid Mobile Number Entered")
        print()
        mobile_number=input("Enter Your Mobile Number(10-digit): ")
    email_id=input("Enter Your Email Address: ")
    while "@" not in email_id or not email_id.endswith(".com"):
            print("Invalid Email Address Entered")
            print()
            email_id=input("Enter Your Email Address: ")
    
    user_id=r.randint(101,999)
    user_id=str(user_id)
    
    
    while user_id in customer_details.keys():
        user_id=r.randint(101,999)
    print()
    time.sleep(1)
    print("Congrats!You have successfully registered.")
    print("Now you are eligible to use other options.") 
    print()
    print("User Id","Name",sep="\t\t")
    print("-------","----",sep="\t\t")
    print(user_id,name,sep="\t\t")

    
    customer_details[user_id]={"Name":name,"Mobile Number":mobile_number,"Email Id":email_id,"Number Of Books Issued":0,"Books Issued":[],"Book Id":[]}
    
    
    print()
    print("-"*70)


def book_issue(user_input):
    global books,customer_details,issued_books
    print("Available Books")
    books_table=[]

    for book,info in books.items():
            books_table.append([book.title(),info["Book Id"],info["Author"],info["Number Of Books"]])

    print(tabulate(books_table,headers=["Book Name","Book Id","Author","Number Of Books"],tablefmt="grid"))

    print()

    print("User Id","Name","Number Of Books Issued",sep="\t\t",end="\t\t")
    print("Books Issued")
    print("-------","----","----------------------",sep="\t\t",end="\t\t")
    print("------------")
    print(user_input,customer_details.get(user_input).get("Name"),customer_details.get(user_input).get("Number Of Books Issued"),sep="\t\t",end="\t\t\t")
    print(*customer_details.get(user_input).get("Books Issued"),sep=",")
    print()
    print("To go back to other available options type quit instead of book name.")
    if customer_details.get(user_input).get("Number Of Books Issued")==3:
              print()
              time.sleep(1)
              print("You have already taken three books.Please return the issued books for issuing new book.")
              print()
    else:
        while True:
            print()
            book_name=input("Enter the name of the book you want: ")
            if book_name=="quit":
                    time.sleep(1)
                    print("Exiting book issue option.")
                    print()
                    break
            else:
                if book_name not in books.keys():
                        time.sleep(1)
                        print("Wrong name entered.")
                        print("Enter the valid name.")
                        print("To go back to other available options type quit instead of book name.")
                        print()

                elif books.get(book_name).get("Number Of Books")==0:
                    print("This book is out of stock.")
                    print()
                    
                elif books.get(book_name).get("Book Id") in customer_details[user_input]["Book Id"]:
                    print("This book is already issued to you.")
                    print()
                    
                else:    
                    date_of_issuance=datetime.now()
                    issuance_date=date_of_issuance.strftime("%Y-%m-%d %H:%M:%S")
                    new_status=customer_details.get(user_input).get("Number Of Books Issued")+1
                    customer_details[user_input]["Number Of Books Issued"]=new_status
                    time.sleep(2)
                    print("Congrats!Book is issued.")
                    print("Return the book after 15 days or fine of Rs 300 is charged.")
                    print()
                    issued_books[book_name]={"Date Of Issuance":issuance_date}
                    customer_details[user_input]["Books Issued"].append(book_name)
                    customer_details[user_input]["Book Id"].append(books.get(book_name).get("Book Id"))
                    books[book_name]["Number Of Books"]=books.get(book_name).get("Number Of Books")-1
                    time.sleep(1)
            
            
        print() 
        print("-"*70)


def book_return(user_input):
    global books ,issued_books,customer_details 
    while True:
        print("To go back to other available options type quit instead of book name.")
        book_name=input("Enter the name of the book you want to return: ")
        if book_name=="quit":
                time.sleep(1)
                print("Exiting book return option.")
                print()
                break
        else:
             if book_name not in books.keys():
                time.sleep(1)
                print("Wrong name entered.")
                print("Enter the valid name.")
                print()
             elif book_name  not in issued_books.keys():
                        time.sleep(1)
                        print("Wrong book name entered.")
                        print("Please tell correct name of book to return it.the book name you have entered is not in issued books list.")
                        print("To go back to other available options type quit instead of book name.")
                        print()
             else:
                 time.sleep(1)
                 print("User Id:                 ",user_input)        
                 print("Name:                    ",customer_details.get(user_input).get("Name"))
                 print("Mobile Number:           ",customer_details.get(user_input).get("Mobile Number"))
                 print("Email Id:                ",customer_details.get(user_input).get("Email Id"))
                 print("Issued Books:            ",",".join(customer_details.get(user_input).get("Books Issued")))
                 print("Date & Time Of Issuance: ",issued_books.get(book_name).get("Date Of Issuance"))
                 print()
                 date_of_return=datetime.now()
                 return_date=date_of_return.strftime("%Y-%m-%d %H:%M:%S")
                 new_status=customer_details.get(user_input).get("Number Of Books Issued")-1
                 customer_details[user_input]["Number Of Books Issued"]=new_status
                 time.sleep(2)
                 print("Congrats!book is successfully returned.")
                 print("Thank  you for visiting us.")
                 print()
                 print("Date Of Return: ",return_date)
                 issued_books.pop(book_name)
                 customer_details[user_input]["Books Issued"].remove(book_name)
                 customer_details[user_input]["Book Id"].remove(books.get(book_name).get("Book Id"))
                 books[book_name]["Number Of Books"]=books.get(book_name).get("Number Of Books")+1
                 print()


def book_information():
      global books
      print("Available Books")
      print()
      books_table=[]

      for book,info in books.items():
            books_table.append([book.title(),info["Book Id"],info["Author"],info["Number Of Books"]])

      print(tabulate(books_table,headers=["Book Name","Book Id","Author","Number Of Books"],tablefmt="grid"))


def user_information(user_input):
    print()
    time.sleep(2)
    print("User Id:                ",user_input)
    print("User Name:              ",customer_details.get(user_input).get("Name"))
    print("Mobile Number:          ",customer_details.get(user_input).get("Mobile Number"))
    print("Email Id:               ",customer_details.get(user_input).get("Email Id"))
    print("Number Of Books Issued: ",customer_details.get(user_input).get("Number Of Books Issued"))
    print("Books Issued:           ",",".join(customer_details.get(user_input).get("Books Issued")))
    print("-"*70)
            
file_dataaa = file_data()                      
main_dict = file_dataaa                                                 
customer_details=main_dict["customers"]           
issued_books=main_dict["ibooks"]                  
books=main_dict["books"]


def library(main_dict):
    
    while True:
        print("-"*70)
        print("Choose the required option.")
        print("Type the serial order of the option to select it.")
        for i in options_1:
            print(i)
        print()
        print("-"*70)
        valid_inputs=["i","ii","iii"]
        user_choice=input("enter the required option: ")
        while user_choice not in valid_inputs:
            time.sleep(1)
            print("Invalid Option Entered")
            print("Please enter the option from the available options only.")
            user_choice=input("enter the required option: ")
        print()

        
        if user_choice=="iii":
            time.sleep(5)
            print("Thank You for using Harmony Library")
            print("Visit Again!")
            print("-"*70)
            main_dict["customers"]=customer_details
            main_dict["ibooks"]=issued_books
            main_dict["books"]=books
            file = open(file_path, 'w')
            file.writelines(json.dumps(main_dict))
            file.close()
            break
        else:
             if user_choice=="i":
                registration()
             elif user_choice=="ii":
                        user_input=input("enter your user id(3-digit): ")
                        while user_input not in customer_details.keys():
                            time.sleep(3)
                            print("invalid user id entered")
                            print("enter the correct user id to view the available services.")
                            print()
                            user_input=input("enter your user id(3-digit): ")
                       
                
                        print()
                        print("-"*70)
                        print("choose the required option")
                        for i in options:
                                print(i)
                        print()
                        while True:
                                valid_input=["1","2","3","4","5"]
                                user_option=input("enter the required option: ")
                                while user_option not in valid_input:
                                                time.sleep(3)
                                                print("invalid option entered")
                                                print("please enter the option from the available options only")
                                                user_option=input("enter the required option: ")
                                user_option=int(user_option)
                                print()
                                         
                                if user_option==5:
                                               time.sleep(5)
                                               print("Thank You for using Harmony Library")
                                               print("Enter option (iii) to logout.")
                                               break
                                else:
                                  if user_option==1:
                                             book_issue(user_input)
                                  elif user_option==2:
                                             book_return(user_input)
                                  elif user_option==3:
                                             book_information()      
                                  elif user_option==4:
                                             user_information(user_input)
                         
library(main_dict)

