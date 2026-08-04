# write a function add_flights that take input of below fields and append_record in flights.csv
from storage import *
from config import *


def add_flights():
    record=[]
    flight_no=input("Enter the Flight Number: ")
    record.append(flight_no)
    
    source=input("Enter the Source City: ")
    record.append(source)
    
    destination=input("Enter the Destination: ")
    record.append(destination)
    
    departure=input("Enter the Departure: ")
    record.append(departure)
    
    arrival=input("Enter the Arrival: ")
    record.append(arrival)
    
    total_seats=input("Enter the Total seats: ")
    record.append(total_seats)
    
    available_seats=input("Enter the Available_seats: ")
    record.append(available_seats)
    
    fare=input("Enter the Fare: ")
    record.append(fare)
    append_record(FLIGHT_FILE,record)

def view_flights():
    flights = read_file(FLIGHT_FILE)
    if len(flights) == 0:
        print("\nNo Flights Available.")
        return

    print("\n" + "-" * 105)
    print(
        f"{'Flight':<10}"
        f"{'Source':<15}"
        f"{'Destination':<15}"
        f"{'Departure':<12}"
        f"{'Arrival':<12}"
        f"{'Total':<10}"
        f"{'Available':<20}"
        f"{'Fare':<10}"
    )
    print("-" * 105)

    for flight in flights:
        print(
            f"{flight[0]:<10}"
            f"{flight[1]:<15}"
            f"{flight[2]:<15}"
            f"{flight[3]:<12}"
            f"{flight[4]:<12}"
            f"{flight[5]:<10}"
            f"{flight[6]:<20}"
            f"{flight[7]:<10}"
        )
    input("Press enter to continue")

def update_flight():
    number = input("\nEnter Flight Number : ").strip().upper()
    flights = read_file(FLIGHT_FILE)
    found = False

    for flight in flights:
        if flight[0] == number:
            print("\nPress Enter to keep old value.\n")

            value = input(
                "Source ("+flight[1] +") : "
            )
            if value:
                flight[1] = value.title()

            value = input(
                "Destination ("+flight[2] +") : "
            )
            if value:
                flight[2] = value.title()

            value = input(
                "Departure ("+flight[3]+") : "
            )
            if value:
                flight[3] = value
            value = input(
                "Arrival ("+flight[4]+") : "
            )
            if value:
                flight[4] = value

            value = input(
                "Total Seats ("+flight[5]+") : "
            )

            if value:
                difference = (
                    int(value)
                    -
                    int(flight[5])
                )
                flight[5] = value
                flight[6] = str(
                    int(flight[6])
                    +
                    difference
                )

            value = input(
                "Fare ("+flight[7]+") : "
            )
            if value:
                flight[7] = value

            found = True
            break
        
    if found:
        write_records(
        FLIGHT_FILE,
        FLIGHT_HEADER,
        flights
        )
        print("\nFlight Updated Successfully.")
    else:
        print("\nFlight Not Found.")
    input("Press Enter to continue.")



def search_flight():
    number = input("\nEnter Flight Number : ").strip().upper()
    flights = read_file(FLIGHT_FILE)

    for flight in flights:
        if flight[0] == number:
            print("\n========== FLIGHT DETAILS ==========\n")
            print("Flight No.:  ",flight[0],"\nSource City: ",flight[1],"\nDestination: ",flight[2],"\nDeparture:   ",flight[3],"\nArrival:     ",flight[4],"\nSeat:        ",flight[5],"\nFare:        ",flight[6])
            print("--"*18)
            input("Press Enter to Continue")
            return
        
    input("Press Enter to continue")
    print("\nFlight Not Found.")

def delete_flight():
    number = input("\nEnter Flight Number : ").strip().upper()

    flights = read_file(FLIGHT_FILE)
    new_list = []
    found = False

    for flight in flights:
        if flight[0] == number:
            found = True
        else:
            new_list.append(flight)


    if found:
        write_records(
            FLIGHT_FILE,
            FLIGHT_HEADER,
            new_list
        )
        print("\nFlight Deleted Successfully.")
    else:
        print("\nFlight Not Found.")