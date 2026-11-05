# Create the dictionary - car names are key and values are mpg
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
#Display only the keys from the dictionary
print(cars.keys())
print()
#Get the user to pick a car
car_name = input("Enter a car to see its mpg: ")
# Get the mpg for the given car
car_mpg = cars[car_name]
print()
# Display the MPG
print(f"The {car_name} gets {car_mpg} MPG")
print()
#Get the miles the user will drive on the car
miles_driven = float(input("How many miles will you drive the Pirus?:"))
print()
#Calculate how much money and gas the use will need to drive the car
gallons_gas = miles_driven / car_mpg
#Display the amount of money and gas the user will need to use to drive the car
print(f" {gallons_gas:.2} gallon(s) of gas are needed to drive the {car_name}
{miles_driven}.")
