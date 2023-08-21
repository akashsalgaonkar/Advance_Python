#Project which connects python to mysql database.......................

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Enter mysql database password",database="commands")

#initialize a cursor to perform queries.....................................
mycursor=con.cursor()

#To perform sql queries/cured operations on given database.....................

#1. Insert New Record in database.....................
def insert():
    q="select * from employee"
    mycursor.execute(q);
    data=mycursor.fetchall()
    #print(data)
    print("Employee_id  Employee_Name  Employee_Salary  Employee_Location")
    #print()
    for x in data:
        print(x[0],"         ",x[1],"         ",x[2],"        ",x[3])
    eid=int(input("Enter Employee I'd:"))
    ename=input("Enter Employee Name:")
    esal=int(input("Enter Employee Salary:"))
    eloc=input("Enter Employee Location:")
    q="insert into employee values({0},'{1}',{2},'{3}')".format(eid,ename,esal,eloc);
    mycursor.execute(q)
    con.commit()
    print("New Record Inserted Successfully.....")
    
#2. Delete the record from database..............................
def delete():
    q="select * from employee"
    mycursor.execute(q);
    data=mycursor.fetchall()
    #print(data)
    print("Employee_id  Employee_Name  Employee_Salary  Employee_Location")
    #print()
    for x in data:
        print(x[0],"         ",x[1],"         ",x[2],"        ",x[3])

    eid=int(input("Enter id to delete the record permanantly:"))
    q="delete from employee where eid={0}".format(eid)
    mycursor.execute(q)
    con.commit()
    print("Record deleted successfully.!!!")
    
#3. Update a specific record to be updated........................
def update():
    q="select * from employee"
    mycursor.execute(q);
    data=mycursor.fetchall()
    #print(data)
    print("Employee_id  Employee_Name  Employee_Salary  Employee_Location")
    #print()
    for x in data:
        print(x[0],"         ",x[1],"         ",x[2],"        ",x[3])
        
    eid=int(input("Enter Employee Id:"))
    q="select * from employee where eid={0}".format(eid)
    mycursor.execute(q)
    data=mycursor.fetchall()
    print(data)
    #Enter or leave empty record.........................
    ename=input("Enter Name / Else leave empty:")
    if(ename==" "):
        ename=data[0][1]
    esalary=input("Enter Salary / Else enter 0:")
    if(esalary==0):
        ename=data[0][2]
    eloc=input("Enter Location / Else leave empty:")
    if(eloc==" "):
        ename=data[0][3]
        
    q="update employee set ename='{0}',esalary={1}, eloc='{2}' where e_id={3}".format(ename,esalary,eloc,eid)
    con.commit()
    print("New Record Updated...")
    
#4. Display all records from database.....................
def display():
    q="select * from employee"
    mycursor.execute(q);
    data=mycursor.fetchall()
    #print(data)
    print("Employee_id  Employee_Name  Employee_Salary  Employee_Location")
    #print()
    for x in data:
        print(x[0],"         ",x[1],"         ",x[2],"        ",x[3])
    
#5. Display a specific record from database.......................
def display_id():
    eid=int(input("Enter i'd to retrive record:"))
    q="select * from employee where eid={0}".format(eid);
    mycursor.execute(q)
    data = mycursor.fetchall()
  
    for x in data:
        print(x)
    
n=1
while(n!=0):
    print("1.Insert new data\n2.Delete data using i'd\n3.Update data using i'd\n4.Display Record\n5.Display using i'd\n6.Exit")
    n=int(input("Enter your choice:"))
    if(n==1):
        insert()
    elif(n==2):
        delete()
    elif(n==3):
        update()
    elif(n==4):
        display()
    elif(n==5):
        display_id()
    else:
        n=0;
        
else:
    print("-----------VISIT AGAIN--------------")
