# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length_of_field = 92
width_of_field = 48.8

total_area = length_of_field * width_of_field
print(f"{total_area:.2f} m")

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

each_packet_cost = 1.49
total_cost = 9 * each_packet_cost

change_cash = 20 - total_cost
print(f"{change_cash} $")


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)

total_area_of_bathroom = 5.5 ** 2
total_cost_tiles = total_area_of_bathroom * 500

print(f"{total_cost_tiles} $")

# 4. Print binary representation of number 17

num = 17
print("Binary of number 17 is:",format(num,"b"))
