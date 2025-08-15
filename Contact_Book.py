import csv
try:
    print("WELCOME TO CONTACT BOOK !!")

    def add_contact():
        with open("Contact_Book.csv","a",newline="") as f:
            fobj=csv.writer(f)
            if f.tell() == 0:
                fobj.writerow(["Name","Contact_number","E-mail","Address"])
            while True:
                name=input("Enter your Name ->")
                num=int(input("Enter your contact number->"))
                if len(str(num))==10:
                    pass
                else:
                    print("Invalid Number !!  Please enter a 10-digit number.")
                    break
                mail=input("Enter your Email-id->")
                if mail.endswith("@gmail.com"):
                    pass
                else:
                    print("Invalid Email !! Must end with '@gmail.com'.")
                    break
                address=input("Enter your Address->")
            
                data=[name,num,mail,address]

                fobj.writerow(data)
                
                print("Data added succesfully !!")
                print("_________________________")
                
        

                v=int(input("Do you want to add another contact? 1 for Yes, 0 for No -> "))
                if v==0:
                 break

    def view_contacts():
        with open("Contact_Book.csv","r",newline="") as f:
            reader=csv.reader(f)
            for i in reader:
                print(i)
            print("Here is all Contacts !!")


    def search():
        with open("Contact_Book.csv","r",newline="") as f:
            reader=csv.reader(f)
            a=int(input("Search by 1-Name | 2-Email\nEnter your choice->"))
            if a==1:
                b=input("Enter name->")
                for i in reader:
                    if i[0].lower()==b.lower():
                        print(i)
                    
            elif a==2:
                c=input("Enter Email->")
                for i in reader:
                    if i[2].lower()==c.lower():
                        print(i)
                     
            else:
                print("Invalid choice")


    def update():
        rows = []
        with open("Contact_Book.csv", "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
            print("what do you want to update?")
            d=int(input("Enter 1-Contact Number | 2-Address | 3-Email\nEnter your choice->"))
            if d==1:
                e=input("Enter your Name->")
                for i in rows:
                    if i[0].lower()==e.lower():
                        print("Record found")
                        f=int(input("Enter New contact number->"))
                        i[1]=f
                print("Contact number Updated successfully ")
            elif d==2:
                f=input("Enter your Name->")
                for j in rows:
                    if j[0].lower()==f.lower():
                        print("Record found")
                        g=input("Enter New address->")
                        j[3]=g
                print("Address Updated successfully ")
            elif d==3:
                k=input("Enter your Name->")
                for l in rows:
                    if l[0].lower()==k.lower():
                        print("Record found")
                        h=input("Enter New Email-id->")
                        l[2]=h
                print("Email-id Updated successfully ")

            else:
                print("Invalid Choice !")
            

            with open("Contact_Book.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)



    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        z=int(input("Enter 1 for Add New Contacts | 2 for View Contacts | 3 for Search Contacts | 4 for Update Contacts |\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nEnter Your Choice-> "))
        print("~~~~~~~~~~~~~~~~~~~~~~~|")
        if z==1:
            add_contact()

        elif z==2:
            view_contacts()

        elif z==3:
            search()

        elif z==4:
            update()
        else:
            print("Invalid Choice !")
        print("______________________________________________________")
        m = int(input("Do you want to perform another operation? 1 - Yes | 0 - No -> "))
        print("______________________________________________________")
        if m == 0:
            print("Exiting Contact Book. Goodbye!")
            break

except:
    print("**Something Went Wrong **")



