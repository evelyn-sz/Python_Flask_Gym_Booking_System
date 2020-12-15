class Member:

    def __init__(self, first_name, last_name, membership_type, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"