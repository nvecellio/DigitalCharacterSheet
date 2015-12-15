"""
This class will be called if a character can't be loaded at the beginning of
execution, or if we need to modify the current character
"""

class Player:

    def player_name(self, value=None, new=None):

        if value:
            self.player_name = value
            print "Name changed to {}".format(value)

        if new:
            self.player_name = raw_input(">> Please enter your name:\n>> ")

        return self.player_name

    def player_class(self, value=None, new=None):

        if value:
            self.player_class = value
            print "Class set to {}".format(value)

        if new:
            self.player_class = raw_input(">> Please enter your class:\n>> ")

        return self.player_class

    def player_level(self, value=None, new=None):

        if value:
            self.player_level = value
            print "Level set to {}".format(value)

        if new:
            input_level = raw_input(">> Please enter your level as a number:\n")

            # this only checks if input is int since we'll need this to be an int
            # later on. The other string values above don't need validation
            if input_level.isdigit():
                self.player_level = input_level
            else:
                while not input_level.isdigit():
                    input_level = raw_input(">> Please enter your level as a\
                                            number:\n")
                self.player_level = input_level

        return self.player_level
