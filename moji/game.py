import sys
from moji.character import Character
from moji.monster import Dragon
from moji.monster import Goblin
from moji.monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            if input("Dodge? Y/N ").lower() == 'y':
                if not self.player.dodge():
                    self.player.hit_points -= 1
                    print("Monster hit you!")
                else:
                    print("Monster missed!")
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
        else:
            print("{} isn't attacking.".format(self.monster))

    def player_turn(self):

        choice = input("Do you want to ([A]ttack, [R]est or [Q]uit): ").lower()
        if choice == 'a':
            print("You're attacking {}!".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}!".format(
                        self.monster, self.player.weapon))
            else:
                print("You missed!")
        elif choice == 'r':
            self.player.rest()
        elif choice == 'q':
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + "=" * 20)
            print(self.player)
            self.monster_turn()
            print("-" * 20)
            self.player_turn()
            self.cleanup()
            print("\n" + "=" * 20)
        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()


Game()
