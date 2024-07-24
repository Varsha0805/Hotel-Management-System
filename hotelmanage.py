import pickle
import os
def new():
    rec=list()
    cid=0
    if os.path.isfile("Hotel.dat"):
        f=open("Hotel.dat",'rb')
        rec=pickle.load(f)
        f.close()
    nm=input("Enter Customer Name:")
    ad=input("Enter Customer Address:")
    ag=input("Enter Customer Age:")
    cn=input("Enter Customer Country:")
    ph=input("Enter Customer Phone Number:")
    em=input("Enter Customer Email:")
    cid=len(rec)+1
    print("Your customer ID is: ",cid)
    print("-----------------------------------------------------------------------------------------")
    print("NEW CUSTOMER ENTERED IN THE SYSTEM SUCCESSFULLY! \n")
    data=[cid,nm,ad,ag,cn,ph,em]
    rec.append(data)
    f=open("Hotel.dat",'wb')
    pickle.dump(rec,f)
    f.close()
def book():
    ci=input("\nEnter Customer check-In Date (YYYY-MM-DD) :")
    cd=input("\nEnter Customer check-Out Date (YYYY-MM-DD) :")
    print("------------------------------------------------------------------------------------------------")
    print("CHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY!! \n")
def room():
    print("\n\t WE HAVE FOLLOWING ROOMS FOR YOU ")
    print("\t----------------------------------------------------------------------------------")
    print("1.Ultra Royal--------Rs. 2500") 
    print("2.Royal--------Rs. 2000") 
    print("3.Elite--------Rs. 1500") 
    print("4.Budget--------Rs. 1000")
    ch=int(input("Enter your choice: "))
    da=int(input("Enter Number of days: ")) 
    if ch==1:
        pc=2500
        print("Ultra Royal Room rent : 2500")
        print("Your Total Room rent is : Rs. ",pc)
    elif ch==2:
        pc=2000
        print("Royal Room rent : 2000")
        print("Your Total Room rent is : Rs. ",pc)
    elif ch==3:
        pc=1500
        print("Elite Room rent : 1500")
        print("Your Total Room rent is : Rs. ",pc)
    elif ch==4:
        pc=1000
        print("Budget Room rent : 1000")
        print("Your Total Room rent is : Rs. ",pc)
    rt=pc*da
    print("______________________________")
    print("FOR BOOKING YOUR ROOM,TOTAL ROOM RENT IS: ",rt)
    print("THANK YOU!! YOUR ROOM HAS BEEN BOOKED FOR: " ,da,'DAYS!')
    print("ENJOY YOUR STAY!! \n")

def resturant():
    print("\n\t WE HAVE FOLLOWING OPTIONS")
    print("\t ----------------------------------------------------------------")
    print("1.Vegetarian Combo--------------------------->> Rs.300")
    print("2.Non-Vegetarian -------------------------->> Rs.500")
    print("3.Vegetarian and Non-Vegetarian ---------------------->> Rs.750")
    cu=int(input("\nEnter Cuisine Number: "))
    qn=int(input("Enter Quantity : "))
    if cu==1:
        pr=300
        print("SO YOU HAVE ORDERED VEGETARIAN COMBO")
    if cu==2:
        pr=500
        print("SO YOU HAVE ORDERED NON- VEGETARIAN COMBO")
    if cu==3:
        pr=750
        print("SO YOU HAVE ORDERED VEGETARIAN AND NON-VEGETARIAN COMBO")
    tt=qn*pr
    print("YOUR TOTAL BILL AMOUNT IS ------ Rs. ",tt)
    print("ENJOY YOUR MEAL!!! \n")

