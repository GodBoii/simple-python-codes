class Cab:
    def __init__(self, cab_id, driver_name, capacity, fare_per_km):
        self.cab_id = cab_id
        self.driver_name = driver_name
        self.capacity = capacity
        self.fare_per_km = fare_per_km

    def calculate_fare(self, distance_km):
        return self.fare_per_km * distance_km


class LuxuryCab(Cab):
    def __init__(self, cab_id, driver_name, capacity, fare_per_km, luxury_charge):
        super().__init__(cab_id, driver_name, capacity, fare_per_km)
        self.luxury_charge = luxury_charge

    def calculate_fare(self, distance_km):
        base_fare = super().calculate_fare(distance_km)
        total_fare = base_fare + self.luxury_charge
        return total_fare


if __name__ == "__main__":
    regular_cab = Cab(cab_id=1212, driver_name="Prajwal", capacity=4, fare_per_km=10.0)
    luxury_cab = LuxuryCab(cab_id=201, driver_name="Vinay", capacity=2, fare_per_km=15.0, luxury_charge=200)

    print(f"Regular Cab Fare for 10 km: {regular_cab.calculate_fare(10)}")
    print(f"Luxury Cab Fare for 10 km: {luxury_cab.calculate_fare(10)}")