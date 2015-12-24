

class Attributes:

    attributes = {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'intelligence': 0,
        'wisdom': 0,
        'charisma': 0
    }

    modifiers = {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'intelligence': 0,
        'wisdom': 0,
        'charisma': 0
    }

    modifier_values = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3,
            6: -2, 7: -2, 8: -1, 9: -1, 10: 0,
            11: 0, 12: 1, 13: 1, 14: 2, 15: 2,
            16: 3, 17: 3, 18: 4, 19: 4, 20: 5,
            21: 5, 22: 6, 23: 6, 24: 7, 25: 7,
            26: 8, 27: 8, 28: 9, 29: 9, 30: 10
    }

    def __init__(self):
        menu_choice = self.menu
        if menu_choice == 1:
            self.show_all()
        elif menu_choice == 2:
            self.edit_all()
        elif menu_choice == 3:
            self.change_attribute()

    def change_attribute(self, attribute=None, value=None):
        if not attribute and not value:
            print '>> Please type an attribute to modify\n'
            for attr, value in self.attributes:
                print attr
            attribute = raw_input(">> ")
        if attribute not in self.attributes:
            print 'Not an attribute, please try again'
            while attribute not in self.attributes:
                print 'Please try again'
                attribute = raw_input(">> ")
        choice = raw_input(">> Please enter a numerical value:\n>> ")
        try:
            value = int(choice)
            self.attributes[attribute] = value
            return True
        except ValueError:
            pass
            while type(choice) != int:
                print "You have not entered a number, please try again"
                choice = raw_input(">> Please select an option...")
                try:
                    value = int(choice)
                    self.attributes[attribute] = value
                    return True
                except ValueError:
                    pass

    def edit_all(self):
        for attr, value in self.attributes.iteritems():
            choice = raw_input(">> Enter value for {}".format(attr))
            try:
                value = int(choice)
                self.attributes[attr] = value
            except ValueError:
                pass
                while type(choice) != int:
                    print "You have not entered a number, please try again"
                    choice = raw_input(">> Please select an option...")
                    try:
                        value = int(choice)
                        return value
                    except:
                        pass

    def set_modifiers(self):
        for attr, value in self.modifiers.iteritems():
            attribute_val = self.attributes[attr]
            self.modifiers[attr] = self.modifier_values[attribute_val]

    def get_attribute(self, attribute):
        if attribute in self.attributes:
            return self.attributes[attribute]
        else:
            print 'Not an attribute, please try again'

    def show_all(self):
        print 'Strength     @==]====> ' + str(self.attributes['strength'])
        print 'Dexterity    @==]====> ' + str(self.attributes['dexterity'])
        print 'Constitution @==]====> ' + str(self.attributes['constitution'])
        print 'Intelligence @==]====> ' + str(self.attributes['intelligence'])
        print 'Wisdom       @==]====> ' + str(self.attributes['wisdom'])
        print 'Charisma     @==]====> ' + str(self.attributes['charisma'])

    def menu(self):
        print """
        @==]======>
        1. View all attributes      2. Edit all attributes
        3. Edit single attribute    4. View modifiers
        <======]==@
        """
        choice = raw_input(">> Please select an option...")

        try:
            value = int(choice)
            return value
        except ValueError:
            pass
            while type(choice) != int:
                print "You have not entered a number, please try again"
                choice = raw_input(">> Please select an option...")
                try:
                    value = int(choice)
                    return value
                except ValueError:
                    pass