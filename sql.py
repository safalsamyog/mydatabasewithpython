import sqlite3
conn=sqlite3.connect("safal.db")
cursor=conn.cursor()
#adding query
#cursor.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT ,email TEXT)")
def see_one(id_):
    #for viewing only one id
    cursor.execute("SELECT*FROM Users")
    users=cursor.fetchall()
    return users[id_-1]
   


loop=True
a=0
while loop:
    try:
        dd=int(input("enter 1 for inputing data and 2 for seeing,3 for deleting data ,4 for uptading,5 for seeing one id data,6 for exit... : "))
        if dd==1:
            a=int(input("enter the id number: "))
            
            b=input("enter the name: ")
            c=input("enter the email: ")
            cursor.execute("INSERT INTO Users (id,name,email) values(?,?,?)",(a,b,c))
           
        elif dd==2:
            cursor.execute("SELECT*FROM Users")
            users=cursor.fetchall()
            for row in users:
                print(list(row))
        elif dd==3:
            e=int(input("enter id for deleting: "))
            cursor.execute("DELETE FROM Users WHERE id=%s"%e)
            print("successfully deleted...")
        elif dd==4:
             a=int(input("enter the id number: "))
             b=input("enter the name: type N for not uptading ")
             c=input("enter the email type N for not uptading: ")
             if b=="N":
                 print("ok we are not upatding name......")
             else:
                 cursor.execute("UPDATE Users SET name = ? WHERE id = ?",(b,a))
             if c=="N":
                 print("ok we are not upatding email ...") 
             else:
                 cursor.execute("UPDATE Users SET email = ? WHERE id = ?",(c,a))
             cursor.execute("SELECT*FROM Users")
             users=cursor.fetchall()
             for row in users:
                 print(list(row))
            #  cursor.execute(sql_update_query, data)
        elif dd==5:
            try:
                _ss=int(input("Enter id name to see data: "))
                ss=see_one(_ss)
                print(list(ss))
            except:
                print("sorry! there is no such value")

        elif dd==6:
            loop=False
            
            

    except:
        print("error find out!! id is alredy there...Try unique data and id")
        cursor.execute("SELECT*FROM Users")
        # users=cursor.fetchall()
        # for row in users:
        #     print("here is upataded data",list(row))

conn.commit()

conn.close()

#cursor.execute("INSERT INTO Users VALUES(1,'safal','safal@gmail.com')")
# a=3
# b="safal"
# c="dd"
# cursor.execute("INSERT INTO Users (id,name,email) values(?,?,?)",(a,b,c))
# conn.commit()
# conn.close()