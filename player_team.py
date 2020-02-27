from action import Action


class Player(Action):
    name = ""
    scoring = 1
    stamina = 10
    confidence = 50
    # confused = 0

    skills = {
        'shoot': 0,
        'deke': 1,
        'spin': 3,
        'toe drag': 2,
        'fake': 2,
        'skate': 1
    }
    special_skills = {}

    def shoot(self):
        pass

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Crosby(Player):
    name = "Crosby"
    scoring = 82
    speed = 80
    special_skills = {
        'super backhand': 4
    }


class Stamkos(Player):
    name = "Stamkos"
    scoring = 85
    speed = 80
    special_skills = {
        'super wrister': 3
    }


class Ovechkin(Player):
    name = "Ovechkin"
    scoring = 85
    speed = 78
    special_skills = {
        'super slapshot': 5
    }


class Malkin(Player):
    name = "Malkin"
    scoring = 83
    speed = 76
    special_skills = {
        'shoot everybody': 4
    }


class Weber(Player):
    name = "Weber"
    scoring = 80
    speed = 74
    special_skills = {
        'super slapshot': 9
    }
