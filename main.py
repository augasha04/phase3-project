from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the engine and connect to the database
engine = create_engine('sqlite:///AugashaMotors.db')
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
    brand = Column(String)
    color = Column(String)
    
    #the relationships
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
        
    def addingcar(self, make, model, year, category):
        car = Car (
        make = make,
        model = model,
        year = year,
        category = category
        )
        # Add a car
        self.session.add(car)
        self.session.commit()
        print("Car added successfully!")
        
    def remove_car(self, car_id):
        car = self.session.query(Car).get(car_id)
        if car:
            self.session.delete(car)
            self.session.commit()
            print("Car removed from Augasha Motors")
        else:
            print("Car not found at Augasha Motors Dealership!")
            
    def search_car(self, make, model, year):
        car = self.session.query(Car).filter_by(make=make, model=model).first()
        if car:
            return car
        else:
            return None
        
    def close(self):
        self.session.close()    
        
def main():
    
    #initialize carlist
    carlist = []
        
    
    # creating the car dealership menu
    choice = 0
    while choice != 4:
        print("*** CARS MENU ***")
        print("1. Order a car")
        print("2. Check a car")
        print("3. Print all cars")
        print("4. Exit")
        choice = int(input("ENTER YOUR CHOICE BTW (1-4):"))
        
        if choice == 1:
            print("You are ordering at Augasha Motors")
            nbrand = input ("The brand of the car: ")
            nprice = int(input ("The price of the car is: "))
            ncolor = input ("Color of car: ") 
            carlist.append([nbrand, nprice, ncolor])
            
        elif choice == 2:
            print("You are checking a car at Augasha Motors")
            keyword = input("search for a car at Augasha Motors: ")
            for car in carlist:
                if keyword in car:
                    print(car)
                    
        elif choice == 3:
            print("You are printing all cars at Augasha Motors")
            for i in range(len(carlist)):
                print(carlist[i])
                
        elif choice == 4:
            print("You are exiting the car dealership")
    print("Thank you, for doing business with Augasha.")
    
                        
           
if __name__ == "__main__":
    main()
