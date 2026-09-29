# Vehicle functions

def create_vehicle(number, owner, vehicle_type, slot):

    vehicle = [number, owner, vehicle_type, slot]

    return vehicle

def show_vehicle(vehicle):

    print("Vehicle Number:", vehicle[0])
    print("Owner:", vehicle[1])
    print("Vehicle Type:", vehicle[2])
    print("Slot Number:", vehicle[3])