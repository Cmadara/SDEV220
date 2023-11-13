class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = 0
        self.make = ""
        self.model = ""
        self.doors = 0
        self.roof_type = ""

    def set_car_info(self, year, make, model, doors, roof_type):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof_type}")


def main():
    # Get user input
    vehicle_type = input("Enter the vehicle type (car, truck, plane, boat, or broomstick): ").lower()

    # Create an instance of the Automobile class
    car = Automobile()

    # Set the vehicle type
    car.set_vehicle_type(vehicle_type)

    # Get additional user input for car attributes
    car.set_car_info(
        int(input("Enter the year: ")),
        input("Enter the make: "),
        input("Enter the model: "),
        int(input("Enter the number of doors (2 or 4): ")),
        input("Enter the type of roof (solid or sun roof): "),
    )

    # Display the car information
    print("\nCar Information:")
    car.display_info()


if __name__ == "__main__":
    main()