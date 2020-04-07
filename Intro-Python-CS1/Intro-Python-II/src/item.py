class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        display_string = f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        return display_string


    