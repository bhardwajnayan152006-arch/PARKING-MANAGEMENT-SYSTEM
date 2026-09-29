#  parking data

parking = []

total_slots = 15

parking_fee = 30

total_collection = 0


# save vehicle data
def save_data():

    file = open("parking_data.txt", "w")

    for vehicle in parking:

        line = vehicle[0] + "," + vehicle[1] + "," + vehicle[2] + "," + str(vehicle[3])

        file.write(line + "\n")
    file.close()

# Load vehicle data
def load_data():

    global parking

    parking = []

    file = open("parking_data.txt", "r")

    for line in file:

        line = line.strip()

        if line != "":

            parts = line.split(",")

            number = parts[0]
            owner = parts[1]
            vehicle_type = parts[2]
            slot = int(parts[3])

            vehicle = [number, owner, vehicle_type, slot]

            parking.append(vehicle)

    file.close()


# Save collection
def save_collection():

    file = open("collection.txt", "w")

    file.write(str(total_collection))

    file.close()


# Load  collection
def load_collection():

    global total_collection

    file = open("collection.txt", "r")

    value = file.read().strip()

    if value != "":
        total_collection = int(value)

    file.close()