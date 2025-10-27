# 🏥 Hospital Management System (HMS)

A comprehensive Python-based Hospital Management System built with MySQL database integration, featuring nested switch-case menu structures for efficient hospital operations management.

## 📋 Table of Contents

- [Features](#features)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [System Architecture](#system-architecture)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 🏥 Core Functionality
- **Employee Management**: Add and manage Doctors, Nurses, and Receptionists
- **Patient Management**: Patient registration and room assignment
- **Room Management**: Room allocation and nurse assignment
- **Test Reports**: Medical test result management
- **Consult Management**: Doctor-patient consultation tracking
- **Records Management**: Appointment and record maintenance
- **Patient Search**: Comprehensive patient status lookup by phone number

### 🔧 Technical Features
- **Nested Switch-Case Menu**: Intuitive command-line interface
- **MySQL Integration**: Robust database connectivity
- **Relationship Management**: Proper foreign key handling
- **Data Validation**: Input validation and error handling
- **Transaction Safety**: Database transaction management

## 🗄️ Database Schema

The system uses a comprehensive MySQL database with the following main entities:

### Core Tables
- **Employee**: Base employee information
- **Doctor**: Doctor-specific details (qualification, department)
- **Nurse**: Nurse-specific details (qualification, department)
- **Receptionist**: Receptionist information
- **Patient**: Patient demographics and contact information
- **Rooms**: Room details (type, capacity, availability)
- **Bills**: Patient billing information
- **Test_Report**: Medical test results
- **Records**: Appointment records

### Relationship Tables
- **Consults**: Doctor-Patient consultation relationships
- **Assigned**: Patient-Room assignments
- **Governs**: Nurse-Room governance relationships
- **Maintains**: Receptionist-Record maintenance relationships

## 🚀 Installation

### Prerequisites
- Python 3.7+
- MySQL Server 5.7+
- mysql-connector-python

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hmsproject3.git
   cd hmsproject3
   ```

2. **Install dependencies**
   ```bash
   pip install mysql-connector-python
   ```

3. **Database Setup**
   - Create a MySQL database named `hospitaldb`
   - Run the SQL commands from `dbstructure.md` to create tables
   - Update database credentials in `app.py`:
     ```python
     conn = mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="hospitaldb"
     )
     ```

4. **Run the application**
   ```bash
   python app.py
   ```

## 📖 Usage

### Main Menu Navigation
```
Hospital Management System
├── 1. Employee Management
│   ├── 1. Insert Nurse
│   ├── 2. Insert Doctor
│   ├── 3. Insert Receptionist
│   └── 4. Back to main menu
├── 2. Patient Management
│   ├── 1. Insert Patient
│   ├── 2. Assign Patient to Room
│   └── 3. Back to main menu
├── 3. Room Management
│   ├── 1. Add New Room
│   ├── 2. Assign Nurse to Room
│   └── 3. Back to main menu
├── 4. Test Reports
├── 5. Consult Management
├── 6. Records Management
├── 7. Search Patient Status
└── 8. Exit
```

### Key Operations

#### Adding Employees
1. Select **Employee Management**
2. Choose employee type (Nurse/Doctor/Receptionist)
3. Enter required information
4. System automatically handles database relationships

#### Patient Search
1. Select **Search Patient Status**
2. Enter patient's phone number
3. View comprehensive patient information including:
   - Basic demographics
   - Room assignment status
   - Assigned medical staff
   - Test results
   - Billing information

#### Room Management
- Add new rooms with type and capacity
- Assign nurses to govern specific rooms
- Assign patients to available rooms
- Automatic availability tracking

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Interface │    │  Business Logic │    │   Database      │
│   (CLI Menu)     │◄──►│   (Functions)   │◄──►│   (MySQL)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Key Components
- **Menu System**: Nested switch-case structure for intuitive navigation
- **Database Layer**: MySQL connector for data persistence
- **Business Logic**: Modular functions for each operation
- **Error Handling**: Comprehensive error management and user feedback

## 📚 API Reference

### Core Functions

#### Employee Management
```python
insert_nurse(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept)
insert_doctor(name, sex, salary, mob_no, address, state, city, pin_no, qualification, dept)
insert_receptionist(name, sex, salary, mob_no, address, state, city, pin_no)
```

#### Patient Management
```python
insert_patient(name, gender, age, dob, mob_no)
assign_patient_to_room(patient_id, room_id)
search_patient_by_phone(mob_no)
```

#### Room Management
```python
insert_room(room_type, capacity)
assign_nurse_to_room(nurse_id, room_id)
```

#### Medical Operations
```python
insert_test_report(patient_id, test_type, result)
create_consult(patient_id, doctor_id)
create_record(app_no, receptionist_id)
```

## 🔧 Configuration

### Database Configuration
Update the connection parameters in `app.py`:

```python
conn = mysql.connector.connect(
    host="localhost",        # Your MySQL host
    user="root",            # Your MySQL username
    password="",            # Your MySQL password
    database="hospitaldb"   # Your database name
)
```

### Environment Variables (Optional)
You can use environment variables for sensitive data:

```python
import os
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', ''),
    database=os.getenv('DB_NAME', 'hospitaldb')
)
```

## 🧪 Testing

### Manual Testing
1. **Employee Addition**: Test adding different types of employees
2. **Patient Registration**: Register patients and assign to rooms
3. **Search Functionality**: Test patient search with various phone numbers
4. **Room Management**: Test room creation and assignment
5. **Error Handling**: Test with invalid inputs

### Test Data
```sql
-- Sample employee data
INSERT INTO Employee (Name, Sex, Salary, Mob_No, Address, State, City, Pin_no) 
VALUES ('Dr. Smith', 'Male', 80000, '1234567890', '123 Main St', 'CA', 'Los Angeles', '90210');

-- Sample patient data
INSERT INTO Patient (Name, Gender, Age, DOB, Mob_No) 
VALUES ('John Doe', 'Male', 35, '1988-01-15', '9876543210');
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex functions
- Include error handling for new features
- Update documentation for new functionality


## 👥 Authors

- Ritobrata Khan- (https://github.com/RitobrataK)

## 🙏 Acknowledgments

- Thank you to my mentor shibshankar sir to guide me throughout this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/hmsproject/issues) page
2. Create a new issue with detailed description

## 🔮 Future Enhancements

- [ ] Web-based interface
- [ ] User authentication system
- [ ] Advanced reporting features
- [ ] Mobile application
- [ ] Integration with medical devices
- [ ] Automated billing system
- [ ] Appointment scheduling
- [ ] Inventory management

---

**Made with ❤️ for better healthcare management**
