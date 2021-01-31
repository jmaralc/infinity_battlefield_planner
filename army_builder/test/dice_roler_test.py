
class DiceRoller:
    def __init__(self):
        self.dice_count = 1

    def all_rolls(self):
        return range(1, 21)


class TestDiceRollerTest:
    def test_a_new_dice_roller_has_one_die(self,):
        roller = DiceRoller()

        assert roller.dice_count == 1

    def test_a_dice_roller_can_provide_all_dice_roll_combinations(self,):
        roller = DiceRoller()
        
        rolls = roller.all_rolls()

        assert len(rolls) == 20
        for (expected_value, value) in zip(range(1, 20), rolls):
            assert expected_value == value