def game():
    print("\n\t THE GAMES")
    print("\t---------------------------------------\n")
    print("1. Table Tennis -------------------->>150 Rs/Hr")
    print("2. Bowling-------------------------->>100 Rs/Hr")
    print("3. Swimming Pool Games------------->>350 Rs/Hr")
    print("4. Video Games--------------------->>300 Rs./Hr ")
    print("5. Snooker-------------------------->>250 Rs./Hr")
    wg=int(input("\nEnter Your Game choice: "))
    tm=int(input("Enter No. of Hours You want To Play: "))
    if wg==1:
        pr=150
        print("YOU HAVE DECIDED TO PLAY: TABLE TENNIS")
    if wg==2:
        pr=100
        print("YOU HAVE DECIDED TO PLAY: BOWLING")
    if wg==3:
        pr=350
        print("YOU HAVE DECIDED TO PLAY: SWIMMING POOL GAMES")
    if wg==4:
        pr=150
        print("YOU HAVE DECIDED TO PLAY: VIDEO GAMES")
    if wg==5:
        pr=150
        print("YOU HAVE DECIDED TO PLAY: SNOOKER")
    tt=pr*tm
    print("\n YOUR TOTAL GAMING BILL IS : Rs.",tt,"FOR",tm,"HOURS")
    print("WE HOPE YOU WILL ENJOY YOUR GAME!!\n")

def details():
    f=open('Hotel.dat','rb')
    rec=pickle.load(f)
    print("\nId \t Name\t Address Age ")
    print("------------------------------------------------------------------------------------")
    for i in rec:
        print(" ",i[0],'  ',i[1],'    ',i[2],'   ',i[3],'  ',i[4],'     ',i[5],'     ',i[6],'\n')
    f.close()
def search():
        n=int(input("enter Customer ID:"))
        if os.path.isfile("Hotel.dat"):
            found=0
            f=open("Hotel.dat",'rb')
            rec=pickle.load(f)
            for i in rec:
                if i[0]==n:
                    print("\n ID \t     Name\t    Address   Age\t     Country\t   Phone number\t  Email")
                    print("------------------------------------------------------------------------------")
                    print(" ",i[0],'  ',i[1],'    ',i[2],'   ',i[3],'  ',i[4],'     ',i[5],'     ',i[6],'\n')
                    found=1
            f.close()
            if found==0:
                print("Record Not Found")

def update():
    if os.path.isfile("Hotel.dat"):
        n=int(input("Enter Customer ID: "))
        found=0
        f=open("Hotel.dat",'rb')
        rec=pickle.load(f)
        for i in rec:
            if i[0]==n:
                print("\n ID \t     Name\t    Address   Age\t     Country\t   Phone number\t  Email")
                print("------------------------------------------------------------------------------")
                print(" ",i[0],'  ',i[1],'    ',i[2],'   ',i[3],'  ',i[4],'     ',i[5],'     ',i[6],'\n')
                found=1
                newnm=input('Enter New Name :')
                newad=input('Enter New Address :')
                newag=input('Enter New Age :')
                newcn=input('Enter New Country :')
                newpn=input('Enter New Phone No. :')
                newem=input('Enter New  Email :')
                print("\nRECORD UPDATED! \n")
                newdata=[n,newnm,newad,newag,newcn,newpn,newem]
                rec[n-1]=newdata
                f=open("Hotel.dat",'wb')
                pickle.dump(rec,f)
                f.close()
            f.close()

while True:
    print("\t\t HOTEL MANAGEMENT SYSTEM")
    print("\t\t****************")
    print("\t1-->.Enter Customer Details\n\t2-->.Booking Record ")
    print("\t3-->.Calculate Rooms Rent\n\t4-->.Calculate Resturant Bill ")
    print("\t5-->.calculate Game Bill\n\t6-->.Display Customer Details ")
    print("\t7-->.Search Record ")
    print("\t8-->.Update Record \n\t9-->.Exit")
    n=int(input("\nEnter Your Options: "))
    if n==1:
        new()
    elif n==2:
        book()
    elif n==3:
        room()
    elif n==4:
        resturant()
    elif n==5:
        game()
    elif n==6:
        details()
    elif n==7:
        search()
    elif n==8:
        update()
    elif n==9:
        exit(None)
    else:
        print("Wrong Choice")
                
        






    

    




    



