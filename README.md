# Library Management System

A simple command-line Library Management System built with Python, designed to manage books, users, and check out/in operations. This system allows users to add, update, delete, and search for books and users. It also provides a simple logging mechanism to track operations.

# Project Directory Structure:

library-management-system/
│
├── book.py                 # Book management (add, update, delete, list, search)
├── user.py                 # User management (add, update, delete, list, search)
├── check.py                # Check out and check in functionality
├── log_operations.py       # Logging operations (add, view logs)
├── main.py                 # Main program and menu navigation
├── models.py               # Models for Book and User
├── storage.py              # File-based storage for persistence (books, users, checkouts)
└── data/                   # Directory for storing JSON data and logs
    ├── books.json          # Data storage for books
    ├── users.json          # Data storage for users
    ├── checkouts.json      # Data storage for checkouts
    └── operations.log      # Log file for tracking operations

# Steps to Set Up the Project

Clone the repository

```bash
git clone https://github.com/arunt7767/Redesigning-Poor-Code.git
cd library-management-system
```

Run the setup script

```bash
python setup.py
```
