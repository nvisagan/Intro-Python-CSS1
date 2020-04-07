# Write a class to hold player information, e.g. what room they are in
# currently.
#5 lines
"""
 The player class that is called for movement.
 Includes a name 

"""
class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room   
        self.inventory = []

    def travel(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            print("Nice try, That way is blocked")

   def on_take(self, name):
        if getattr()
        
