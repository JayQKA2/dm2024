class Course:
    def __init__(self, name, id, credits):
        self.name = name
        self.id = id
        self.credits = credits

    def __repr__(self):
        return str(self.__dict__)