import pickle
import sys
import os

class Main():

    path = os.getenv('HOME') + '/Documents/CharSheet/'

    def __init__(self):
        player = raw_input(">> Speak your name, adventurer:\n>> ")

        player_data = self.load(player)
        if player_data:
            print 'Welcome back, {player}'.format(player=player)
        else:
            if not self.save_dir(player, check_path=True):
                self.save_dir(player, make_path=True)
            elif not self.save_dir(player, check_file=True):
                self.new_player(player)


    def load(self, name, path=path):
        file_name = '{name}.p'.format(name=name)
        save_file = path + '/{file}'.format(file=file_name)
        if os.path.isfile(save_file):
            try:
                #TODO: Make the load function work. it probably doesnt because that file is empty
                player_data = pickle.load(open(save_file, 'rb'))
                return player_data
            except Exception:
                raise
        else:
            return False

    def save_dir(self, name, path=path, make_path=False, check_path=False, check_file=False):
        file_name = '{name}.p'.format(name=name)
        if check_path:
            return os.path.isdir(path)
        if check_file:
            return os.path.isfile(path + file_name)
        if make_path:
            if not os.path.isdir(path):
                try:
                    os.makedirs(path + name)
                    return True
                except Exception as e:
                    print 'Failed creating directory'
                    sys.exit(e)
        else:
            return False

    def new_player(self, name, path=path):
        file = str(path + '{name}.p'.format(name=name))
        try:
            open(file, 'wb')
            return True
        except Exception as e:
            sys.exit(e)

    def save(self, name, player, path=path):
        file = str(path + '{name}.p'.format(name=name))
        try:
            pickle.dump(player, file)
            return True
        except Exception as e:
            sys.exit(e)

    def menu(self, name):
        print("""
        Hello, and welcome, {name}. What would you like to do?
        1. View/Edit Basics        2. View/Edit Attributes
        3. View/Edit Skills        4. View/Edit Spells
        5. View/Edit Inventory     5. View/Edit Traits
        6. Roll the dice
        """.format(name=name))
        choice = raw_input('>> ')

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
                except:
                    pass

