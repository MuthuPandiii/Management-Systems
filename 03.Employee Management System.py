from curses import curs_set
from sqlite3 import Cursor
import mysql.connector as db

database = db.connect(
                host = "localhost",
                user = "root",
                passwd="g2l3b5@2002M",
                database="Employee_DataBase"
                    )


def Check_Employee(emp_id):
    cursor  = database.cursor()
    
    command="Select * from EMPLOYEE WHERE EMPLOYEE_ID =  %s"
    
    data = (emp_id,)
    
    cursor.execute(command,data)
    
    r=cursor.fetchall()
    
    if len(r)>=1:
        return -1
    else:
        return 1
    

def Add_Employee(emp_id):
    r=Check_Employee(emp_id)
    
    if r==-1:
        print("\n\tThe Employee ID already exists")
        Home()
    
    else:
        Emp_ID = emp_id
        Name   = input("Enter the Name of the Employee")
        Post   = input("Enter the Post of the Employee")
        Salary = input("Enter the Salary of the Employee")
        data = (Emp_ID,Name,Post,Salary)
        
        cursor = database.cursor()

        command = "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s)"

        cursor.execute(command,data)

        database.commit()

        print("\n\tEmployee Details Added Successfully✅")

        Home()

def Remove_Employee():
    print("\nEnter the Employee ID")
    emp_id=input()

    result=Check_Employee(emp_id)

    if  result==1:
        print("\n\tThe given Employee does not exist")
        Home()
    else:
        cursor = database.cursor()

        command="DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID=%s"

        data = (emp_id,)

        cursor.execute = (command,data)
    
def Home():
    
    print("\n\t\tEmployee DataBase")
    print("\t\t<---------------->")
    print("\n\t1.Add Employee")
    print("\t2.Remove Employee")
    print("\t3.Update Details")
    print("\t4.Exit")
        
    choice = int(input("Enter your choice"))
    
    if choice==1:
        print("\nEnter the Employee Id ")
        print("\nThe Employee Id is the Employee's Date of Birth without special characters")
        emp_id = input()
        Add_Employee(emp_id)
        
    
    if choice==2:
        pass
    
    if choice==3:
        pass
    
    if choice==4:
        print("\nExiting")
        exit()

Home()