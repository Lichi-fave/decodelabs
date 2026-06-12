import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

#connect to azure mysql
def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT')),
        ssl={'ca':r'C:\Users\oluchi\Downloads\DigiCertGlobalRootG2.crt.pem'} #path to ssl certificate
    )
    
# create the table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Interns (
                       InternID INT PRIMARY KEY AUTO_INCREMENT,
                       FirstName VARCHAR(100) NOT NULL,
                       LastName VARCHAR(100) NOT NULL,
                       Role VARCHAR(100) NOT NULL,
                       Email VARCHAR(100) NOT NULL UNIQUE
                       )
                       """)
    cursor.execute("TRUNCATE TABLE Interns;")
    conn.commit()
    print("Table created successfully")
    cursor.close()
    conn.close()
    
# insert dummy records
def insert_records():
    conn = get_connection()
    cursor = conn.cursor()
    
    interns = [
        ('John', 'Abunwa', 'Backend Developer', 'jabunwa@decodelabs.com'),
        ('Jane', 'Love', 'Cloud Engineer', 'jlove@decodelabs.com'),
        ('Conan', 'Johnson', 'DevOps Intern', 'conjohnson@decodelabs.com'),
    ]
    
    cursor.executemany("""
                       INSERT IGNORE INTO Interns (FirstName, LastName, Role, Email)
                       VALUES (%s, %s, %s, %s)
                       """, interns)
    
    conn.commit()
    print(f"{cursor.rowcount} records inserted")
    cursor.close()
    conn.close()
    
# read and display all records
def read_records():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Interns")
    rows = cursor.fetchall()
    
    print("\n Interns Table:")
    print(f"{'ID':<3} {'FirstName':<20} {'LastName':<20} {'Role':<25} {'Email':<30}")
    print("-" * 80)
    for row in rows:
        print(f"{row[0]:<3} {row[1]:<20} {row[2]:<20} {row[3]:<25} {row[4]:<30}")
        
    cursor.close()
    conn.close()
    
if __name__=="__main__":
    print("Connecting to Azure MySQL...")
    create_table()
    insert_records()
    read_records()
    print("\n Project 3 complete")

                       
                   