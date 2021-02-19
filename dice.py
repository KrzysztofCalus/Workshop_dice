import random

possible_dices = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)

def dice_code():
    """
    Simulate dice throws
    :return: Integer; dice throws result
    """
    user_input = input("Insert dice:")
    for dice in possible_dices:
        if dice in user_input:
            try:
                throws_number, optional = user_input.split(dice)
                optional = int(optional) if optional else 0
                throws_number = int(throws_number) if throws_number else 1
                dice_number = int(dice[1:])
                throws_result = [random.randint(1, dice_number) for _ in range(throws_number)]
                return sum(throws_result) + optional
            except ValueError:
                return "Wrong input"
            break
    else:
        return "Wrong Input"

print(dice_code())