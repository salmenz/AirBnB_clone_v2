#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import os
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)



class DBStorage():
    """ 
    class
    """
    __engine = None
    __session = None
    all_classes = ['Amenity',
                   'City',
                   'Review',
                   'Place',
                   'User',
                   'State']

    def __init__(self):
        """init"""
        self.__engine = create_engine
        ('mysql+mysqldb://{}:{}@{}/{}'.format
         (os.getenv("HBNB_MYSQL_USER"),
          os.getenv("HBNB_MYSQL_PWD"),
          os.getenv("HBNB_MYSQL_HOST"),
          os.getenv("HBNB_MYSQL_DB")),
         pool_pre_ping=True)                                                               if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of objects which their name is specified """
        mylist = list()
        newdict = dict()
        if cls is not None:
            obj = eval(cls)
            mylist = self.__session.query(obj).all()
            for item in mylist:
                key = item.__class__.__name__ + "." + item.id
                newdict[key] = item
        else:
            for obj in self.all_classes:
                obj = eval(obj)
                mylist = self.__session.query(obj).all()
                for item in mylist:
                    key = item.__class__.__name__ + "." + item.id
                    newdict[key] = item
        return (newdict)

    def new(self, obj):
        """ Adds a new object to the database """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes made in current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an existing object from the database """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in database and set a session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(expire_on_commit=False)
        session_factory.configure(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()
