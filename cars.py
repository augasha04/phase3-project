from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the engine and connect to the database
engine = create_engine('sqlite:///car_dealership.db')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

# Define the Car table
class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    manufacturer = relationship("Manufacturer", back_populates="cars")
    category = relationship("Category", back_populates="cars")

# Define the Manufacturer table
class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cars = relationship("Car", back_populates="manufacturer")

# Define the Category table
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cars = relationship("Car", back_populates="category")

# Create the tables
Base.metadata.create_all()

class CarDealership:
    def __init__(self):
        self.session = Session()

    def add_car(self, make, model, year, price, manufacturer, category):
        car = Car(make=make, model=model, year=year, price=price)
        manufacturer_obj = self.session.query(Manufacturer).filter_by(name=manufacturer).first()
        if manufacturer_obj is None:
            manufacturer_obj = Manufacturer(name=manufacturer)
        category_obj = self.session.query(Category).filter_by(name=category).first()
        if category_obj is None:
            category_obj = Category(name=category)
        car.manufacturer = manufacturer_obj
        car.category = category_obj
        self.session.add(car)
        self.session.commit()
        print("Car added successfully!")

    def remove_car(self, car_id):
        car = self.session.query(Car).get(car_id)
        if car:
            self.session.delete(car)
            self.session.commit()
            print("Car removed successfully!")
        else:
            print("Car not found!")

    def search_car(self, make, model, year):
        car = self.session.query(Car).filter_by(make=make, model=model, year=year).first()
        if car:
            return car
        else:
            return None

    def display_inventory(self):
        cars = self.session.query(Car).all()
        print("Car Inventory:")
        for car in cars:
            print(f"{car.make} {car.model} ({car.year}) - ${car.price} | Manufacturer: {car.manufacturer.name} | Category: {car.category.name}")

    def close(self):
        self.session.close()


def main():
    dealership = CarDealership()

    while True:
        print("\nCar Dealership CLI")
        print("1. Add a car")
        print("2. Remove a car")
        print("3. Search for a car")
        print("4. Display inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = int(input("Enter the year of the car: "))
            price = int(input("Enter the price of the car: "))
            manufacturer = input("Enter the manufacturer of the car: ")
            category = input("Enter the category of the car: ")

            dealership.add_car(make, model, year, price, manufacturer, category)

        elif choice == "2":
            car_id = int(input("Enter the ID of the car to remove: "))
            dealership.remove_car(car_id)

        elif choice == "3":
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = int(input("Enter the year of the car: "))

            car = dealership.search_car(make, model, year)
            if car:
                print(f"Car found: {car.make} {car.model} ({car.year}) - ${car.price} | Manufacturer: {car.manufacturer.name} | Category: {car.category.name}")
            else:
                print("Car not found!")

        elif choice == "4":
            dealership.display_inventory()

        elif choice == "5":
            dealership.close()
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
