class Event(object):
    def __init__(self):
        self.count = 0
        self.data = {}

    def add(self, msg):
        self.count += 1
        self.data.update({f'event {self.count}': msg})

    def get_data(self):
        if self.count:
            return self.data
        return {"message": "The required data was already in the database"}


WIDTH = 1200
HEIGHT = 800
