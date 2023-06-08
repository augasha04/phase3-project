from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Creating the engine and connecting to the database
engine = create_engine('sqlite:///car_dealership.db')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

#defining the car class
class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))   
    manufacturer = relationship("Manufacturer", back_populates="cars")
    
# Defining the Manufacturer table
class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    # Defining the primary key
    # Defining the columns
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    # Creating the tables
    Base.metadata.create_all(engine)
    
    # Creating a session
    session = Session()
    
    # Creating a new car
    new_car = Car(make="Ford", model="Mustang", year=1)
    new_car = Car(make="Ford", model="Mustang", year=1)
    

   


