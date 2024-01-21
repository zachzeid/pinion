from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Database connection configuration
DATABASE_URI = 'sqlite:///example.db'  # Replace with your database URI

Base = declarative_base()

# Association table for the many-to-many relationship between Offboards and Users
offboard_user_association = Table('offboard_user', Base.metadata,
    Column('offboard_id', Integer, ForeignKey('offboards.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    manager = Column(String)
    organization = Column(String)
    title = Column(String)
    systems = relationship('System', back_populates='user')
    offboards = relationship('Offboard', secondary=offboard_user_association, back_populates='users')

class System(Base):
    __tablename__ = 'systems'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    date_added = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='systems')

class Offboard(Base):
    __tablename__ = 'offboards'

    id = Column(Integer, primary_key=True)
    scheduled_date = Column(DateTime)
    executed_date = Column(DateTime)
    executed_by = Column(String)
    users = relationship('User', secondary=offboard_user_association, back_populates='offboards')
    system_id = Column(Integer, ForeignKey('systems.id'))
    system = relationship('System')

def get_engine():
    return create_engine(DATABASE_URI)

def initialize_database(engine):
    Base.metadata.create_all(engine)

# This function can be called from outside to initialize the database
if __name__ == "__main__":
    engine = get_engine()
    initialize_database(engine)
