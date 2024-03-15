class Person:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def __repr__(self):
        return str(self.__dict__)