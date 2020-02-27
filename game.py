import random
import sys

import logging

from player_team import *
from opposing import *
from equipment import *

class Game():

    def show_stats(self):
        print("\nScore Chance: {}, Block Chance: {}, Shoot: {}, Block: {}".format(self.scoring_chance,
                                                                                self.blocking_chance,
                                                                                self.player.scoring,
                                                                                self.goalie.blocking))

    def show_player_stats(self):
        print("\nPlayer: {}, Scoring: {}, Speed: {}, Stamina: {}, Confidence: {}".format(
            self.player.name,
            self.player.scoring,
            self.player.speed,
            self.player.stamina,
            self.player.confidence))

    def show_goalie_stats(self):
        print("Goalie: {}, Blocking: {}, Agility: {}, Stamina: {}, Confidence: {}".format(
            self.goalie.name,
            self.goalie.blocking,
            self.goalie.agility,
            self.goalie.stamina,
            self.goalie.confidence))

    def help_input(self, help_level):
        print("Your choices are:")
        if help_level == 1:
            print("\nY or N")
        elif help_level == 2:
            print("\nRegular Skills:")
            for x in self.all_player_choices:
                print(x.title())
            print("\nSpecial Skills:")
            for x in self.player_specials:
                print(x.title())
        elif help_level == 3:
            print("\nRegular Skills:")
            for x in self.all_goalie_choices:
                print(x.title())
            print("\nSpecial Skills:")
            for x in self.goalie_specials:
                print(x.title())

    def select_player(self):
        choice = True
        while choice:
            print("\nPlayers:")
            for player in self.players:
                print(player.name)
            player_choice = input("\nWho do you want to be? ").title().strip()

            for player in self.players:
                if player_choice == player.name:
                    self.player = player
                    choice = False
                    break
            if choice:
                print("That player is not playing today, try again.")

        equip = input("Do you want to equip better equipment? (Y/N) ").lower().strip()
        if equip[0] == 'y':
            choice = True
            while choice:
                for s in self.sticks:
                    print(s.name)
                stick_choice = input("Pick a stick: ").title().strip()

                for stick in self.sticks:
                    if stick_choice == stick.name:
                        self.equipped = stick
                        choice = False
                if choice:
                    print("That is not an available stick, try again.")
            if self.equipped:
                self.player.scoring += self.equipped.scoring
                self.player.speed += self.equipped.speed

        self.all_player_choices = self.player.skills
        self.player_specials = self.player.special_skills

        if self.two_player == 1:
            self.goalie = random.choice(self.goalies)
            print("\nSelected {} as a random goalie".format(self.goalie.name))
        del equip

    def select_goalie(self):
        choice = True
        while choice:
            print("\nGoalies:")
            for goalie in self.goalies:
                print(goalie.name)
            player_choice = input("\nWho do you want to be? ").title().strip()

            for goalie in self.goalies:
                if player_choice == goalie.name:
                    self.goalie = goalie
                    choice = False
                    break
            if choice:
                print("That player is not playing today, try again.")

        equip = input("Do you want to equip better equipment? (Y/N) ").lower().strip()
        if equip[0] == 'y':
            choice = True
            while choice:
                for p in self.pads:
                    print(p.name)
                pad_choice = input("Pick your pads: ").title().strip()

                for pad in self.pads:
                    if pad_choice == pad.name:
                        self.equipped = pad
                        choice = False
                if choice:
                        print("Those are not available pads, try again.")
                if self.equipped:
                    self.goalie.blocking += self.equipped.blocking
                    self.goalie.agility += self.equipped.agility

        self.all_goalie_choices = self.goalie.skills
        self.goalie_specials = self.goalie.special_skills

        del equip

    def set_base_stats_and_skills(self):
        self.hold_score_stat = self.player.scoring
        self.hold_speed_stat = self.player.speed
        self.hold_blocking_stat = self.goalie.blocking
        self.hold_agility_stat = self.goalie.agility
        self.hold_player_confidence = self.player.confidence
        self.hold_goalie_confidence = self.goalie.confidence

        # self.all_player_choices = self.player.skills
        # self.player_specials = self.player.special_skills
        # self.all_goalie_choices = self.goalie.skills
        # self.goalie_specials = self.goalie.special_skills

    def setup(self):
        self.players = [
            Crosby(),
            Stamkos(),
            Malkin(),
            Ovechkin(),
            Weber()
            ]

        self.sticks = [
            Good_Stick(),
            Awesome_Stick(),
            Light_Stick()
        ]

        self.goalies = [
            Fleury(),
            Holtby(),
            Niemi(),
            Crawford(),
            Lundqvist()
            ]

        self.pads = [
            Better_Pads(),
            Great_Pads(),
            Light_Pads()
        ]

        self.select_player()

        if self.two_player == 2:
            self.select_goalie()

        self.set_base_stats_and_skills()

        # copy base stats for players and goalies to reset after each shot

        self.show_player_stats()
        self.show_goalie_stats()

        # set up initial try stats
        # self.reset_chances()
        self.player_wins = 0
        self.player_goals = 0
        self.goalie_wins = 0
        self.total_blocks = 0
        self.total_goals = 0

    def reset_chances(self):
        # original scoring chance formula
        # self.scoring_chance = random.randint(1, 100)
        # self.blocking_chance = random.randint(1, 100)

        # confidence based scoring chance formula
        self.scoring_chance = random.randint(int(self.player.confidence * 0.5), self.player.confidence + 5)
        self.blocking_chance = random.randint(int(self.goalie.confidence * 0.5), self.goalie.confidence + 5)
        self.player_choice = ''
        self.goalie_choice = ''
        self.deke_count = 0
        self.spin_count = 0
        self.poke_check = False
        self.totally_fooled = False
        self.choice_count = 0
        self.skate_count = 0
        self.toe_drag_count = 0
        self.fake_count = 0

    def shooter_play(self):

        while self.player_choice not in self.all_player_choices or self.player_choice != 'shoot':
            choice = input("\nGo to the goal, what do you do? ").lower().strip()
            self.choice_count += 1

            # switch statement for shots
            if choice == 'shoot':
                self.show_stats()
                # if self.two_player == 1:
                #     self.goalie_action()
                #     self.shot_outcome()
                break
            elif choice == 'deke' and self.enough_stamina(choice, self.player):
                self.deke_count += 1
                self.player.scoring += self.player.skills[choice]
                self.player.stamina -= self.player.skills[choice]
            elif choice == 'spin' and self.enough_stamina(choice, self.player):
                self.player.scoring += self.player.skills[choice]
                self.player.stamina -= self.player.skills[choice]
                self.spin_count += 1
            elif choice == 'skate' and self.enough_stamina(choice, self.player):
                self.player.speed += self.player.skills[choice]
                self.player.stamina -= self.player.skills[choice]
                self.skate_count += 1
            elif choice == 'toe drag' and self.enough_stamina(choice, self.player):
                self.player.scoring += self.player.skills[choice]
                self.player.speed -= self.player.skills[choice] * 2
                self.player.stamina -= self.player.skills[choice]
                self.toe_drag_count += 1
            elif choice == 'fake' and self.enough_stamina(choice, self.player):
                self.player.scoring += self.player.skills[choice]
                self.player.stamina -= self.player.skills[choice]
                self.fake_count += 1
            elif choice in self.player.special_skills and self.enough_special_stamina(choice, self.player):
                self.player.scoring += self.player.special_skills[choice]
                self.player.stamina -= self.player.special_skills[choice]
                self.show_stats()
                # if self.two_player == 1:
                #     self.goalie_action()
                #     self.shot_outcome()
                break
            elif choice == 'help':
                self.help_input(2)
            elif choice not in self.player.skills:
                print("\nI don't understand, you better figure")
                print("out what you want to do quickly!")
                self.confused += 1
                if self.confused >= 3:
                    self.poke_check = True

            if self.poke_check == True:
                self.misses += 1
                self.blocks += 1
                print("\nThe goalie poke checked you and you lost the puck")
                self.player.confidence -= 5
                self.goalie.confidence += 1
                break

    def goalie_play(self):

        while self.goalie_choice not in self.all_player_choices or self.goalie_choice != 'block':
            choice = input("\nPlayer made his move, what do you do? ").lower().strip()

            if choice == 'block':
                self.show_stats()
                # if self.two_player == 1:
                #     self.goalie_action()
                #     self.shot_outcome()
                break
            elif choice == 'poke check' and self.enough_stamina(choice, self.goalie):
                self.deke_count += 1
                self.goalie.blocking += self.goalie.skills[choice]
                self.goalie.stamina -= self.goalie.skills[choice]
            elif choice == 'stand tall' and self.enough_stamina(choice, self.goalie):
                self.goalie.blocking += self.goalie.skills[choice]
                self.goalie.stamina -= self.goalie.skills[choice]
                self.spin_count += 1
            # elif choice == 'skate' and self.enough_stamina(choice):
            #     self.player.speed += self.goalie.skills[choice]
            #     self.player.stamina -= self.goalie.skills[choice]
            #     self.skate_count += 1
            # elif choice == 'toe drag' and self.enough_stamina(choice):
            #     self.player.scoring += self.player.player_skills[choice]
            #     self.player.speed -= self.player.player_skills[choice] * 2
            #     self.player.stamina -= self.player.player_skills[choice]
            #     self.toe_drag_count += 1
            # elif choice == 'fake' and self.enough_stamina(choice):
            #     self.player.scoring += self.player.player_skills[choice]
            #     self.player.stamina -= self.player.player_skills[choice]
            #     self.fake_count += 1
            elif choice in self.goalie.special_skills and self.enough_special_stamina(choice, self.goalie):
                self.goalie.blocking += self.goalie.special_skills[choice]
                self.goalie.stamina -= self.goalie.special_skills[choice]
                self.show_stats()
                # if self.two_player == 1:
                #     self.goalie_action()
                #     self.shot_outcome()
                break
            elif choice == 'help':
                self.help_input(3)
            elif choice not in self.goalie.skills:
                print("\nI don't understand, you better figure")
                print("out what you want to do quickly!")
                self.confused += 1
                if self.confused >= 3:
                    self.totally_fooled = True

            if self.totally_fooled == True:
                self.goals += 1
                self.player_goals += 1
                print("\nYou were totally fooled and you were scored on")
                self.goalie.confidence -= 5
                self.player.confidence += 1
                break

    def reset_stats(self):
        self.player.scoring = self.hold_score_stat
        self.player.speed = self.hold_speed_stat
        self.goalie.blocking = self.hold_blocking_stat
        self.goalie.agility = self.hold_agility_stat

    def shot_outcome(self):
        shot_attempt = (self.scoring_chance * self.player.scoring * (self.player.speed * 0.5)) // 200
        block_attempt = (self.blocking_chance * self.goalie.blocking * (self.goalie.agility * 0.5)) // 200
        #if self.scoring_chance * self.player.scoring > self.blocking_chance * self.goalie.blocking:
        if shot_attempt > block_attempt:
            print("\nYOU MADE THE SHOT!")
            self.goals += 1
            self.player_goals += 1
            self.total_goals += 1
            if self.player_choice in self.player.special_skills:
                self.player.confidence += 4
            else:
                self.player.confidence += 3
            if self.goals > 3:
                print("\nYou're shooting like a mad man!\n")
                self.goalie.confidence -= 1
        else:
            print("\nBLOCKED!")
            self.misses += 1
            self.blocks += 1
            self.total_blocks += 1
            if self.goalie_choice in self.goalie.special_skills:
                self.goalie.confidence +=4
            else:
                self.goalie.confidence += 3
            if self.blocks > 3:
                print("\nYou're standing on your head!\n")
                self.player.confidence -= 1

        self.show_player_stats()
        self.show_goalie_stats()
        print("\nShot: {}; Block: {}".format(shot_attempt,
                                             round(block_attempt, 0)))

    def goalie_action(self):
        goalie_move = random.randint(1, 10)
        if goalie_move < 6:
            # picks the value from a random key
            move = random.choice(list(self.goalie.skills.items()))[1]
            self.goalie.blocking += move
            self.goalie.stamina -= move
            # prints the key of the previously randomly chosen value
            print("\n**Goalie move: {}".format(list(self.goalie.skills.keys())[list(self.goalie.skills.values()).index(move)]))

    def enough_stamina(self, choice, player):
        enough = True
        if player.stamina < player.skills[choice]:
            enough = False
            print("\nYou don't have enough stamina for that move")
        return enough

    def enough_special_stamina(self, choice, player):
        enough = True
        if player.stamina < player.special_skills[choice]:
            enough = False
            self.confused += 1
            print("\nYou don't have enough stamina for that move")
        return enough

    def how_many_players(self):
        two_player = 0
        while two_player != 1 or two_player != 2:
            try:
                two_player = int(input("How many players? (1 or 2) "))
                if two_player == 1 or two_player == 2:
                    return two_player
            except:
                continue

    def __init__(self):

        print("\nSHOOTOUT CHALLENGE!")
        print("Type 'help' at any time to see options\n")
        game_count = 0
        shootout = input("PLAY? (Y/N) ").lower().strip()
        # if shootout == 'y':
        #     self.setup()
        if shootout[0] == 'n':
            print("Goodbye")
            sys.exit()
        while shootout[0] == 'y':# or shootout[0] != 'n':
            if game_count < 1:
                self.two_player = self.how_many_players()
                self.setup()
            if shootout[0] == 'y':
                self.reset_chances()
                self.shots = 0
                self.misses = 0
                self.blocks = 0
                self.goals = 0
                self.player.stamina = 10
                self.goalie.stamina = 10
                while self.shots < 5:
                    print("\n" + '*'*20 + "\n{} v {}".format(self.player.name, self.goalie.name))
                    print("Chance {}".format(self.shots + 1))
                    self.reset_chances()
                    self.reset_stats()
                    self.confused = 0

                    self.shooter_play()
                    if self.two_player == 2 and self.poke_check != True:
                        self.confused = 0
                        # This is to take the screen down so you can't see what the player did before you.
                        # You could just scroll up, but until I can clear the terminal this is how it must be done
                        print("\n"*20)
                        self.goalie_play()

                    if self.poke_check != True and self.totally_fooled != True:
                        if self.two_player == 1:
                            self.goalie_action()
                            self.shot_outcome()
                        else:
                            self.shot_outcome()

                    self.shots += 1
                    if self.goals >= 3 or self.misses >= 3:
                        break

                if self.goals > self.misses:
                    print("\n{} scored {} out of 5 shots on {} and wins!\n\n".format(self.player.name,
                                                                                     self.goals,
                                                                                     self.goalie.name))
                    self.player_wins += 1
                else:
                    print("\n{} blocked {} out of 5 shots from {} and wins!\n\n".format(self.goalie.name,
                                                                                        self.blocks,
                                                                                        self.player.name))
                    self.goalie_wins += 1

            elif shootout == 'help':
                self.help_input(1)
                continue
            game_count += 1
            # print(game_count)
            shootout = input("PLAY AGAIN? (Y/N) ").lower().strip()

            if shootout[0] == 'y':
                revert = input("RESET GAME? (Y/N) ").lower().strip()
                if revert[0] == 'y':
                    self.two_player = self.how_many_players()
                    self.setup()
                    continue
                else:
                    reset = input("\nChange Player? (Y/N) ").lower().strip()
                    if reset[0] == 'y':
                        self.select_player()
                    if self.two_player == 2:
                        reset = input("\nChange Goalie? (Y/N) ").lower().strip()
                        if reset[0] == 'y':
                            self.select_goalie()
                continue
            print("Player wins: {} - Goals: {}\nGoalie wins: {} - Blocks: {}".format(self.player_wins,
                                                                                 self.total_goals,
                                                                                 self.goalie_wins,
                                                                                 self.total_blocks))
        sys.exit()

Game()