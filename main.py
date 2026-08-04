
from storage import *
from config import *
from auth import *
import auth

from flight import *
from passenger import *
from booking import *

create_file(FLIGHT_FILE,FLIGHT_HEADER)
create_file(PASSENGER_FILE,PASSENGER_HEADER)
create_file(BOOKING_FILE,BOOKING_HEADER)
create_file(USER_FILE,USER_HEADER)



# ---------------------------------------
# Main Program
# ---------------------------------------
login_success,role=auth.check_login()
if login_success == True:


    while True:

        print("\n")
        print("=" * 65)
        print(
            "AIRLINE RESERVATION SYSTEM".center(65)
        )
        print("=" * 65)


        # ---------------- Flight ----------------
        print("\nFlight Management")
        print("1.  Add Flight")
        print("2.  View Flights")
        print("3.  Search Flight")
        print("4.  Update Flight")
        print("5.  Delete Flight")


        # -------------- Passenger --------------
        print("\nPassenger Management")
        print("6.  Add Passenger")
        print("7.  View Passengers")
        print("8.  Search Passenger")
        print("9.  Update Passenger")
        print("10. Delete Passenger")


        # ---------------- Booking ----------------
        print("\nBooking Management")
        print("11. Book Ticket")
        print("12. View Bookings")
        print("13. Search Booking")
        print("14. Cancel Booking")


        # ---------------- Reports ----------------
        if role=="admin":
            print("\nADMIN PERSONNEL ONLY")
            print("15. Flight Occupancy Report")
            print("16. Revenue Report")
            print("17. Create NEW USER")
            print("18. Delete User")


        print("\n0. Exit")

        choice = input("\nEnter Choice : ")
        



        # ---------------- Flight ----------------
        if choice == "1":
            add_flights()

        elif choice == "2":
            view_flights()

        elif choice == "3":
            search_flight()

        elif choice == "4":
            update_flight()

        elif choice == "5":
            delete_flight()


        # -------------- Passenger --------------
        elif choice == "6":
            add_passenger()

        elif choice == "7":
            view_passengers()

        elif choice == "8":
            search_passenger()

        elif choice == "9":
            update_passenger()

        elif choice == "10":
            delete_passenger()


        # ---------------- Booking ----------------
        elif choice == "11":
            add_booking()

        elif choice == "12":
            view_bookings()
        elif choice == "13":
            search_booking()

        elif choice == "14":
            cancel_booking()
            

        # ---------------- Reports ----------------
        elif choice == "15":
            flight_occupancy_report()

        elif choice == "16":
            revenue_report()
        
        elif choice == "17":
            create_newuser()
        
        elif choice == "18":
            delete_user()

        # ---------------- Exit ----------------
        elif choice == "0":

            print(
                "\nThank You for using Airline Reservation System."
            )
            break

        else:
            print("\nInvalid Choice.")

else:

    print("\nProgram Closed.")


