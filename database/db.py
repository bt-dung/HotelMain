import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user="root",database = "hoteldb")

myCursor = mydb.cursor()
create_users_table = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Address VARCHAR(255),
    Gender ENUM('Male', 'Female', 'Other'),
    PhoneNumber VARCHAR(20),
    PasswordHash VARCHAR(64) NOT NULL,
    Role ENUM('user', 'admin') NOT NULL
);
"""

# Câu lệnh SQL để tạo bảng Hotel
create_hotel_table = """
CREATE TABLE IF NOT EXISTS Hotel (
    HotelID INT AUTO_INCREMENT PRIMARY KEY,
    HotelName VARCHAR(100) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Rating TINYINT CHECK (Rating BETWEEN 1 AND 5),
    Description TEXT
);
"""

# Câu lệnh SQL để tạo bảng Room
create_room_table = """
CREATE TABLE IF NOT EXISTS Room (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,
    HotelID INT,
    RoomType ENUM('Single', 'Double', 'Suite') NOT NULL,
    PricePerNight DECIMAL(10, 2) NOT NULL,
    Availability BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID)
);
"""

# Câu lệnh SQL để tạo bảng Booking
create_booking_table = """
CREATE TABLE IF NOT EXISTS Booking (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    RoomID INT,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    BookingDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);
"""
tables = [create_users_table, create_hotel_table, create_room_table, create_booking_table]

for table in tables:
    try:
        myCursor.execute(table)
        print("Table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Đóng kết nối
mydb.close()