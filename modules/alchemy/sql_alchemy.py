# SQLAlchemy 1.3 Documentation: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# Example: https://github.com/graphql-python/graphene-sqlalchemy/tree/master/examples/flask_sqlalchemy
# Many to many, ...: https://github.com/auth0-blog/sqlalchemy-orm-tutorial

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.sql import exists


engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost:3306/fyks", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(32))
    username = Column(String(20), unique=True)
    age = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', age='%d')>" % (self.name, self.surname, self.age)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('addresses'))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(bind=engine)

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()

try:
    user = User(name='esaadd', surname='Ed afsdf', username='affadf', age=20)
    exists = session.query(exists().where(username=user.username)).scalar()

    session.add(user)
except Exception as e:
    print(e)

session.commit()
