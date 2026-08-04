from config import *
from storage import *

def generate_passenger_id():
    bookings = read_file(PASSENGER_FILE)
    number = len(bookings) + 1
    return "P" + str(number).zfill(8)

def add_passenger():
    record=[]
    
#    id=input("Enter your Passenger ID:")
    id=generate_passenger_id()
    record.append(id)
    name=input("Enter your Name:")
    record.append(name)
    age=input("Enter your Age:")
    record.append(age)
    gender=input("Enter your Gender:")
    record.append(gender)
    phone=input("Enter your Phone:")
    record.append(phone)
    append_record(PASSENGER_FILE,record)

def view_passengers():
    passengers = read_file(PASSENGER_FILE)
    print()
    if len(passengers) == 0:
        print("No Passengers Found.")
        return
    print("-" * 80)
    print(
        f"{'ID':<12}"
        f"{'Name':<22}"
        f"{'Age':<8}"
        f"{'Gender':<12}"
        f"{'Phone':<20}"
    )
    print("-" * 80)
    for passenger in passengers:
        print(
            f"{passenger[0]:<12}"
            f"{passenger[1]:<22}"
            f"{passenger[2]:<8}"
            f"{passenger[3]:<12}"
            f"{passenger[4]:<20}"
        )
    input("Press Enter to continue")


def search_passenger():
    pid = input("\nEnter Passenger ID : ").strip()
    passengers = read_file(PASSENGER_FILE)
    for passenger in passengers:
        if passenger[0] == pid:
            print("\n========== PASSENGER DETAILS ==========\n")
            print("PassengerID:",passenger[0],"\nName:       ",passenger[1],"\nAge:        ",passenger[2],"\nGender:     ",passenger[3],"\nPhone:      ",passenger[4])
            print("-"*39)
            input("Press Enter to Continue")
            return
    
    print("\nPassenger Not Found.")
    input("Press Enter to Continue")

def delete_passenger():
    pid = input("\nEnter Passenger ID : ").strip().upper()
    passengers = read_file(PASSENGER_FILE)
    new_list = []
    found = False
    for passenger in passengers:
        if passenger[0] == pid:
            found = True
        else:
            new_list.append(passenger)
    if found:
        write_records(
            PASSENGER_FILE,
            PASSENGER_HEADER,
            new_list
        )
        print("\nPassenger Deleted Successfully.")
    else:
        print("\nPassenger Not Found.")


def update_passenger():
    pid = input("\nEnter Passenger ID : ").strip().upper()
    passengers = read_file(PASSENGER_FILE)
    found = False
    for passenger in passengers:
        if passenger[0] == pid:
            print("\nPress Enter to keep existing value.\n")
            value = input(f"Name ({passenger[1]}) : ").strip()
            if value != "":
                passenger[1] = value.title()
            value = input(f"Age ({passenger[2]}) : ").strip()
            if value != "":
                passenger[2] = value
            value = input(f"Gender ({passenger[3]}) : ").strip()
            if value != "":
                passenger[3] = value.title()
            value = input(f"Phone ({passenger[4]}) : ").strip()
            if value != "":
                passenger[4] = value
            found = True
            break
    if found:
        write_records(
            PASSENGER_FILE,
            PASSENGER_HEADER,
            passengers
        )
        print("\nPassenger Updated Successfully.")
    else:
        print("\nPassenger Not Found.")