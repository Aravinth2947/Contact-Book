# Concepts used: dictionary, functions, loops
# Features:
# Add contact (name, phone)
# Update contact
# Delete contact
# Search contact
# Display all contacts


details = {}

def contact():
   name=input("Enter name : ")
   number = input("Enter phone number : ")
   details[name]=number

  
   
print("Contact details")
contact()
print("Details add successfully : ")
# for name,number in details.items():
#    print("Name :",name)
#    print("Number : ",number)
for i,(name,number) in enumerate(details.items(),start=1):
    print(i,".",name, number)

def choo():
   print("1.add contact")
   print("2.delete contact")
   print("3.update")

choo()
choice = int(input("Choose : "))
 
if choice == 1:
   contact()
   for i,(name,number) in enumerate(details.items(),start=1):
    print("details add sucessfully!")
    print(i,".",name, number)
    choo()
 
   
elif choice == 2:
   print(details)
   n = input("Enter name : ")
   if n in details:
      del details[name]
      print(details)
   else:
     print("contact not found") 


elif choice ==3:
    n=input("enter name")
    if n in details:
       print("1.to change name \n 2.to change number")
       a = int(input("Enter :"))
       if a == 1:
           f=input("Enter name :")
           details[f]=details.pop(n)
           for i,(name,number) in enumerate(details.items(),start=1):
            print(i,".",name, number)
       elif a == 2:
           x= input("Enter number : ")
           details[x]=details.pop(n)
           for i,(name,number) in enumerate(details.items(),start=1):
            print(i,".",name, number)

    else:
        print("contact not found")
        