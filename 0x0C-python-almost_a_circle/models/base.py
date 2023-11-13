#!/usr/bin/python3
"""module"""
import json
from os.path import exists
import csv
import turtle
import time
from random import random


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """"json"""

        i = list_dictionaries
        if i is None or type(i) is not list or len(i) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"file save"""

        n = cls.__name__
        liste = []
        if list_objs is not None:
            for i in list_objs:
                liste.append(i.to_dictionary())
        with open(n + ".json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(liste))

    @staticmethod
    def from_json_string(json_string):
        """"json"""

        i = json_string
        if i is None or type(i) is not str or len(i) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"create"""

        n = cls.__name__
        if n == "Rectangle":
            t = cls(1, 1)
        elif n == "Square":
            t = cls(1)
        else:
            t = None
        t.update(**dictionary)
        return t

    @classmethod
    def load_from_file(cls):
        """"file"""

        n = cls.__name__ + ".json"
        if not exists(n):
            return []
        with open(n, "r+", encoding="utf-8") as file:
            t = cls.from_json_string(file.read())
        liste = []
        for i in t:
            liste.append(cls.create(**i))
        return liste

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"file"""
        n = cls.__name__
        liste = []
        if list_objs is not None:
            if n == "Rectangle":
                for i in list_objs:
                    liste.append([i.id, i.width, i.height, i.x, i.y])
            else:
                for i in list_objs:
                    liste.append([i.id, i.size, i.x, i.y])
        with open(n + ".csv", "w+", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """"from file"""

        n = cls.__name__
        if not exists(n + ".csv"):
            return []
        with open(n + ".csv", "r+", encoding="utf-8", newline='') as file:
            t = csv.reader(file)
            liste = []
            for j in t:
                j = [int(i) for i in j]
                if n == "Rectangle":
                    di = {"id": j[0], "width": j[1], "height": j[2],
                            "x": j[3], "y": j[4]}
                elif n == "Square":
                    di = {"id": a[0], "size": a[1], "x": a[2], "y": a[3]}
                else:
                    return []
                liste.append(cls.create(**di))
        return liste

    @staticmethod
    def draw(list_rectangles, list_squares):
        shapes = list_rectangles + list_squares
        for a in shapes:
            draw = turtle.Turtle()
            draw.color(random(), random(), random())
            draw.setpos(-a.x, -a.y)
            draw.pensize(7)
            draw.pendown()
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.end_fill()

        time.sleep(10)
