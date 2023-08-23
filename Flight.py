class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        self.populate_flights()

    def populate_flights(self):
        data = [
            ("AI161E90", "BLR", "BOM", 5600),
            ("BR161F91", "BOM", "BBI", 6750),
            ("AI161F99", "BBI", "BLR", 8210),
            ("VS171E20", "JLR", "BBI", 5500),
            ("AS171G30", "HYD", "JLR", 4400),
            ("AI131F49", "HYD", "BOM", 3499),
        ]
        for flight_id, source, destination, price in data:
            self.flights.append(Flight(flight_id, source, destination, price))

    def search_by_city(self, city):
        city_flights = [flight for flight in self.flights if city in (flight.source, flight.destination)]
        return city_flights

    def search_flights_from_city(self, city):
        flights_from_city = [flight for flight in self.flights if flight.source == city]
        return flights_from_city

    def search_flights_between_cities(self, city1, city2):
        flights_between_cities = [flight for flight in self.flights if flight.source == city1 and flight.destination == city2]
        return flights_between_cities

def main():
    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    flight_table = FlightTable()

    while True:
        print("\nSearch Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            city_code = input("Enter city code (e.g. BLR): ")
            city_flights = flight_table.search_by_city(city_code)
            print("Flights related to", cities.get(city_code, "Unknown City"))
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, From: {cities.get(flight.source)}, To: {cities.get(flight.destination)}, Price: {flight.price}")
        
        elif choice == 2:
            city_code = input("Enter city code (e.g. BLR): ")
            flights_from_city = flight_table.search_flights_from_city(city_code)
            print("Flights from", cities.get(city_code, "Unknown City"))
            for flight in flights_from_city:
                print(f"Flight ID: {flight.flight_id}, To: {cities.get(flight.destination)}, Price: {flight.price}")
        
        elif choice == 3:
            city_code1 = input("Enter source city code (e.g. BLR): ")
            city_code2 = input("Enter destination city code (e.g. BOM): ")
            flights_between_cities = flight_table.search_flights_between_cities(city_code1, city_code2)
            print("Flights between", cities.get(city_code1, "Unknown City"), "and", cities.get(city_code2, "Unknown City"))
            for flight in flights_between_cities:
                print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
