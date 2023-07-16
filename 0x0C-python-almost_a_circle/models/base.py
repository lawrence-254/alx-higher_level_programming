#!/usr/bin/python3
"""Defines a class base model."""
import json
import csv
import turtle


class Base:
    """Base model class.

    Private Attribute:
        __nb_object(int): number of bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Defines a new base.

        Args:
            id (int): an integer identifier for the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a list as JSON data.

        Args:
            list_dictionaries (list).
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list objects to a file as JSON data.

        Args:
            list_objs (list).
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns deserialized JSON.

        Args:
            json_string (str).

        Returns:
            Python list represented by json_string.
            Or Empty list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instant from a dictionary.

        Args:
            **dictionary (dict).
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON.

        That Reads from `<cls.__name__>.json`.

        Returns:
            A list of instantiated classes.
            Or An empty list.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """SavesCSV serialization of a list of objects to a file.

        Args:
            list_objs (list).
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            A list of instantiated classes.
            Or An empty list.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Uses turtle module to draw Squares and Rectangles.

        Args:
            list_squares (list).
            list_rectangles (list)
        """
        tortoise = turtle.Turtle()
        tortoise.screen.bgcolor("#b7312c")
        tortoise.pensize(3)
        tortoise.shape("turtle")

        tortoise.color("#ffffff")
        for rect in list_rectangles:
            tortoise.showturtle()
            tortoise.up()
            tortoise.goto(rect.x, rect.y)
            tortoise.down()
            for i in range(2):
                tortoise.forward(rect.width)
                tortoise.left(90)
                tortoise.forward(rect.height)
                tortoise.left(90)
            tortoise.hideturtle()

        tortoise.color("#b5e3d8")
        for sq in list_squares:
            tortoise.showturtle()
            tortoise.up()
            tortoise.goto(sq.x, sq.y)
            tortoise.down()
            for i in range(2):
                tortoise.forward(sq.width)
                tortoise.left(90)
                tortoise.forward(sq.height)
                tortoise.left(90)
            tortoise.hideturtle()

        turtle.exitonclick()
