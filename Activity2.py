print("===========================")
print("      Welcome to ride builder!     ")
print("===========================")
print()

print("Step 1: pick ur vehicle")
print(" 1 - Bike")
print(" 2 - car")
print()

choice = int(input("Enter 1 or 2:"))
print()

if choice == 1:
    print("Step 2:pick your bike type")
    print("1 - scooty")
    print("2 - Mountain bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City roads")
    else:
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")

elif choice == 2:
    # Nested if-else — runs only when choice is 2
    print("Step 2: Pick your car type")
    print("  1 - Sedan")
    print("  2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked  : Sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    else:
        print("You picked  : SUV")
        print("Seats       : 7 passengers")
        print("Best for    : Off-road adventures")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")

print()
print("====================================")
print("   Your custom ride is ready!       ")
print("   Enjoy the journey!               ")
print("====================================")
