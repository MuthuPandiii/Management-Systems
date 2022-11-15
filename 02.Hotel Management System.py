import datetime,random
from operator import le

data = {}

def Home():
    
    print("\n\tWelcome to Hotel Python.How can we help you??")
    
    while True:
        print("\n\t\tHotel Management System")
        print("\t\t<======================>")
        print('''
                    1.Booking
                    2.Room Info
                    3.Record
                    4.Exit
               ''')
        choice=input("Enter the option : [1/2/3/4]:")
        
        while choice not in ["1","2","3","4","5"]:
            
            print("\n\tOOPs..It Seems like you entered the  option wrongly")
            choice=int(input("Enter the option : [1/2/3/4]:"))
            
        if choice=="1":
            Booking()
            
        if choice=="2":
            Room_Info()
            
        if choice=="3":
            Record()
            
        if choice=="4":
            print("\n\tThanks for visitig Hotel PYTHON")
            print("\n\tExiting....")
            break

def date():

    cin=input("\nEnter the Checkin  Date [dd/mm/yyyy]: ")
    cout=input("\nEnter the Checkout Date[dd/mm/yyyy] : ")
    
    try:
        cin  = datetime.datetime.strptime(cin,'%d/%m/%Y')
        cout = datetime.datetime.strptime(cout,'%d/%m/%Y')

    except ValueError:
        print("\n\tPlease enter the date in the given Format [dd/mm/yyyy] : ")
        date()

    if cin>=cout:
        print("\nLoL..Are  you  time travelling😜....The Checkin  Date must be less than Checkout Date")
        print("Please re-enter the dates.")
        date()

    days=cout-cin

    return cin,cout,days


def Booking():

    print("\nEnter Your name : ")
    name=input()
    print("\nEnter  your phone number : ")
    phn=input()
    print("\nEnter your Address")
    address=input()

    for i in range(len(data)):
        if phn in  list(data.values())[i]:
            print("\nThe given phone  number belongs to another person.")
            print("\nKindly refill again")
            Booking()
    
    checkin,checkout,days_stayed=date()

    checkin=str(checkin).split(" ")[0]
    checkout=str(checkout).split(" ")[0]

    days_stayed=str(days_stayed).split(",")[0]

    customer_id=''.join(random.choice('0123456789ABCDEF') for i in range(7))

    for i in range(len(data)):
        if customer_id in list(data.values())[i]:
            customer_id=''.join(random.choice('0123456789ABCDEF') for i in range(7))

    print("\n\tDetails Entered:")
    print("\t-----------------")
    print('''
                1.Name         : {}
                2.Phone Number : {}
                3.Address      : {}
                4.Checkin      : {}
                5.Checkout     : {}
                6.Days Stayed  : {}
                7.Customer ID  : {}
    '''.format(name,phn,address,checkin,checkout,days_stayed,customer_id))

    rooms=["Standard Non-AC ","Standard AC","3-Bed Non-AC","3-Bed AC "]

    print("\n\t----SELECT ROOM TYPE----")
    print("\t1. Standard Non-AC  -- Rs.3000")
    print("\t2. Standard AC      -- Rs.3500")
    print("\t3. 3-Bed Non-AC     -- Rs.4000")
    print("\t4. 3-Bed AC         -- Rs.4500")

    room=int(input())

    while room not in [1,2,3,4]:
        print("\nNo rooms exist  for the given input")
        print("Please enter  from the option [1/2/3/4] : ")
        room=int(input())

    price=0
    no_of_days= int(days_stayed.split(" ")[0])

    if room==1:
        price+=3000 * no_of_days
    elif room==2:
        price+=3500 * no_of_days
    elif room==3:
        price+=4000 * no_of_days
    else:
        price+=4500 * no_of_days

    print(f"\n\tAre you sure you want to book {rooms[room-1]} for {price} rupees")
    wish=input("[Y/N]")

    while wish not in ["Y","y","N","n"]:
        print("\n\tPlease enter Y/N.")
        wish=input("[Y/N]")


    if wish=="Y" or  wish=="y":

        room_no=random.randrange(200)

        for i  in range(len(data)):
            if room_no in list(data.values())[i]:
                room_no=random.randrange(200)

        data[customer_id]=[name,phn,address,checkin,checkout,days_stayed,room_no,price,"not_paid"]

        print("\n\tThanks for confirmation...Room Booking Successful...Please make the Payment to confirm the Room.")

        Payment()


    elif wish=="N" or wish=="n":
        print("\nReturn to Home Screen -- Press 1")
        print("\nTo Exit               -- Press 0")
        choice=int(input())


        while choice not in [0,1]:
            print("\nOOPS it seems to be a wrong choice...please enter 0  or 1.")
            choice=int(input())
            
        if choice==1:
           Home()
            
        if  choice==0:
          exit()
    
            
# Taken from Geek for Geeks
def Room_Info():
    print("\n\t---------------------------------")
    print("\t------- HOTEL ROOMS INFO -------")
    print("\t--------------------------------")
    print("\n(1)STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("(2)STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("(3)3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("(4)3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    
    i=1
    while i!=0:
        print("\n\n\t\tPress 0 for back to Home")
        i=int(input())
        if i==0:
            break
    Home()
    exit()

def Payment():

    print("\n\tPlease enter your customer ID :  ")
    id=input()

    b=None

    if id in list(data.keys()):
        b=id
    
    if b==None:
        print("\nThe given Customer id  doesn't exist.....")
        Payment()
        exit()


    try:
        print(f"\nEnter the  cash amount of Rupees {data[b][7]}")
        cash=int(input())

    except ValueError:
        print("\nEnter a valid Cash Amount")
        Payment()
        exit()

    #data[customer_id]=[name,phn,address,checkin,checkout,days_stayed,room_no,price,"not_paid"]

    if cash==data[b][7]:
        pass
    
    elif cash > data[b][7]:
        print("\nHere is the Remaining Balance")
        print(f"\n\t Rupees : {cash - data[b][7]}")

    elif cash<  data[b][7]:
        print("\nInsufficient Cash...")
        Payment()
        exit()
    
    print("\n\tRoom Confirmation Successful.")
        
    data[b][8]="Paid"

    Home()

def Record():

    print("\n\tPlease enter your customer ID :  ")
    id=input()

    b=None

    if id in list(data.keys()):
        b=id

    if b==None:
        print("\nThe given Customer id  doesn't exist.....")
        Home()
        exit()
    
    #data[customer_id]=[name,phn,address,checkin,checkout,days_stayed,room_no,price,"not_paid"]
    
    print("\n\tThe  Record::")
    print("\t==============")
    print('''
            1) Name            : {}
            2) Phone Number    : {}
            3) Address         : {}
            4) CheckIn         : {}
            5) CheckOut        : {}
            6) Days Stayed     : {}
            7) Room Number     : {}
            8) Prize           : {}
            9) Payment  Status : {}
    '''.format(data[b][0],data[b][1],data[b][2],data[b][3],data[b][4],data[b][5],data[b][6],data[b][7],data[b][8]))

    i=1
    while i!=0:
        print("\n\n\t\tPress 0 for back to Home")
        i=int(input())
        if i==0:
            break
    Home()
    exit()

Home()