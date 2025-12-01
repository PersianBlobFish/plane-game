source = input("Source station: ")
destination = input("Destination station: ")
distance_km = float(input("Distance in kilometers: "))
class_type = input("Class (Economy/Sleeper/AC): ").strip().lower()
passenger = input("Passenger type (Adult/Child/Senior): ").strip().lower()
base_fare_per_km = 2
class_multipliers = {
    "economy": 1.0,
    "sleeper": 1.5,
    "ac": 2.0
}
passenger_discounts = {
    "adult": 0.0,
    "child": 0.5,
    "senior": 0.2
}

print("Base fare = $",base_fare_per_km,"per km")
if class_type in class_multipliers:
    class_multiplier = class_multipliers[class_type]
else:
    print("Invalid class type. Defaulting to Economy.")
    class_multiplier = class_multipliers["economy"]
if passenger in passenger_discounts:
    passenger_discount = passenger_discounts[passenger]
else:
    print("Invalid passenger type. Defaulting to Adult.")
    passenger_discount = passenger_discounts["adult"]
base_fare = distance_km * base_fare_per_km
fare_after_class = base_fare * class_multiplier
final_fare = fare_after_class * (1 - passenger_discount)
print(f"Ticket from {source} to {destination}")
print(f"Distance: {distance_km} km")
print(f"Class: {class_type.capitalize()}")
print(f"Clases Multiplier: {class_multiplier}")
print(f"Passenger Type: {passenger.capitalize()}")
print(f"Total before discount: ${base_fare:.2f}")
print(f"Fare after class multiplier: ${fare_after_class:.2f}","(", 100/class_multiplier, "%", ")")
print(f"Discount applied: {passenger_discount*100}%")
print(f"Total Fare: ${final_fare:.2f}")

print("Thank you for choosing Python Railways!")