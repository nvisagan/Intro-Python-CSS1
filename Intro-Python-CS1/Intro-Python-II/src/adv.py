from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. Small rocks fall from the top."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. A rusty sword lies next to a corpse"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. A few coins can be found on the ground."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. A lonely scroll sits perched on a flat stone. The only exit is to the south."""),
}

item = {
    'outside':  Item("rock", 
                    "A rock, you're only companion on this adventure."),
    'foyer':    Item("sword",
                    "A weak weapon but it might come in handy"),
    'overlook': Item("rope",
                    "A rope but not long enough to cross the chasm"),
    'narrow':   Item("coins",
                    "Few gold coins, is there treasure nearby"),
    'treasure': Item("scroll",
                    "The scroll reads of another treasure, but was the real treasure the adventure")
         
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#Ask for name and welcome them 
player = Player(input("What is your name traveler: "), room['outside'])
print("Welcome to game", player.name)

directions = ["n", "s", "e", "w"]


while True:
    #Get intial game control
    cmd = input(f"Where to {player.name}:").lower()
    # Check n/s/e/w/q
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
    elif cmd == f"get "
    elif cmd == "i":
        print(f"You open your bag:{player.inventory}")   
    elif cmd == "q":
        # Quit game
        print(f"Great Quest {player.name}, More treasure awaits!")
        exit()
    else:
        print("I did not recognize that command. Please enter n, s, e, w to move")

