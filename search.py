import data


# Find vehicle
def search_vehicle():

    number = input("Enter vehicle number: ")

    for v in data.parking:

        if v[0] == number:

            print("--------- VEHICLE FOUND ---------")

            print("Vehicle Number:", v[0])
            print("Owner:", v[1])
            print("Vehicle Type:", v[2])
            print("Slot Number:", v[3])

            return

    print("Vehicle not found")


# Show parked vehicles
def show_vehicles():

    if len(data.parking) == 0:

        print("No vehicles are parked")

        return

    print("--------- PARKED VEHICLES ---------")

    for v in data.parking:

        print("-------------------------")

        print("Vehicle Number:", v[0])
        print("Owner:", v[1])
        print("Vehicle Type:", v[2])
        print("Slot Number:", v[3])


# Show available slots
def available_slots():

    print("--------- AVAILABLE SLOTS ---------")

    found = False

    for slot in range(1, data.total_slots + 1):

        occupied = False

        for v in data.parking:

            if v[3] == slot:

                occupied = True
                break
        if occupied == False:
            print("Slot", slot, "is available")
            found = True
    if found == False:
        print("No slots available")