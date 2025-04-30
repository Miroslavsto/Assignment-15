# Base Employee class
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        return self.salary * bonus_rate

    def show_info(self):
        print(f"Employee: {self.first_name} {self.last_name}")
        print(f"Salary: ${self.salary:.2f}")

# Derived Manager class
class Manager(Employee):
    def compute_long_term_bonus(self):
        return self.salary * 0.40

# Test the Manager class
print("Enter Manager Info:")
first = input("First Name: ")
last = input("Last Name: ")
salary = float(input("Salary: "))

manager = Manager(first, last, salary)
print("\n--- Manager Info ---")
manager.show_info()
print(f"Long Term Bonus: ${manager.compute_long_term_bonus():.2f}")

print("\n" + "-"*40 + "\n")

# Base Car class
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = self.compute_discount_price()

    def compute_discount_price(self):
        return self.sticker_price * 0.90

    def show_info(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Sticker Price: ${self.sticker_price:.2f}")
        print(f"Discount Price: ${self.discount_price:.2f}")

# Derived Sport class
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = False
        self.sport_engine = False
        self.sport_interior = False

    def add_sport_wheels(self, choice):
        if choice.upper() == 'Y':
            self.sport_wheels = True

    def add_sport_engine(self, choice):
        if choice.upper() == 'Y':
            self.sport_engine = True

    def add_sport_interior(self, choice):
        if choice.upper() == 'Y':
            self.sport_interior = True

    def price_with_options(self):
        price = self.discount_price
        if self.sport_wheels:
            price += 1000.00
        if self.sport_engine:
            price += 3000.00
        if self.sport_interior:
            price += 2000.00
        return price

    def show_price_with_options(self):
        self.show_info()
        print(f"Price with Options: ${self.price_with_options():.2f}")

# Test the Sport class
print("Enter Car Info:")
car_make = input("Make: ")
car_model = input("Model: ")
sticker = float(input("Sticker Price: "))

sport_car = Sport(car_make, car_model, sticker)

print("\nDo you want to add the following options?")
wheels_choice = input("Sport Wheels (Y/N): ")
engine_choice = input("Sport Engine (Y/N): ")
interior_choice = input("Sport Interior (Y/N): ")

sport_car.add_sport_wheels(wheels_choice)
sport_car.add_sport_engine(engine_choice)
sport_car.add_sport_interior(interior_choice)

print("\n--- Car Info ---")
sport_car.show_price_with_options()
