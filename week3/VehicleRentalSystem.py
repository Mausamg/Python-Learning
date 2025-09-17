class Vehicle:
    def __init__(self, vehicle_id, brand, model):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.is_available = True

    def rent(self):
        self.is_available = False

    def return_vehicle(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"{self.vehicle_id}: {self.brand} {self.model} - {status}"


class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the system.")
            return
        for vehicle in self.vehicles:
            print(vehicle)

    def rent_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if vehicle.is_available:
                    vehicle.rent()
                    print(f"{vehicle.brand} {vehicle.model} rented successfully.")
                else:
                    print("Vehicle already rented.")
                return
        print("Vehicle ID not found.")

    def return_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if not vehicle.is_available:
                    vehicle.return_vehicle()
                    print(f"{vehicle.brand} {vehicle.model} returned successfully.")
                else:
                    print("Vehicle was not rented.")
                return
        print("Vehicle ID not found.")


def run():
    system = VehicleRentalSystem()

    # Sample vehicles
    system.add_vehicle(Vehicle("V001", "Toyota", "Corolla"))
    system.add_vehicle(Vehicle("V002", "Honda", "Civic"))
    system.add_vehicle(Vehicle("V003", "Tesla", "Model 3"))

    while True:
        print("\n--- Vehicle Rental System ---")
        print("1. Show Vehicles")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            system.show_vehicles()
        elif choice == '2':
            vehicle_id = input("Enter vehicle ID to rent: ").strip()
            system.rent_vehicle(vehicle_id)
        elif choice == '3':
            vehicle_id = input("Enter vehicle ID to return: ").strip()
            system.return_vehicle(vehicle_id)
        elif choice == '4':
            print("Thank you for using the Vehicle Rental System.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()
