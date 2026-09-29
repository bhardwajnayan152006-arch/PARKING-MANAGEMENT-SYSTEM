import data
import parking
import search
import reports

# Main menu
def main():

    data.load_data()

    data.load_collection()

    while True:

        print("\n==============================")
        print("     PARKING MANAGEMENT SYSTEM")
        print("=================================")

        print("1. Vehicle Entry")
        print("2. Vehicle Exit")
        print("3. Show Parked Vehicles")
        print("4. Search Vehicle")
        print("5. Show Available Slots")
        print("6. Parking Summary")
        print("7. Vehicle Count")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":

            parking.vehicle_entry()

        elif choice == "2":

            parking.vehicle_exit()

        elif choice == "3":

            search.show_vehicles()

        elif choice == "4":

            search.search_vehicle()

        elif choice == "5":

            search.available_slots()

        elif choice == "6":

            reports.parking_summary()

        elif choice == "7":

            reports.vehicle_count()

        elif choice == "8":

            print("Thank you for using Parking Management System")

            break

        else:
            print("Invalid choice")

main()