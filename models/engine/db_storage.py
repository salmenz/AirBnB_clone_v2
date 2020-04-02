#!/usr/bin/python3
"""db_storage engine"""
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)


class DBStorage():
    """class"""
    __engine = None
    __session = None
    classes = ['Amenity',
               'City',
               'User',
               'Review',
               'State',
               'Place']

    def __init__(self):
        """init"""
        self.__engine = create_engine
        ('mysql+mysqldb://{}:{}@{}/{}'.format
         (os.environ['HBNB_MYSQL_USER'],
          os.environ['HBNB_MYSQL_PWD'],
          os.environ['HBNB_MYSQL_HOST'],
          os.environ['HBNB_MYSQL_DB']),
         pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        return a dictionary: (like FileStorage)
        """
        d = {}
        objects = []
        if cls:
            objects = self.__session.query(eval(cls)).all()
        else:
            for item in self.classes:
                objects += self.__session.query(eval(item)).all()
        d = {obj.__class__.__name__ + '.' + obj.id: obj for obj in objects}
        return d

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in database and
        create the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(expire_on_commit=False)
        session_factory.configure(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

