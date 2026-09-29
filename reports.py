import data


#  parking summary
def parking_summary():

    print("--------- PARKING SUMMARY ---------")

    print("Total Slots:", data.total_slots)

    print("Occupied Slots:", len(data.parking))

    print(
        "Available Slots:",
        data.total_slots - len(data.parking)
    )

    print("Parking Fee:", data.parking_fee)

    print("Total Collection:", data.total_collection)

# vehicle count
def vehicle_count():

    cars = 0
    bikes = 0

    for v in data.parking:

        if v[2] == "Car":

            cars = cars + 1

        elif v[2] == "Bike":

            bikes = bikes + 1

    print("-------- VEHICLE COUNT ---------")

    print("Cars:", cars)

    print("Bikes:", bikes)

    print("Total Vehicles:", len(data.parking))