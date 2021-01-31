
from src.army.dice import DiceRoller


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
        assert rolls[0] == 1
        assert rolls[19] == 20
        
        