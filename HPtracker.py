class Mob:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def hp_set(self):
        print(self.name + " hp has been set.")

    def oof(self):
        damage = int(input("Enter damage: "))
        self.hp -= damage

    def results(self):
        print(self.name + " reduced to", self.hp, "HP.")


print("HP bars setup. Enter values for 10 enemies. If there is less than 10, set HP to 0 for empty slots:")
mob1 = Mob("Enemy#1", int(input("Set HP for Enemy#1: ")))
mob1.hp_set()

mob2 = Mob("Enemy#2", int(input("Set HP for Enemy#2: ")))
mob2.hp_set()

mob3 = Mob("Enemy#3", int(input("Set HP for Enemy#3: ")))
mob3.hp_set()

mob4 = Mob("Enemy#4", int(input("Set HP for Enemy#4: ")))
mob4.hp_set()

mob5 = Mob("Enemy#5", int(input("Set HP for Enemy#5: ")))
mob5.hp_set()

mob6 = Mob("Enemy#6", int(input("Set HP for Enemy#6: ")))
mob6.hp_set()

mob7 = Mob("Enemy#7", int(input("Set HP for Enemy#7: ")))
mob7.hp_set()

mob8 = Mob("Enemy#8", int(input("Set HP for Enemy#8: ")))
mob8.hp_set()

mob9 = Mob("Enemy#3", int(input("Set HP for Enemy#9: ")))
mob9.hp_set()

mob10 = Mob("Enemy#10", int(input("Set HP for Enemy#10: ")))
mob10.hp_set()

print("HP bars set up successfully.")

print('Enemy#1 HP', mob1.hp)
print('Enemy#2 HP', mob2.hp)
print('Enemy#3 HP', mob3.hp)
print('Enemy#4 HP', mob4.hp)
print('Enemy#5 HP', mob5.hp)
print('Enemy#6 HP', mob6.hp)
print('Enemy#7 HP', mob7.hp)
print('Enemy#8 HP', mob8.hp)
print('Enemy#9 HP', mob9.hp)
print('Enemy#10 HP', mob10.hp)

while mob1.hp > 0 or mob2.hp > 0 or mob3.hp > 0 or mob4.hp > 0 or mob5.hp > 0 or mob6.hp > 0 or mob7.hp > 0 or mob8.hp > 0 or mob9.hp > 0 or mob10.hp > 0:
    target = int(input("Enter target number: "))
    match target:
        case 1:
            mob1.oof()
            mob1.results()
        case 2:
            mob2.oof()
            mob2.results()
        case 3:
            mob3.oof()
            mob3.results()
        case 4:
            mob4.oof()
            mob4.results()
        case 5:
            mob5.oof()
            mob5.results()
        case 6:
            mob6.oof()
            mob6.results()
        case 7:
            mob7.oof()
            mob7.results()
        case 8:
            mob8.oof()
            mob8.results()
        case 9:
            mob9.oof()
            mob9.results()
        case 10:
            mob10.oof()
            mob10.results()
        case _:
            print("Enter a valid target number.")


print("All enemies have been defeated!")
input("Press any key to continue.")
