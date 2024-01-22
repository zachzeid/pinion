from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Database connection configuration


'''  
class JobProfile(Base):
    __tablename__ = 'job_profiles'

    id = Column(Integer, primary_key=True)
    job_role = Column(String)
    job_grade = Column(String)
    manager = Column(String)
    organization = Column(String)
    mandatory_systems = Column(JSON)
    optional_systems = Column(JSON)
    user_groups = Column(JSON)

    # Relationships
    users = relationship("User", back_populates="job_profile")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    job_profile_id = Column(Integer, ForeignKey('job_profiles.id'))

    # Relationships
    job_profile = relationship("JobProfile", back_populates="users")

Base.metadata.create_all(engine)

def create_job_profile(data):
    session = Session()
    job_profile = JobProfile(**data)
    session.add(job_profile)
    session.commit()
    return job_profile.id

def query_job_profile(profile_id):
    session = Session()
    job_profile = session.query(JobProfile).filter_by(id=profile_id).first()
    return job_profile

def update_job_profile(profile_id, update_data):
    session = Session()
    session.query(JobProfile).filter_by(id=profile_id).update(update_data)
    session.commit()

def delete_job_profile(profile_id):
    session = Session()
    session.query(JobProfile).filter_by(id=profile_id).delete()
    session.commit()

# Example usage
if __name__ == "__main__":
    job_profile_data = {
        "job_role": "Software Developer",
        "job_grade": "Level 2",
        "manager": "John Doe",
        "organization": "Engineering",
        "mandatory_systems": [{"name": "System A", "type": "SaaS"}, {"name": "System B", "type": "PaaS"}],
        "optional_systems": [{"name": "System C", "type": "IaaS"}],
        "user_groups": ["Developers", "Tech Leads"]
    }

    # Create a job profile
    profile_id = create_job_profile(job_profile_data)
    print(f"Created Job Profile with ID: {profile_id}")

    # Query the job profile
    retrieved_profile = query_job_profile(profile_id)
    print(f"Retrieved Job Profile: {retrieved_profile.job_role}")

    # Update the job profile
    update_job_profile(profile_id, {"job_grade": "Level 3"})
    updated_profile = query_job_profile(profile_id)
    print(f"Updated Job Profile Grade: {updated_profile.job_grade}")

    # Delete the job profile
    delete_job_profile(profile_id)
    deleted_profile = query_job_profile(profile_id)
    print(f"Deleted Job Profile: {deleted_profile}")
'''
DATABASE_URI = 'sqlite:///example.db'  # Replace with your database URI

Base = declarative_base()

# Association table for the many-to-many relationship between Offboards and Users
offboard_user_association = Table('offboard_user', Base.metadata,
    Column('offboard_id', Integer, ForeignKey('offboards.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)


class System(Base):
    __tablename__ = 'systems'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    iam_users = Column(JSON)
    iam_groups = Column(JSON)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)


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
