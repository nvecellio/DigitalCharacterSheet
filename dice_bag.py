import random
"""
# DiceRoller
# - roll(x)
# -- rolls dice in range
# -- accepts modifiers, based on int input or skill value
#
# - multi-roll(args)
# -- accepts modifiers, based on int input or skill value
# -- roll all dice specified in line
# -- print each roll separately
#
# - saving_throw(ability)
# -- roll saving throw based on ability
#
# - attack(count=None, bonus=None)
# -- display menu of attacks available
# -- roll dice based on attack
#
# - death_save
# -- modify combat.death_saves
#
# - advantage
# -- account for advantage
#
# - disadvantage
# -- account for disadvantage
"""

def roll_dice(sides=None):
    print random.randrange(1, sides)
