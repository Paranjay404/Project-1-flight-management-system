# Airline Reservation System

## Objective
Built to practice file-based data persistence and multi-module project 
structure — using CSV files as a lightweight database and separating 
the system into distinct modules by responsibility (auth, flights, 
passengers, bookings, storage).

## What it does
- Login system with username/password and role-based access (admin 
  vs regular user)
- Add, view, search, update, and delete flight records
- Add, view, search, update, and delete passenger records
- Book and cancel tickets
- Admin-only reports: flight occupancy and total revenue
- All data persisted to CSV files (`flights.csv`, `passengers.csv`, 
  `bookings.csv`, `users.csv`)

## What I focused on / learned
- Reading and writing structured data with Python's `csv` module
- Splitting a project into modules with a single clear purpose each 
  (`config.py` for constants, `storage.py` for file I/O, `auth.py` 
  for login, etc.)
- Building a menu-driven CLI application with role-based menus

## Known limitations (next steps)
- Seat availability isn't automatically updated when a booking is 
  made or cancelled — this needs to be fixed before seat counts are 
  reliable
- Passwords are stored in plain text — would like to add hashing
- Limited input validation — invalid input can crash the program
- No automated tests yet

## How to run
1. Make sure Python 3 is installed
2. Clone this repo
3. Run:
```
   python main.py
```
