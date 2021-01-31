class DiceRoller:
    def __init__(self, dice_count=1):
        self.dice_count = dice_count

    def all_rolls(self):
        rolls = []
        if self.dice_count > 1:
            self.__generate_rolls((), rolls)
        else:
            for face in range(1, 21):
                rolls.append(face)
        return rolls
    
    def __generate_rolls(self, current_roll, rolls):
        if len(current_roll) == self.dice_count:
            rolls.append(current_roll)
        else:
            for die_roll in range(1, 21):
                self.__generate_rolls(current_roll + tuple([die_roll]), rolls)
