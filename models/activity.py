class Activity:

    def __init__(self, name, venue, category, capacity, finished = False, offpeak = False, id = None):
        self.name = name
        self.venue = venue
        self.category = category
        self.capacity = capacity
        self.finished = finished
        self.offpeak = offpeak
        self.id = id