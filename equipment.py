class Equipment():
    name = ''
    speed = 0
    blocking = 0
    agility = 0
    scoring = 0

    # takes basically any argument passed in when creating an instance and sets attribute
    # ex. Monster(adjective='awesome') makes a 'self.adjective = awesome'
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


# Player equipment
# Sticks
class Good_Stick(Equipment):
    name = 'Good Stick'
    speed = -1
    scoring = 1

class Awesome_Stick(Equipment):
    name = 'Awesome Stick'
    speed = -2
    scoring = 3

class Light_Stick(Equipment):
    name = 'Light Stick'
    speed = 5
    scoring = -2

# Helmets
class Better_Helmet(Equipment):
    name = 'Better Helmet'
    scoring = 0
    speed = 1

# Skates
class Better_Skates(Equipment):
    name = 'Better Skates'
    speed = 3

# Goalie Equipment
# Pads
class Better_Pads(Equipment):
    name = 'Better Pads'
    blocking = 2
    agility = -1

class Great_Pads(Equipment):
    name = 'Great Pads'
    blocking = 3
    agility = -2

class Light_Pads(Equipment):
    name = 'Light Pads'
    blocking = -2
    agility = 4

# Helmets
class G_Better_Helmet(Equipment):
    name = 'Better Helmet'
    blocking = 0
    agility = 1

# Skates
class G_Better_Skates(Equipment):
    name = 'Better Skates'
    agility = 2