# Sets a variable named "cars" with the value of 100 int
cars = 100
# Sets a variable named "space_in_a_car" with the value of 4.0 float
space_in_a_car = 4
# Sets a variable named "drivers" with the value of 30 int
drivers = 30
# Sets a variable named "passengers" with the value of 90 int
passengers = 90
# Sets a variable named "cars_not_driven" with the value of the difference between the variable "cars" subtracted by the value of "drivers"
cars_not_driven = cars - drivers
# Sets a variable named "cars_driven" with the value of the variable "drivers"
cars_driven = drivers
# Sets a variable named "carpool_capacity" with the value of the product of the variable "cars_driven" times "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# Sets a variable named "average_passengers_per_car" with the value of the quotient of the variable "passengers" divided by "cars_driven" 
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Code Debug Explanation
# When Zed Shaw tried to use the variable "car_pool_capacity" in line 8, before defining it in this code which triggered a error message. If this variable was written after line 14, it would've worked perfectly



