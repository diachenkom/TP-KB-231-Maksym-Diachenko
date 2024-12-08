class Student:
    def __init__(self, name: str, phone: str, kurs: str, group: str):        
        self.name = name
        self.phone = phone
        self.kurs = kurs
        self.group = group

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Course: {self.kurs}, Group: {self.group}"

    def update(self, name=None, phone=None, kurs=None, group=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if kurs:
            self.kurs = kurs
        if group:
            self.group = group