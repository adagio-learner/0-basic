# Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#  1. Write a program that asks user to enter a city name and it should tell which country the city belongs to

city = input("Enter the city name: ")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! sorry!")

print("--------------------------------------------------------------")

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not.For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

city1 = input("Enter the name of the first city: ")
city2 = input("Enter the name of the second city: ")

if city1 in india and city2 in india:
    print(f"Both {city1} and {city2} are in India")
elif city1 in pakistan and city2 in pakistan:
    print(f"Both {city1} and {city2} are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"Both {city1} and {city2} are in Bangladesh")
else:
    print("They don't belong to same country")

print("--------------------------------------------------------------")

# 2. Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = input("Enter the sugar level: ")
sugar_level = float(sugar_level)

if sugar_level < 80:
    print("The suger is low, go eat some jalebi")
elif sugar_level > 100:
    print("The sugar is high, stop eating all mithais..!")
else:
    print("Sugar is normal, relax and enjoy your life!")
