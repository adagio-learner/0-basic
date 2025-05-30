# 1. Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "405 East 42nd Street"
city = "New York"
country = "United States"

address = "\n" + street + "\n" + city + "\n" + country + "\n"
print("Address using + operator:",address)

address = f'\n{street}\n{city}\n{country}\n'
print("Address using f-string:",address)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

fact = "Earth revolves around the sun"
print(fact[6:14])
print(fact[26:29])
print(fact[-3:])

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.

num_fruits = 10
num_vegetables = 5
print(f"I eat {num_vegetables} veggies and {num_fruits} fruits daily")


# 4. I have a string variable called s='I ate 200 bananas.'. This of course is a wrong statement, the correct statement is 'I ate 10 apples.'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s = "I ate 200 bananas"
s = s.replace("banana", "apple")
s = s.replace("200","10")
print(s)

st = "I ate 200 bananas"
st = st.replace("banana","apple").replace("200","10")
print(st)











