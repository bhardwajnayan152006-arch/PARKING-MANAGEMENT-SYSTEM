import data
import vehicle
import validation
import billing


# Add vehicle 
def vehicle_entry():

    if len(data.parking) >= data.total_slots:

        print("Parking is full")

        return

    number = input("Enter vehicle number: ")

    # Check duplicate vehicle
    for v in data.parking:

        if v[0] == number:

            print("Vehicle already parked")

            return

    owner = input("Enter owner name: ")

    vehicle_type = input("Enter vehicle type (Car/Bike): ")

    vehicle_type = validation.check_vehicle_type(vehicle_type)

    if vehicle_type == "":

        print("Enter Car or Bike")
        return

    # Find empty slot
    slot = 1

    while slot <= data.total_slots:
        occupied = False

        for v in data.parking:

            if v[3] == slot:

                occupied = True

                break
        if occupied == False:

            break

        slot = slot + 1

    new_vehicle = vehicle.create_vehicle(
        number,
        owner,
        vehicle_type,
        slot)
    
    data.parking.append(new_vehicle)

    data.save_data()

    print("Vehicle parked successfully")

    vehicle.show_vehicle(new_vehicle)


# Remove vehicle
def vehicle_exit():

    number = input("Enter vehicle number: ")

    for v in data.parking:

        if v[0] == number:

            data.parking.remove(v)

            fee = billing.calculate_fee(data.parking_fee)

            data.total_collection = data.total_collection + fee

            data.save_data()
            data.save_collection()

            print("Vehicle exit successful")

            billing.show_bill(
                v[0],
                v[1],
                v[3],
                fee
            )

            return
    print("Vehicle not found")