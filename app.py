import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # change this
    database="hospitaldb"
)
cursor = conn.cursor()

# Function to insert patient details
def insert_patient(name, gender, age, dob, mob_no):
    try:
        query = """
        INSERT INTO Patient (Name, Gender, Age, DOB, Mob_No)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, gender, age, dob, mob_no)
        cursor.execute(query, values)
        conn.commit()
        print(f"✅ Patient '{name}' inserted successfully with ID {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
def insert_employee(name,sex,salary,mob_no,address,state,city,pin_no):
    try:
        query= """
        insert into Employee(name, sex, salary, mob_no, address, state, city, pin_no)
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (name,sex,salary,mob_no,address,state,city,pin_no)
        cursor.execute(query,values)
        conn.commit()
        print(f"employee '{name}' inserted sucessfully with id {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("error:",err)

def insert_nurse(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept):
    try:
        # First insert into Employee table
        employee_query = """
        INSERT INTO Employee (Name, Sex, Salary, Mob_No, Address, State, City, Pin_no)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        employee_values = (name, sex, salary, mob_no, address, state, city, pin_no)
        cursor.execute(employee_query, employee_values)
        employee_id = cursor.lastrowid
        
        # Then insert into Nurse table
        nurse_query = """
        INSERT INTO Nurse (E_ID, Qualification, Dept)
        VALUES (%s, %s, %s)
        """
        nurse_values = (employee_id, qualification, dept)
        cursor.execute(nurse_query, nurse_values)
        conn.commit()
        print(f"✅ Nurse '{name}' inserted successfully with Employee ID {employee_id}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

def insert_doctor(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept):
    try:
        # First insert into Employee table
        employee_query = """
        INSERT INTO Employee (Name, Sex, Salary, Mob_No, Address, State, City, Pin_no)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        employee_values = (name, sex, salary, mob_no, address, state, city, pin_no)
        cursor.execute(employee_query, employee_values)
        employee_id = cursor.lastrowid
        
        # Then insert into Doctor table
        doctor_query = """
        INSERT INTO Doctor (E_ID, Dept, Qualification)
        VALUES (%s, %s, %s)
        """
        doctor_values = (employee_id, dept, qualification)
        cursor.execute(doctor_query, doctor_values)
        conn.commit()
        print(f"✅ Doctor '{name}' inserted successfully with Employee ID {employee_id}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

def insert_receptionist(name, sex, salary, mob_no, address, state, city, pin_no):
    try:
        # First insert into Employee table
        employee_query = """
        INSERT INTO Employee (Name, Sex, Salary, Mob_No, Address, State, City, Pin_no)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        employee_values = (name, sex, salary, mob_no, address, state, city, pin_no)
        cursor.execute(employee_query, employee_values)
        employee_id = cursor.lastrowid
        
        # Then insert into Receptionist table
        receptionist_query = """
        INSERT INTO Receptionist (E_ID)
        VALUES (%s)
        """
        cursor.execute(receptionist_query, (employee_id,))
        conn.commit()
        print(f"✅ Receptionist '{name}' inserted successfully with Employee ID {employee_id}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Room Management Functions
def insert_room(room_type, capacity):
    try:
        query = """
        INSERT INTO Rooms (Type, Capacity, Availability)
        VALUES (%s, %s, %s)
        """
        values = (room_type, capacity, True)  # Available by default
        cursor.execute(query, values)
        conn.commit()
        print(f"✅ Room of type '{room_type}' with capacity {capacity} inserted successfully with ID {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

def assign_patient_to_room(patient_id, room_id):
    try:
        # Check if room is available
        check_query = "SELECT Availability FROM Rooms WHERE R_ID = %s"
        cursor.execute(check_query, (room_id,))
        result = cursor.fetchone()
        
        if not result:
            print("❌ Room not found!")
            return
        if not result[0]:
            print("❌ Room is not available!")
            return
            
        # Insert into Assigned table
        assign_query = """
        INSERT INTO Assigned (P_ID, R_ID)
        VALUES (%s, %s)
        """
        cursor.execute(assign_query, (patient_id, room_id))
        
        # Update room availability
        update_query = "UPDATE Rooms SET Availability = FALSE WHERE R_ID = %s"
        cursor.execute(update_query, (room_id,))
        
        conn.commit()
        print(f"✅ Patient {patient_id} assigned to Room {room_id} successfully")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

def assign_nurse_to_room(nurse_id, room_id):
    try:
        query = """
        INSERT INTO Governs (N_ID, R_ID)
        VALUES (%s, %s)
        """
        cursor.execute(query, (nurse_id, room_id))
        conn.commit()
        print(f"✅ Nurse {nurse_id} assigned to govern Room {room_id} successfully")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Test Report Functions
def insert_test_report(patient_id, test_type, result):
    try:
        query = """
        INSERT INTO Test_Report (P_ID, Test_Type, Result)
        VALUES (%s, %s, %s)
        """
        values = (patient_id, test_type, result)
        cursor.execute(query, values)
        conn.commit()
        print(f"✅ Test report for Patient {patient_id} inserted successfully with ID {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Consult Functions
def create_consult(patient_id, doctor_id):
    try:
        query = """
        INSERT INTO Consults (P_ID, D_ID)
        VALUES (%s, %s)
        """
        cursor.execute(query, (patient_id, doctor_id))
        conn.commit()
        print(f"✅ Consult relationship created between Patient {patient_id} and Doctor {doctor_id}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Records Functions
def create_record(app_no, receptionist_id):
    try:
        # First create record
        record_query = """
        INSERT INTO Records (App_no)
        VALUES (%s)
        """
        cursor.execute(record_query, (app_no,))
        record_no = cursor.lastrowid
        
        # Then create maintains relationship
        maintains_query = """
        INSERT INTO Maintains (RCP_ID, Record_no)
        VALUES (%s, %s)
        """
        cursor.execute(maintains_query, (receptionist_id, record_no))
        
        conn.commit()
        print(f"✅ Record {record_no} created and maintained by Receptionist {receptionist_id}")
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Patient Search and Status Functions
def search_patient_by_phone(mob_no):
    try:
        # Get patient basic info
        patient_query = """
        SELECT P_ID, Name, Gender, Age, DOB, Mob_No
        FROM Patient 
        WHERE Mob_No = %s
        """
        cursor.execute(patient_query, (mob_no,))
        patient = cursor.fetchone()
        
        if not patient:
            print("❌ No patient found with this phone number!")
            return
            
        print(f"\n📋 PATIENT INFORMATION")
        print(f"Patient ID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"Gender: {patient[2]}")
        print(f"Age: {patient[3]}")
        print(f"DOB: {patient[4]}")
        print(f"Phone: {patient[5]}")
        
        # Check if patient is assigned to a room
        room_query = """
        SELECT r.R_ID, r.Type, r.Capacity, r.Availability
        FROM Rooms r
        JOIN Assigned a ON r.R_ID = a.R_ID
        WHERE a.P_ID = %s
        """
        cursor.execute(room_query, (patient[0],))
        room = cursor.fetchone()
        
        if room:
            print(f"\n🏥 ROOM ASSIGNMENT")
            print(f"Room ID: {room[0]}")
            print(f"Room Type: {room[1]}")
            print(f"Capacity: {room[2]}")
            print(f"Status: {'Available' if room[3] else 'Occupied'}")
        else:
            print(f"\n🏥 ROOM ASSIGNMENT: Not assigned to any room")
            
        # Check for assigned nurses
        nurse_query = """
        SELECT n.N_ID, e.Name, n.Qualification, n.Dept
        FROM Nurse n
        JOIN Employee e ON n.E_ID = e.E_ID
        JOIN Governs g ON n.N_ID = g.N_ID
        JOIN Assigned a ON g.R_ID = a.R_ID
        WHERE a.P_ID = %s
        """
        cursor.execute(nurse_query, (patient[0],))
        nurses = cursor.fetchall()
        
        if nurses:
            print(f"\n👩‍⚕️ ASSIGNED NURSES")
            for nurse in nurses:
                print(f"Nurse ID: {nurse[0]}, Name: {nurse[1]}, Qualification: {nurse[2]}, Department: {nurse[3]}")
        else:
            print(f"\n👩‍⚕️ ASSIGNED NURSES: No nurses assigned")
            
        # Check for consulting doctors
        doctor_query = """
        SELECT d.D_ID, e.Name, d.Qualification, d.Dept
        FROM Doctor d
        JOIN Employee e ON d.E_ID = e.E_ID
        JOIN Consults c ON d.D_ID = c.D_ID
        WHERE c.P_ID = %s
        """
        cursor.execute(doctor_query, (patient[0],))
        doctors = cursor.fetchall()
        
        if doctors:
            print(f"\n👨‍⚕️ CONSULTING DOCTORS")
            for doctor in doctors:
                print(f"Doctor ID: {doctor[0]}, Name: {doctor[1]}, Qualification: {doctor[2]}, Department: {doctor[3]}")
        else:
            print(f"\n👨‍⚕️ CONSULTING DOCTORS: No doctors assigned")
            
        # Check for test reports
        test_query = """
        SELECT T_ID, Test_Type, Result
        FROM Test_Report
        WHERE P_ID = %s
        ORDER BY T_ID DESC
        """
        cursor.execute(test_query, (patient[0],))
        tests = cursor.fetchall()
        
        if tests:
            print(f"\n🧪 TEST REPORTS")
            for test in tests:
                print(f"Test ID: {test[0]}, Type: {test[1]}, Result: {test[2]}")
        else:
            print(f"\n🧪 TEST REPORTS: No test reports found")
            
        # Check for bills
        bill_query = """
        SELECT B_ID, Amount
        FROM Bills
        WHERE P_ID = %s
        """
        cursor.execute(bill_query, (patient[0],))
        bills = cursor.fetchall()
        
        if bills:
            print(f"\n💰 BILLS")
            total_amount = 0
            for bill in bills:
                print(f"Bill ID: {bill[0]}, Amount: ${bill[1]}")
                total_amount += float(bill[1])
            print(f"Total Amount: ${total_amount}")
        else:
            print(f"\n💰 BILLS: No bills found")
            
    except mysql.connector.Error as err:
        print("❌ Error:", err)

# Menu-driven switch-case style
def menu():
    print("\n--- Hospital Management System ---")
    print("1. Employee Management")
    print("2. Patient Management")
    print("3. Room Management")
    print("4. Test Reports")
    print("5. Consult Management")
    print("6. Records Management")
    print("7. Search Patient Status")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:  # Employee Management
            print("\n--- Employee Management ---")
            print("1. Insert Nurse")
            print("2. Insert Doctor")
            print("3. Insert Receptionist")
            print("4. Back to main menu")

            sub_choice = int(input("Enter your choice: "))

            match sub_choice:
                case 1:  # Insert Nurse
                    print("\n--- Insert Nurse ---")
                    name = input("Enter nurse name: ")
                    sex = input("Enter gender: ")
                    salary = int(input("Enter salary: "))
                    mob_no = input("Enter mobile no.: ")
                    address = input("Enter address: ")
                    state = input("Enter state: ")
                    city = input("Enter city: ")
                    pin_no = input("Enter pin: ")
                    qualification = input("Enter qualification: ")
                    dept = input("Enter department: ")
                    insert_nurse(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept)

                case 2:  # Insert Doctor
                    print("\n--- Insert Doctor ---")
                    name = input("Enter doctor name: ")
                    sex = input("Enter gender: ")
                    salary = int(input("Enter salary: "))
                    mob_no = input("Enter mobile no.: ")
                    address = input("Enter address: ")
                    state = input("Enter state: ")
                    city = input("Enter city: ")
                    pin_no = input("Enter pin: ")
                    qualification = input("Enter qualification: ")
                    dept = input("Enter department: ")
                    insert_doctor(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept)

                case 3:  # Insert Receptionist
                    print("\n--- Insert Receptionist ---")
                    name = input("Enter receptionist name: ")
                    sex = input("Enter gender: ")
                    salary = int(input("Enter salary: "))
                    mob_no = input("Enter mobile no.: ")
                    address = input("Enter address: ")
                    state = input("Enter state: ")
                    city = input("Enter city: ")
                    pin_no = input("Enter pin: ")
                    insert_receptionist(name, sex, salary, mob_no, address, state, city, pin_no)

                case 4:
                    print("🔙 Returning to main menu...")
                    return True

                case _:
                    print("❌ Invalid sub-choice. Returning to main menu...")

        case 2:  # Patient Management
            print("\n--- Patient Management ---")
            print("1. Insert Patient")
            print("2. Assign Patient to Room")
            print("3. Back to main menu")

            sub_choice = int(input("Enter your choice: "))

            match sub_choice:
                case 1:
                    name = input("Enter patient name: ")
                    gender = input("Enter gender (Male/Female): ")
                    age = int(input("Enter age: "))
                    dob = input("Enter DOB (YYYY-MM-DD): ")
                    mob_no = input("Enter mobile number: ")
                    insert_patient(name, gender, age, dob, mob_no)
                case 2:
                    patient_id = int(input("Enter Patient ID: "))
                    room_id = int(input("Enter Room ID: "))
                    assign_patient_to_room(patient_id, room_id)
                case 3:
                    print("🔙 Returning to main menu...")
                    return True
                case _:
                    print("❌ Invalid sub-choice. Returning to main menu...")

        case 3:  # Room Management
            print("\n--- Room Management ---")
            print("1. Add New Room")
            print("2. Assign Nurse to Room")
            print("3. Back to main menu")

            sub_choice = int(input("Enter your choice: "))

            match sub_choice:
                case 1:
                    room_type = input("Enter room type: ")
                    capacity = int(input("Enter room capacity: "))
                    insert_room(room_type, capacity)
                case 2:
                    nurse_id = int(input("Enter Nurse ID: "))
                    room_id = int(input("Enter Room ID: "))
                    assign_nurse_to_room(nurse_id, room_id)
                case 3:
                    print("🔙 Returning to main menu...")
                    return True
                case _:
                    print("❌ Invalid sub-choice. Returning to main menu...")

        case 4:  # Test Reports
            print("\n--- Test Reports ---")
            patient_id = int(input("Enter Patient ID: "))
            test_type = input("Enter test type: ")
            result = input("Enter test result: ")
            insert_test_report(patient_id, test_type, result)

        case 5:  # Consult Management
            print("\n--- Consult Management ---")
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            create_consult(patient_id, doctor_id)

        case 6:  # Records Management
            print("\n--- Records Management ---")
            app_no = int(input("Enter Appointment Number: "))
            receptionist_id = int(input("Enter Receptionist ID: "))
            create_record(app_no, receptionist_id)

        case 7:  # Search Patient Status
            print("\n--- Search Patient Status ---")
            mob_no = input("Enter patient's phone number: ")
            search_patient_by_phone(mob_no)

        case 8:
            print("👋 Exiting program...")
            return False
        case _:
            print("❌ Invalid choice. Try again.")
    return True

# Run menu in loop
while True:
    if not menu():
        break

cursor.close()
conn.close()