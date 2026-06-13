# Project 3 — The Data Warehouse

## Project Overview

This project demonstrates setting up a fully managed cloud database system on **Microsoft Azure** as part of the DecodeLabs Cloud Computing internship track.

The scenario simulates a real-world problem: an e-commerce company outgrowing Excel spreadsheets and needing a scalable, secure, cloud-based database solution.

---

## Objectives

- Provision a managed **Azure Database for MySQL Flexible Server**
- Configure **firewall rules** to restrict database access securely
- Design and engineer an **Interns** table with proper schema constraints
- Insert and verify **dummy records** for data persistence testing
- Connect to the database via **VS Code (SQLTools extension)**
- Connect programmatically via a **Python script**

---

## Tech Stack

| Tool                                     | Purpose                          |
| ---------------------------------------- | -------------------------------- |
| Microsoft Azure                          | Cloud platform                   |
| Azure Database for MySQL Flexible Server | Managed relational database      |
| VS Code + SQLTools Extension             | Visual SQL client                |
| Python                                   | Programmatic database connection |
| PyMySQL                                  | Python MySQL driver              |
| python-dotenv                            | Secure credential management     |
| Git & GitHub                             | Version control                  |

---

## Project Structure

```
decodelabs-project3/
├── .env                  # Local credentials (NOT uploaded to GitHub)
├── .gitignore
├── azure_db.py           # Python script to connect, create, insert & read
├── SELECT query result in MySQL tools on vscode.png
├── Terminal output from running azure_db.py.png
└── README.md

```

---

## Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Lichi-fave/Decodelabs-cloud-computing-internship.git
cd project-3
```

### 2. Install Dependencies

```bash
py -m pip install pymysql python-dotenv
```

### 3. Create Your .env File

Create a `.env` file in the root folder with your own Azure credentials:

- DB_HOST=your-server-name.mysql.database.azure.com
- DB_USER=your_admin_user@your-server-name
- DB_PASSWORD=your_password
- DB_NAME=decodelabs_db
- DB_PORT=3306

> Never share your `.env` file. It is listed in `.gitignore` and will not be uploaded.

### 4. Run the Python Script

```bash
python azure_db.py
```

---

## Database Schema

```sql
CREATE TABLE Interns (
    InternID  INT          PRIMARY KEY AUTO_INCREMENT,
    FirstName      VARCHAR(100) NOT NULL,
    LastName       VARCHAR(100) NOT NULL,
    Role      VARCHAR(100) NOT NULL,
    Email     VARCHAR(100) UNIQUE NOT NULL
);
```

### Constraints Explained

| Constraint     | Column     | Purpose                           |
| -------------- | ---------- | --------------------------------- |
| PRIMARY KEY    | InternID   | Uniquely identifies every row     |
| AUTO_INCREMENT | InternID   | Automatically assigns ID numbers  |
| NOT NULL       | Name, Role | Fields cannot be left empty       |
| UNIQUE         | Email      | No two interns can share an email |

---

## Sample Data

```sql
INSERT INTO Interns (Name, Role, Email) VALUES
    ('John', 'Abunwa', 'Backend Developer', 'jabunwa@decodelabs.com'),
    ('Jane', 'Love', 'Cloud Engineer', 'jlove@decodelabs.com'),
    ('Conan', 'Johnson', 'DevOps Intern', 'conjohnson@decodelabs.com');
```

---

## Security Practices Applied

- Database hosted on **Azure Database for MySQL Flexible Server**
- Access restricted via **Azure Firewall Rules** (IP whitelisting)
- **SSL encryption** enabled for all connections
- Credentials stored in **`.env` file** — never hardcoded in source code
- `.env` listed in **`.gitignore`** — never pushed to GitHub

---

## Milestone Checklist

- [x] Provisioned Azure MySQL Flexible Server
- [x] Configured firewall rules and IP whitelisting
- [x] Created `decodelabs-db` database
- [x] Engineered `Interns` table with proper constraints
- [x] Inserted 5 dummy records
- [x] Verified data with `SELECT * FROM Interns`
- [x] Connected via VS Code SQLTools extension
- [x] Connected via Python script (pymysql)

---

## Screenshots

### VS Code SQLTools - SELECT Query Result

![SELECT query result](project-3/SELECT query result in MySQL tools on vscode.png)

### Python Script - Terminal Output

![Python terminal output](project-3/Terminal output from running azure_db.py.png)

---

## What I Learned

- Difference between **relational (MySQL)** and **NoSQL (Cosmos DB)** databases
- How to provision and configure a **managed cloud database** on Azure
- Importance of **schema design** and data integrity constraints
- How **firewall rules** protect cloud databases from unauthorized access
- Connecting to cloud databases both **visually** and **programmatically**
- Secure credential management using **environment variables**
