from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String(20), nullable = False)
    last_name = Column(String(20), nullable=False)
    PESEL = Column(String(20), nullable = False)
    phone = Column(String(20), nullable=False)
    address = Column(String(50), nullable=False)

    def __repr__(self):
        return f'Student({self.id}, {self.first_name}, {self.last_name}, {self.PESEL}, {self.phone}, {self.address})'

