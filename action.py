import random


class Action():

    def deke(self, deke_count):
        if deke_count < 4:
            return 1
        else:
            return -1


    def shoot(self):
        return None

    def spin(self, spin_count):
        if spin_count < 1:
            return 3
        else:
            return -10


    def poke_check(self):
        return None


