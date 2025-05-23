# Car Showroom Inventory System

This is a simple command-line application to manage the inventory of a car showroom. It allows you to add cars, display the current inventory, sell cars, and search for cars based on various criteria. The data is stored in a JSON file (`showroom_data.json`) to persist between program runs.

## Features

* **Add Car to Inventory:** Allows you to enter details of a new car (make, model, year, color, price) and add it to the showroom's inventory. Each car is assigned a unique ID.
* **Display Inventory:** Shows a list of all cars currently in the showroom, including their details (ID, make, model, year, color, price, and status - Available or Sold).
* **Sell a Car (by ID):** Enables you to mark a car as sold by entering its unique Car ID.
* **Search Cars:** Provides the functionality to search for cars based on Car ID, make, model, year, or color. It displays all cars that match the search term.
* **Data Persistence:** The showroom's inventory data is saved to a `showroom_data.json` file in the same directory as the script. This ensures that the data is retained even after the program is closed and can be loaded when the program is run again.
* **Input Validation:** Basic input validation is implemented to ensure that required car details are provided and that year and price are entered in the correct numeric format.

## How to Run the Application

1.  **Save the Code:** Save the provided Python code as a file named `car_showroom.py` on your computer.
2.  **Open Terminal or Command Prompt:** Open your system's terminal (macOS/Linux) or command prompt (Windows).
3.  **Navigate to the Directory:** Use the `cd` command to navigate to the directory where you saved the `car_showroom.py` file.
4.  **Run the Script:** Execute the script using the Python interpreter:
    ```bash
    python car_showroom.py
    ```
    (or `python3 car_showroom.py` if you have both Python 2 and 3 installed and Python 3 is your default).

## Using the Application

Once the application starts, you will see the main menu:
