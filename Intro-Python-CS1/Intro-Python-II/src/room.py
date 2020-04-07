# Implement a class to hold room information. This should have name and
# description attributes.
# 15 lines
"""
The Room class that can call the description and the name of the room

"""

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
    
    def __str__(self):
        display_string = f"\n-----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None