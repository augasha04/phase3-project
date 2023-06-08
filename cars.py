from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Creating the engine
engine = create_engine('sqlite:///AugashaMotors.db')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()

# Creating the base class for declarative models
Base = declarative_base()

# creating an association table for the relationship
class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    
    #the relationship between the nanufacturer table and the category table
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
    



