# !/usr/bin/python3
"""base for other classes"""

class Base:
    """Represents base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Retursn the JSON string represenation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        
        return json.dumps(list_dictionaries)