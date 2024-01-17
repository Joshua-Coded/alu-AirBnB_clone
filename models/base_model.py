#!/usr/bin/python3

"""
This file defines the BaseModel class that
will serve as the base class for all models
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    """Base class for all classes"""

    def __init__(self, *args, **kwargs):
        """Constructor it either deserializes a
        serialized class or initialize a new instance"""
        # initialize if nothing is passed
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            return

        # using key words (deserialization)
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val

        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')

        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """override str representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the last variable"""
        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of sef"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Retrieves all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get all number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Create a new instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """ Retrieve an instance"""
        return models.storage.find_by_id(cls.__name__, instance_id)

    @classmethod
    def destroy(cls, instance_id):
        """ Delete an instance"""
        return models.storage.delete_by_id(cls.__name__, instance_id)

    @classmethod
    def update(cls, instance_id, *args):
        """update an instance if args has one element and it is a dictionary:
        it update by key value
        else:
        update by first being key and second being value"""
        if not len(args):
            print("** attribute name is missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(cls.__name__, instance_id, *args)
