population = {
    "China" : 143,
    "India" : 136,
    "USA" : 32,
    "Pakistan" : 21
}

def add():
    country = input("Enter the contry name to add: ")
    country = country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p = input(f"Enter population for {country}: ")
    p = float(p)
    population[country] = p #Adds new key value

def remove():
    country = input("Enter country name to remove: ")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]

def query():
    country = input("Enter country name for query: ")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    task = input("Enter opration (add, remove, query or print): ").lower()
    if task == "add":
        add()
    elif task == "remove":
        remove()
    elif task == "query":
        query()
    elif task == "print":
        print()
    else:
        print("not a valid input")

if __name__ == "__main__":
    main()
