from dataclasses import dataclass

@dataclass
class Cab:
    cab_id: int
    driver_name: str
    capacity: int
    fare_per_km: float

    def calculate_fare(self, distance_km: float) -> float:
        return self.fare_per_km * distance_km

if __name__ == "__main__":
    my_cab = Cab(cab_id=1212, driver_name="Prajwal", capacity=2, fare_per_km=1000)
    distance = 100.0
    total_fare = my_cab.calculate_fare(distance)

    print(f"Cab ID: {my_cab.cab_id}")
    print(f"Driver: {my_cab.driver_name}")
    print(f"Capacity: {my_cab.capacity} passengers")
    print(f"Fare for {distance} km: ${total_fare:.2f}")