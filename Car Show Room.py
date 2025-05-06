import json
import os

class Car:
    def __init__(self, car_id, make, model, year, color, price):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = int(year)
        self.color = color
        self.price = float(price)
        self.is_sold = False

    def display_details(self):
        return (f"Car ID: {self.car_id}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Color: {self.color}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Status: {'Sold' if self.is_sold else 'Available'}\n"
                f"{'-' * 20}")

    def mark_as_sold(self):
        self.is_sold = True

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'price': self.price,
            'is_sold': self.is_sold
        }

    @classmethod
    def from_dict(cls, data):
        car = cls(data['car_id'], data['make'], data['model'], data['year'], data['color'], data['price'])
        car.is_sold = data['is_sold']
        return car

class Showroom:
    def __init__(self, name, filename="showroom_data.json"):
        self.name = name
        self.filename = filename
        self.inventory = self._load_inventory()
        self.next_car_id = self._get_next_car_id()

    def _load_inventory(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                if 'inventory' in data and isinstance(data['inventory'], list):
                    return [Car.from_dict(item) for item in data['inventory']]
                else:
                    print("Warning: Inventory data file is malformed. Starting with an empty inventory.")
                    return []
        except json.JSONDecodeError:
            print("Warning: Error decoding inventory data file. Starting with an empty inventory.")
            return []
        except Exception as e:
            print(f"Warning: An error occurred while loading inventory: {e}. Starting with an empty inventory.")
            return []

    def _save_inventory(self):
        data = {'inventory': [car.to_dict() for car in self.inventory]}
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Inventory saved.")
        except IOError:
            print("Error saving inventory to file.")
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def _get_next_car_id(self):
        if self.inventory:
            return max(car.car_id for car in self.inventory) + 1
        else:
            return 1

    def add_car(self, make, model, year, color, price):
        if not all([make.strip(), model.strip(), str(year).strip(), color.strip(), str(price).strip()]):
            print("Error: All car details are required.")
            return

        try:
            year = int(year.strip())
            price = float(price.strip())
            if year <= 1900 or price <= 0:
                print("Error: Invalid year or price.")
                return
        except ValueError:
            print("Error: Invalid input for year or price. Please enter numeric values.")
            return

        new_car = Car(self.next_car_id, make.strip(), model.strip(), year, color.strip(), price)
        self.inventory.append(new_car)
        self.next_car_id += 1
        self._save_inventory()
        print(f"'{make.strip()} {model.strip()}' (ID: {new_car.car_id}) added to the showroom.")

    def display_inventory(self):
        if not self.inventory:
            print(f"\nShowroom '{self.name}' is currently empty.")
            return
        print(f"\n--- Inventory of {self.name} ---")
        for car in self.inventory:
            print(car.display_details())

    def find_car(self, car_id):
        try:
            car_id = int(str(car_id).strip())
        except ValueError:
            print("Error: Invalid Car ID format.")
            return None
        for car in self.inventory:
            if car.car_id == car_id:
                return car
        return None

    def sell_car(self, car_id):
        car_to_sell = self.find_car(car_id)
        if car_to_sell:
            if not car_to_sell.is_sold:
                car_to_sell.mark_as_sold()
                self._save_inventory()
                print(f"Car ID {car_id} ({car_to_sell.make} {car_to_sell.model}) has been sold.")
            else:
                print(f"Error: Car ID {car_id} is already sold.")
        else:
            print(f"Error: Car with ID {car_id} not found in the inventory.")

    def search_cars(self, search_term):
        search_term = str(search_term).strip().lower()
        if not search_term:
            print("Please enter a search term.")
            return
        results = []
        for car in self.inventory:
            if (search_term in str(car.car_id).lower() or
                    search_term in car.make.lower() or
                    search_term in car.model.lower() or
                    search_term in str(car.year).lower() or
                    search_term in car.color.lower()):
                results.append(car)

        if results:
            print(f"\n--- Search Results for '{search_term}' ---")
            for car in results:
                print(car.display_details())
        else:
            print(f"No cars found matching '{search_term}'.")

def main():
    showroom_name = input("Enter the name of the car showroom: ").strip()
    showroom = Showroom(showroom_name)

    while True:
        print("\n--- Car Showroom System ---")
        print(f"Showroom: {showroom.name}")
        print("1. Add Car to Inventory")
        print("2. Display Inventory")
        print("3. Sell a Car (by ID)")
        print("4. Search Cars")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            make = input("Enter car make: ").strip()
            model = input("Enter car model: ").strip()
            year = input("Enter car year: ").strip()
            color = input("Enter car color: ").strip()
            price = input("Enter car price: ").strip()
            showroom.add_car(make, model, year, color, price)
        elif choice == '2':
            showroom.display_inventory()
        elif choice == '3':
            car_id_to_sell = input("Enter the Car ID to sell: ").strip()
            showroom.sell_car(car_id_to_sell)
        elif choice == '4':
            search_term = input("Enter a search term: ").strip()
            showroom.search_cars(search_term)
        elif choice == '5':
            print("Exiting the car showroom system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    