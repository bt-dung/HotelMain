import mysql.connector
from mysql.connector import Error
from database.dbHandle import DatabaseHandler
import hashlib
import database.query as query

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, address, gender, phone, password, role):
    mydb = mysql.connector.connect(host = "localhost",user="root",database = "hoteldb")

    myCursor = mydb.cursor()
    if mydb:
        query = """
        INSERT INTO Users (Name, Email, Address, Gender, PhoneNumber, PasswordHash, Role)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            myCursor.execute(query, (name, email, address, gender, phone, hash_password(password), role))
            mydb.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            myCursor.close()
            mydb.close()

def authenticate_user(email, password):
    mydb = DatabaseHandler(host="localhost", user="root", database="hoteldb")
    mydb.connect()
    
    user = mydb.fetch_one(query.GET_USER_BY_EMAIL, (email,))
    print(user)
    mydb.close()
    if user:
        stored_password_hash = user[7]
        user_role = user[6]
        if hash_password(password) == stored_password_hash:
            return {"status": True, "role": user_role}
        else:
            return {"status": False, "role": None}
    else:
        return {"status": False, "role": None}
        
def login_user(email, password):
    return authenticate_user(email, password)
