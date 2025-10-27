import mysql.connector

# Connect to MySQL (adjust user/password/database)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hospital_db"
)
cursor = conn.cursor()

# Create Tables

cursor.execute("""
CREATE TABLE Employee (
    E_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Sex VARCHAR(10),
    Salary DECIMAL(10,2),
    Mob_No VARCHAR(15),
    Address VARCHAR(255),
    State VARCHAR(50),
    City VARCHAR(50),
    Pin_no VARCHAR(10)
);
""")

cursor.execute("""
CREATE TABLE Doctor (
    D_ID INT PRIMARY KEY AUTO_INCREMENT,
    E_ID INT,
    Dept VARCHAR(100),
    Qualification VARCHAR(100),
    FOREIGN KEY (E_ID) REFERENCES Employee(E_ID)
);
""")

cursor.execute("""
CREATE TABLE Nurse (
    N_ID INT PRIMARY KEY AUTO_INCREMENT,
    E_ID INT,
    Qualification VARCHAR(100),
    Dept VARCHAR(100),
    FOREIGN KEY (E_ID) REFERENCES Employee(E_ID)
);
""")

cursor.execute("""
CREATE TABLE Receptionist (
    RCP_ID INT PRIMARY KEY AUTO_INCREMENT,
    E_ID INT,
    FOREIGN KEY (E_ID) REFERENCES Employee(E_ID)
);
""")

cursor.execute("""
CREATE TABLE Patient (
    P_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Age INT,
    DOB DATE,
    Mob_No VARCHAR(15)
);
""")

cursor.execute("""
CREATE TABLE Rooms (
    R_ID INT PRIMARY KEY AUTO_INCREMENT,
    Type VARCHAR(50),
    Capacity INT,
    Availability BOOLEAN
);
""")

cursor.execute("""
CREATE TABLE Bills (
    B_ID INT PRIMARY KEY AUTO_INCREMENT,
    P_ID INT,
    Amount DECIMAL(10,2),
    FOREIGN KEY (P_ID) REFERENCES Patient(P_ID)
);
""")

cursor.execute("""
CREATE TABLE Test_Report (
    T_ID INT PRIMARY KEY AUTO_INCREMENT,
    P_ID INT,
    Test_Type VARCHAR(100),
    Result VARCHAR(255),
    FOREIGN KEY (P_ID) REFERENCES Patient(P_ID)
);
""")

cursor.execute("""
CREATE TABLE Records (
    Record_no INT PRIMARY KEY AUTO_INCREMENT,
    App_no INT,
    RCP_ID INT,
    FOREIGN KEY (RCP_ID) REFERENCES Receptionist(RCP_ID)
);
""")

# Relationship tables
cursor.execute("""
CREATE TABLE Consults (
    P_ID INT,
    D_ID INT,
    PRIMARY KEY (P_ID, D_ID),
    FOREIGN KEY (P_ID) REFERENCES Patient(P_ID),
    FOREIGN KEY (D_ID) REFERENCES Doctor(D_ID)
);
""")

cursor.execute("""
CREATE TABLE Assigned (
    P_ID INT,
    R_ID INT,
    PRIMARY KEY (P_ID, R_ID),
    FOREIGN KEY (P_ID) REFERENCES Patient(P_ID),
    FOREIGN KEY (R_ID) REFERENCES Rooms(R_ID)
);
""")

cursor.execute("""
CREATE TABLE Governs (
    N_ID INT,
    R_ID INT,
    PRIMARY KEY (N_ID, R_ID),
    FOREIGN KEY (N_ID) REFERENCES Nurse(N_ID),
    FOREIGN KEY (R_ID) REFERENCES Rooms(R_ID)
);
""")

cursor.execute("""
CREATE TABLE Maintains (
    RCP_ID INT,
    Record_no INT,
    PRIMARY KEY (RCP_ID, Record_no),
    FOREIGN KEY (RCP_ID) REFERENCES Receptionist(RCP_ID),
    FOREIGN KEY (Record_no) REFERENCES Records(Record_no)
);
""")

conn.commit()
print("✅ All tables created successfully!")

cursor.close()
conn.close()
