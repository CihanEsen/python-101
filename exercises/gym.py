class Gym:
    def __init__(self, capacity):
        self.capacity = capacity
        self.active_members = 0

    def enter(self, group):
        if self.active_members + group.number_of_people > self.capacity:
            return False
        self.active_members += group.number_of_people
        return True

    def leave(self, group):
        self.active_members -= group.number_of_people


class Group:
    def __init__(self, number_of_people):
        self.number_of_people = number_of_people

