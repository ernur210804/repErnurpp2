import psycopg2 
import csv

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='210804Ernur'
)

cursor = conn.cursor()

#POSTGRESQL КОД ДЛЯ ПАЙТОНА
sql_insert= '''
INSERT INTO phonebook VALUES(%s,%s,%s,%s);
'''

sql_delete_firstname='''
DELETE FROM phonebook WHERE firstname=%s; 
'''

sql_delete_lastname='''
DELETE FROM phonebook WHERE lastname=%s;'''

sql_delete_phone='''
DELETE FROM phonebook WHERE phone=%s;'''

sql_delete_email='''
DELETE FROM phonebook WHERE email=%s;'''

sql_delete_id='''
DELETE FROM phonebook WHERE id=%s;'''

sql_delete_all='''
TRUNCATE TABLE phonebook;
'''

sql_update_lastname='''
UPDATE phonebook SET lastname=%s WHERE id=%s;
'''

sql_update_firstname='''
UPDATE phonebook SET firstname=%s WHERE id=%s;
'''

sql_update_phone='''
UPDATE phonebook SET phone=%s WHERE id=%s;
'''

sql_update_email='''
UPDATE phonebook SET email=%s WHERE id=%s;
'''
sql_query_all='''
SELECT * FROM phonebook;
'''

sql_query_lastname='''
SELECT * FROM phonebook WHERE lastname=%s ;
'''

sql_query_firstname='''
SELECT * FROM phonebook WHERE firstname=%s ;
'''

sql_query_phone='''
SELECT * FROM phonebook WHERE phone=%s ;
'''

sql_query_email='''
SELECT * FROM phonebook WHERE email=%s ;
'''

# FUNCTIONS FOR CHANGING TABLE
def upload_data_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            firstname, lastname, email, phone = row
            cursor.execute(
                "INSERT INTO PhoneBook (firstname, lastname, email, phone) VALUES (%s, %s, %s, %s)",
                (firstname, lastname, email, phone,)
            )
        conn.commit()
        print("Data uploaded successfully from", filename)


def insert_data_from_console():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    cursor.execute(
        "INSERT INTO PhoneBook (firstname, lastname, phone, email) VALUES (%s, %s, %s, %s)",
        (firstname, lastname, phone, email)
    )
    conn.commit()
    print("Data inserted successfully")


def update():
    print('WHAT YOU WANT TO UPDATE?')
    choice = int(input('1-lastname,2-firstname,3-email,4-phone \n'))
    bool =True
    if choice==1:
        id=input('enter id:')
        lastname=input('enter lastname: ')
        cursor.execute(sql_update_lastname,(lastname,id,))
    elif choice==2:
        id=input('enter id:')
        firstname=input("enter firstname: ")
        cursor.execute(sql_update_firstname,(firstname,id,))
    elif choice==3:
        id=input('enter id:')
        email=input('enter email: ')
        cursor.execute(sql_update_email,(email,id,))
    elif choice==4:
        id=input('enter id:')
        phone=input('enter phone: ')
        cursor.execute(sql_update_phone,(phone,id,))
    else:
        print('ERROR')
        bool=False
    conn.commit()
    if bool==True:
        print("Data updated successfully!")


def delete():
    print("WHAT YOU WANT TO DELETE?")
    choice1 = int(input('1-firstname,2-lastname,3-email,4-phone,5-all,6-id \n'))
    bool=True
    if choice1==1:
        firstname=input("enter firstname:")
        cursor.execute(sql_delete_firstname,(firstname,))
        
    elif choice1==2:
        lastname=input("enter lastname:")
        cursor.execute(sql_delete_lastname,(lastname,))
        
    elif choice1==3:
        email=input("enter email:")
        cursor.execute(sql_delete_email(),(email,))
        
    elif choice1==4:
        phone=input("enter phone:")
        cursor.execute(sql_delete_phone,(phone,))
    elif choice1==5:
        cursor.execute(sql_delete_all)
    
    elif choice1==6:
        id=input('enter id: ')
        cursor.execute(sql_delete_id,(id,))
    else:
        print('ERROR')
        bool=False
    conn.commit()
    if bool==True:
        print(" Data deleated successfully! ")
    
def query():
    print('WHAT YOU WANT TO QUERY?')
    choice2 = int(input('1-lastname,2-firstname,3-email,4-phone,5-all \n'))
    if choice2==1:
        lastname=input("enter lastname: ")
        cursor.execute(sql_query_lastname,(lastname,))
        print(cursor.fetchall())
    elif choice2==2:
        firstname=input("enter firstname: ")
        cursor.execute(sql_query_firstname,(firstname,))
        print(cursor.fetchall())
    elif choice2==3:
        email=input('enter email: ')
        cursor.execute(sql_query_email,(email,))
        print(cursor.fetchall())
    elif choice2==4:
        phone= input('enter phone: ')
        cursor.execute(sql_query_phone,(phone,))
        print(cursor.fetchall())
    elif choice2==5:
        cursor.execute(sql_query_all)
        print(cursor.fetchall())
    else:
        print('ERROR')
    conn.commit()
            

def main():
    print("WHAT YOU WANT TO DO?")
    action = int(input('1-insert data , 2-delete data , 3-update data , 4-query data ,5-insert csv\n'))
    if action==1:
        insert_data_from_console()
    elif action==2:
        delete()
    elif action==3:
        update()
    elif action==4:
        query()
    elif action==5:
        upload_data_from_csv("phonebook_data.csv")
    else:
        print('ERROR')

main()

cursor.close()
conn.close()
            
    