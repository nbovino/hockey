from action import Action

class Goalie(Action):# extend monster from object if you need this to work in python 2 as well
    name = ""
    blocking = 1
    agility = 1
    stamina = 10
    confidence = 50

    skills = {
        'block' : 0,
        'poke check' : 2,
        'stand tall' : 3
    }

    special_skills = {}

    # other attributes


    def __init__(self, **kwargs):
        # takes basically any argument passed in when creating an instance and sets attribute
        # ex. Monster(adjective='awesome') makes a 'self.adjective = awesome'
        for key, value in kwargs.items():
            setattr(self, key, value)


class Fleury(Goalie):
    name = "Fleury"
    blocking = 85
    agility = 87
    special_skills = {
        'super butterfly' : 4
    }


class Holtby(Goalie):
    name = "Holtby"
    blocking = 82
    agility = 85
    special_skills = {
        'super stick' : 5
    }


class Niemi(Goalie):
    name = "Niemi"
    blocking = 86
    agility = 84
    special_skills = {
        'super save' : 5
    }


class Crawford(Goalie):
    name = "Crawford"
    blocking = 85
    agility = 82
    special_skills = {
        'tomahawk' : 3
    }


class Lundqvist(Goalie):
    name = "Lundqvist"
    blocking = 83
    agility = 83
    special_skills = {
        'super glove' : 2
    }