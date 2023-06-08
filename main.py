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
    category_id = Column(Integer, ForeignKey('category.id'))
    manufacturer = relationship("Manufacturer", back_populates="cars")
    category = relationship("Category", back_populates="cars")
