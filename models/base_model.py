#!/usr/bin/env python3
""" BaseModel that defines all common attributes/methods for other classes """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """ instantiates a new object """
       
        if len(args) > 0:
            for i in args[0]:
                setattr(self, i, args[0][i])
                """setattr is a function that takes two arguments:
                the name of the attribute to be set and the value to be
                assigned to it.
                """
       
        else:
       
            self.created_at = datetime.now()
            self.id = str(uuid4())
       
        for i in kwargs:
            print("kwargs: {}: {}".format(i, kwargs[i]))

 #   def __init__(self, *args, **kwargs):
 #          """ Initialize a new BaseModel
 #           Args:
 #               *args: variable length argument list
 #               **kwargs: key - value pairs
 #       """
 #       self.id = str(uuid4)
 #       self.created_at = datetime.datetime.now()
 #       current datetime when instance is created
 #       self.updated_at = datetime.datetime.now()
 #       """current datetime when instance is created and
 #       updated when change object"""

    def __str__(self):
        """ Returns a string representation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with current time"""
        from models.base_model import BaseModel
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        from models.base_model import BaseModel
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
       
        return new_dict
