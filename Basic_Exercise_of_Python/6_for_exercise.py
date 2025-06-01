# 1. After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# Using for loop figure out how many times you got heads

print("\n-----Exercise 1-----\n")

count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ", count)


print("\n-----Exercise 2-----\n")

# 2. Print square of all numbers between 1 to 10 except even numbers

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"The square of the {i} no are: \n", i*i)


print("\n-----Exercise 3-----\n")

# 3. Your monthly expense list (from Jan to May) looks like this,

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

exp = int(input("Enter expense amount: "))

for i, expense in enumerate(expense_list):
    if exp == expense:
        print(f"You spent {exp} amount in {month_list[i]}")
        break
else:
    print(f"You didn\'t spend {exp} in any month.")


print("\n-----Exercise 4-----\n")


# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(1, 6):
    x = input("Are you tired (yes/no): ").lower()

    if x == "no":
        if i == 5:
            print("Congratulations!!! You have finished the race.")
        else:
            continue
    elif x == "yes":
        print("You didn't finish the race.")
        break
    else:
        print("The input must be 'yes' or 'no'.")
        break


print("\n-----Exercise 5-----\n")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)
