from config import *
from storage import *

def generate_booking_id():
    bookings = read_file(BOOKING_FILE)
    number = len(bookings) + 1
    return "B" + str(number).zfill(5)

def add_booking():
    record=[]
#    b_id=input("Enter your Booking ID:")
    b_id=generate_booking_id()
    record.append(b_id)
    p_id=input("Enter your Passenger ID:")
    record.append(p_id)
    f_no=input("Enter your Flight Number:")
    record.append(f_no)
    s_no=input("Enter your Seat Number:")
    record.append(s_no)
    append_record(BOOKING_FILE,record)

def view_bookings():
    bookings = read_file(BOOKING_FILE)

    if len(bookings) == 0:
        print("No Bookings Found.")
        return
    print("-" * 80)
    print(
            f"{'BOOKING_ID':<15}"
            f"{'PASSENGER_ID':<15}"
            f"{'FLIGHT_NUMBER':>15}"
            f"{'SEAT_NUMBER':>15}"
        )
    print("-" * 80)

    print("-" * 60)
    for booking in bookings:
        print(f"{booking[0]:<15}"
            f"{booking[1]:<15}"
            f"{booking[2]:>15}"
            f"{booking[3]:>15}")
    print("-" * 60)
    
    input("Press enter to continue")

def revenue_report():
    bookings = read_file(BOOKING_FILE)
    flights = read_file(FLIGHT_FILE)

    revenue = 0

    for booking in bookings:
        for flight in flights:

            if booking[2] == flight[0]:
                revenue += int(flight[7])


    print("\n========== REVENUE REPORT ==========")
    print("Total Revenue :", revenue)
    input("Press enter to continue")



def cancel_booking():
    bid = input("Booking ID : ").upper()

    bookings = read_file(BOOKING_FILE)
    new_list = []
    flight_no = ""
    found = False

    for booking in bookings:
        if booking[0] == bid:
            found = True

        else:
            new_list.append(booking)


    if found:

        write_records(
            BOOKING_FILE,
            BOOKING_HEADER,
            new_list
        )

        print("Booking Cancelled.")

    else:
        print("Booking Not Found.")
    input("Press Enter to Continue")


def search_booking():
    bid = input("Booking ID : ").upper()

    bookings = read_file(BOOKING_FILE)

    for booking in bookings:
        if booking[0] == bid:
            print("\n=============  STATUS.  =============\n")
            print("\nBooking Found")
            print("\n========== BOOKING DETAILS ==========\n")
            print("\nBookingID:  ",booking[0],"\nPassengerID:",booking[1],"\nFlightNo:   ",booking[2],"\nSeatNo:     ",booking[3])
            print("-"*37)
            input("Press Enter to Continue")
            return

    print("Booking Not Found.")
    input("Press Enter to Continue")


def flight_occupancy_report():
    flights = read_file(FLIGHT_FILE)
    if len(flights) == 0:
        print("\nNo Flights Found.")
        return
    print("\n========== FLIGHT OCCUPANCY REPORT ==========\n")
    print(
        f"{'Flight':<10}"
        f"{'Source':<15}"
        f"{'Destination':<15}"
        f"{'Total':<10}"
        f"{'Booked':<10}"
        f"{'Available':<10}"
    )
    print("-" * 70)
    for flight in flights:
        total = int(flight[5])
        available = int(flight[6])
        booked = total - available
        print(
            f"{flight[0]:<10}"
            f"{flight[1]:<15}"
            f"{flight[2]:<15}"
            f"{total:<10}"
            f"{booked:<10}"
            f"{available:<10}"
        )
    input("Press Enter to Continue")