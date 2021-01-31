
class DiceRoller:
    def __init__(self, dice_count=1):
        self.dice_count = dice_count

    def all_rolls(self):
        rolls = []
        self.__generate_rolls((), rolls)
        return rolls
    
    def __generate_rolls(self, current_roll, rolls):
        if len(current_roll) == self.dice_count:
            rolls.append(current_roll)
        else:
            for die_roll in range(1, 21):
                self.__generate_rolls(current_roll + tuple([die_roll]), rolls)


class TestDiceRollerTest:
    def test_a_new_dice_roller_has_one_die(self,):
        roller = DiceRoller()

        assert roller.dice_count == 1

    def test_a_roller_can_have_multiple_dice(self,):
        roller = DiceRoller(2)

        assert roller.dice_count == 2

    def test_a_roller_can_provide_all_dice_roll_combinations_for_2_dice(self,):
        roller = DiceRoller(2)
        
        rolls = roller.all_rolls()

        assert len(rolls) == 20*20
        assert rolls[0] == (1, 1)
        assert rolls[1] == (1, 2)

    def test_a_roller_can_provide_all_dice_roll_combinations_for_3_dice(self,):
        roller = DiceRoller(3)
        
        rolls = roller.all_rolls()

        assert len(rolls) == 20*20*20
        assert rolls[0] == (1, 1, 1)
        assert rolls[1] == (1, 1, 2)

    def test_a_dice_roller_can_provide_all_dice_roll_combinations(self,):
        roller = DiceRoller()
        
        rolls = roller.all_rolls()

        assert len(rolls) == 20
        assert rolls[0] == (1,)  # Make this pretty...
        assert rolls[19] == (20,)
        
        