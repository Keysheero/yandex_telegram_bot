
from sqlalchemy import MetaData, Integer, Column, String, ARRAY, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

metadata: MetaData = MetaData()
Base = declarative_base(metadata=metadata)


class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phones = Column(ARRAY(String), nullable=False)
    teleg_id = Column(String, nullable=False, unique=True)
    car_id = Column(String, unique=True)
    car_category = Column(ARRAY(String), nullable=False)
    orders = relationship('Order', back_populates='driver')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    driver_id = Column(String, ForeignKey(Driver.id))
    driver = relationship('Driver', back_populates='orders')