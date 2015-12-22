

class Attributes():

    attributes = {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'intelligence': 0,
        'wisdom': 0,
        'charisma': 0
    }

    STR = attributes['strength']
    DEX = attributes['dexterity']
    CON = attributes['constitution']
    INT = attributes['intelligence']
    WIS = attributes['wisdom']
    CHA = attributes['charisma']

    def __init__(self):
        print 'place holder'

    def change_attribute(self, attribute, value):
        if attribute not in self.attributes:
            print 'Not an attribute, please try again'
            return False
        try:
            int(value)
            self.attributes[attribute] = value
            return True
        except:
            print 'Not a number, please try again'
            pass

    def get_attribute(self, attribute):
        if attribute in self.attributes:
            return self.attributes[attribute]
        else:
            print 'Not an attribute, please try again'

    def show_all(self):
        for k, v in self.attributes.iteritems():
            print '{attribute} @==]====> {value}'.format(attribute=k, value=v)

#TODO: Create and return modifiers based on attributes